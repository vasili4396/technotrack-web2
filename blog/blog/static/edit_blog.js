$(document).ready(function () {
    function openDialog() {
        $('.modal').modal('show');
    }

    $(document).on('click', '.editLink', function (event) {
        openDialog();
        $.get(this.href, function (data) {
            $('#blogEdit').html(data);
        });
        event.preventDefault();
    });

    $(document).on('submit', '[data-formtype="ajaxForm"]', function (event) {
        $.post(this.action, $(this).serialize(), function (data) {
            if (data == "OK") document.location.reload();
            else $('#blogEdit').html(data);
        });
        event.preventDefault();
    });
});



