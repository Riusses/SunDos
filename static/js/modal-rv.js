$(function() {
    $('.close').click(function() {
        $('#modal-item').hide();
        $('#modal-item iframe').attr("src", $("#modal-item iframe").attr("src"));
    });
});