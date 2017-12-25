from __future__ import unicode_literals
from django.views.generic import ListView, CreateView, UpdateView, View, DetailView
from django.shortcuts import get_object_or_404, reverse, HttpResponseRedirect, HttpResponse
from .models import Blog, Post, Category, Like
from django import forms
from comment.models import Comment


class BlogForm(forms.ModelForm):
    search = forms.CharField(required=False)
    order_by = forms.ChoiceField(choices=(
        ('name', 'A->Z'),
        ('-name', 'Z->A'),
        ('-createdata', 'Last created in the beg'),
        ('createdata', 'Last created in the end'),
    ), required=False)

    class Meta:
        model = Blog
        fields = 'name',


class BlogList(ListView):
    template_name = "blog/blogpage.html"
    context_object_name = 'blog'
    model = Blog

    def get_queryset(self):
        q = super(BlogList, self).get_queryset()
        self.form = BlogForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(name=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['customform1'] = self.form
        context['category'] = Blog.category
        bdict = dict(self.request.GET)
        bdict.pop('page', None)
        from urllib.parse import urlencode
        context['querypart'] = urlencode(bdict)
        for blogs in context['blog']:
            blogs.form = BlogForm(instance=blogs)

        return context


class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = 'name', 'category',


class NewBlog(CreateView):
    form_class = NewBlogForm
    template_name = 'blog/new_blog.html'

    def get_success_url(self):
        return reverse('blog:listOfBlogs')

    def get_context_data(self, **kwargs):
        context = super(NewBlog, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewBlog, self).form_valid(form)


class BlogUpdate(UpdateView):
    template_name = 'blog/edit_blog.html'
    model = Blog
    fields = 'name', 'category'

    def form_valid(self, form):
        if self.object.author == self.request.user:
            super(BlogUpdate, self).form_valid(form)
            return HttpResponse("OK")
        else:
            return HttpResponseRedirect(404)

    def get_queryset(self):
        return super(BlogUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('blog:listOfBlogs')

#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#
#------------------------------------------------------------------------#


class PostList(ListView):
    template_name = "blog/posts_list.html"
    context_object_name = 'posts'
    model = Post
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=self.kwargs['ident'])
        return super(PostList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        return context


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'postname', 'text'


class NewPost(CreateView):
    form_class = NewPostForm
    template_name = 'blog/new_post.html'

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=self.kwargs['ident'], author=request.user)
        return super(NewPost, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:concretePost', kwargs={'ident': self.object.id})

    def form_valid(self, form):
        form.instance.blog_id = self.kwargs['ident']
        form.instance.author = self.request.user
        return super(NewPost, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NewPost, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        return context


class PostUpdate(UpdateView):
    template_name = 'blog/edit_post.html'
    model = Post
    fields = 'postname', 'text'

    def form_valid(self, form):
        if self.object.author == self.request.user:
            return super(PostUpdate, self).form_valid(form)
        else:
            return HttpResponseRedirect(404)

    def get_queryset(self):
        return super(PostUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('blog:concretePost', kwargs={'ident': self.object.id})


class PostPage(CreateView):
    template_name = "blog/post_page.html"
    context_object_name = 'post'
    model = Comment
    fields = ('text', )

    def dispatch(self, request, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=self.kwargs['ident'])
        return super(PostPage, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostPage, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        context['blog'] = self.postobject.blog
        context['likes'] = Like.objects.filter(post=self.postobject).count()
        context['comment_list'] = Comment.objects.filter(post=self.postobject)
        return context

    def get_success_url(self):
        return reverse('blog:concretePost', kwargs={'ident': self.object.post.id})

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.post_id = self.kwargs['ident']
            form.instance.author = self.request.user
            return super(PostPage, self).form_valid(form)
        else:
            return HttpResponseRedirect(reverse('core:login'))


class PostComments(CreateView):
    template_name = "blog/comments.html"
    context_object_name = 'post'
    model = Comment
    fields = ('text',)

    def get_context_data(self, **kwargs):
        self.postobject = get_object_or_404(Post, id=self.kwargs['ident'])
        context = super(PostComments, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context


class PostLikeAjaxView(View):

    def dispatch(self, request, *args, **kwargs):
        self.post_object = get_object_or_404(Post, id=self.kwargs['ident'])
        return super(PostLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated() or not self.post_object.likes.filter(author=self.request.user).exists():
            b2 = Like(author=self.request.user, post=self.post_object)
            b2.save()
            return HttpResponse(Like.objects.filter(post=self.post_object).count())