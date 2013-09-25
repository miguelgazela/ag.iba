$(document).ready(function() {
    console.log("JQuery activated");

    // handlers for datepickers
    $('#input_plate_date').focus(function() {
        $('#input_plate_date').datepicker('show');
    });
    $('#input_due_date').focus(function() {
        $('#input_due_date').datepicker('show');
    });


    $('input[type="checkbox"').click(function(e) {
        console.log("Clicked a checkbox");
    });
});
