$(document).ready(function() {
    console.log("JQuery activated");

    // handlers for datepickers
    $('#input_plate_date').focus(function() {
        $('#input_plate_date').datepicker('show');
    });
    $('#input_due_date').focus(function() {
        $('#input_due_date').datepicker('show');
    });


    // tooltips
    $('[rel=tooltip]').tooltip();
});

function validateNewUsername() {
    var username = $("#input_username_2").val().trim();
    var OK = /^[a-z0-9A-Z._]{4,64}$/.exec(username);

    if(!OK) { // invalid username
        $("#input_username_2").next().removeClass("hide");
        $("#input_username_2").parent(".form-group").addClass("has-error");
    } else {
        $("#input_username_2").parent(".form-group").removeClass("has-error");
        $("#input_username_2").next().addClass("hide");
    }
}

function validateNewPassword() {
    var password = $("#input_password_2").val().trim();
    var OK = /^[a-zA-Z0-9.,-:;_!#$%&*~]{6,30}$/.exec(password);

    if(!OK) { // invalid password
        $("#input_password_2").next().removeClass("hide");
        $("#input_password_2").parent(".form-group").addClass("has-error");
    } else {
        $("#input_password_2").next().addClass("hide");
        $("#input_password_2").parent(".form-group").removeClass("has-error");
    }
}

function matchPasswords() {
    var password1 = $("#input_password_2").val().trim();
    var password2 = $("#input_password_3").val().trim();

    if(password1 != password2) {
        $("#input_password_3").next().removeClass("hide");
        $("#input_password_3").parent(".form-group").addClass("has-error");
    } else {
        $("#input_password_3").next().addClass("hide");
        $("#input_password_3").parent(".form-group").removeClass("has-error");   
    }
}