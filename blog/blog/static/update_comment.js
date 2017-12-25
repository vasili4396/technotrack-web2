function updateComments() {
    $.get(document.URL + "comments/", function (data) {
        $("#tag_comments").replaceWith(data);
    });
};
setInterval(updateComments, 5000);

