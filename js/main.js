$(document).ready(function() {
    console.log("JQuery activated");

    $('#dp2').datepicker('show');

    $('input[type="checkbox"').click(function(e) {
        console.log("Clicked a checkbox");
    });
});
