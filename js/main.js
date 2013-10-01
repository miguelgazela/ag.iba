$(document).ready(function() {
    console.log("JQuery activated");

    // handlers for datepickers
    $('#input_plate_date').focus(function() {
        $('#input_plate_date').datepicker('show');
    });
    $('#input_due_date').focus(function() {
        $('#input_due_date').datepicker('show');
    });

    // js code for the login page ->

    // tooltips
    $('[rel=tooltip]').tooltip();

    // signup form
    $("#signup_form").submit(function(event) {
        return (validateNewUsername() && validateNewPassword() && matchPasswords());
    });

    // signin form
    $("#signin_form").submit(function() {
        return true;
        //return (validateSignInUsername() && validateSignInPassword());
    });

    // <-- js code for the login page
});

function validateInput(value, pattern, object) {
    var OK = pattern.exec(value);

    if(!OK) { // invalid input
        object.next().removeClass('hide');
        object.parents('.form-group').addClass('has-error');
        return false;
    } else {
        object.next().addClass('hide');
        object.parents('.form-group').removeClass('has-error');
        return true;
    }
}

function validateSignInUsername() {
    var username = $("#input_username_1").val().trim();
    return validateInput(username, /^[a-z0-9A-Z._]{4,64}$/, $("#input_username_1"));
}

function validateSignInPassword() {
    var password = $("#input_password_1").val().trim();
    return validateInput(password, /^[a-zA-Z0-9.,-:;_!#$%&*~]{6,30}$/, $("#input_password_1"));
}

function validateNewUsername() {
    var username = $("#input_username_2").val().trim();
    console.log("here");
    return validateInput(username, /^[a-z0-9A-Z._]{4,64}$/, $("#input_username_2"));
}

function validateNewPassword() {
    var password = $("#input_password_2").val().trim();
    return validateInput(password, /^[a-zA-Z0-9.,-:;_!#$%&*~]{6,30}$/, $("#input_password_2"));
}

function matchPasswords() {
    var password1 = $("#input_password_2").val().trim();
    var password2 = $("#input_password_3").val().trim();

    if(password1 != password2) {
        $("#input_password_3").next().removeClass("hide");
        $("#input_password_3").parent(".form-group").addClass("has-error");
        return false;
    } else {
        $("#input_password_3").next().addClass("hide");
        $("#input_password_3").parent(".form-group").removeClass("has-error");
        return true;
    }
}

function validateClientName() {
    var name = $("#input_name").val().trim();
    return validateInput(name, /^([a-zA-Z\u00C0-\u00ff,-.]+ )+[a-zA-Z,-.]+$/, $("#input_name"));
}

function validateClientAddress() {
    var address = $("#input_address").val().trim();
    return validateInput(address, /^[a-zA-Z0-9,:-_ªº]$/, $("#input_address"));
}