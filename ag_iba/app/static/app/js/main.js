$(document).ready(function() {
    console.log("JQuery activated");

    // // handlers for datepickers
    // $('#input_plate_date').focus(function() {
    //     $('#input_plate_date').datepicker('show');
    // });
    // $('#input_due_date').focus(function() {
    //     $('#input_due_date').datepicker('show');
    // });

    // // js code for the login page ->

    // // tooltips
    // $('[rel=tooltip]').tooltip();

    // // signup form
    // $("#signup_form").submit(function(event) {
    //     return (validateNewUsername() && validateNewPassword() && matchPasswords());
    // });

    // // signin form
    // $("#signin_form").submit(function() {
    //     return (validateSignInUsername() && validateSignInPassword());
    // });

    // // <-- js code for the login page

    // $("#add_client_form").submit(function(){
    //     return (validateClientName() &&
    //         validateClientAddress() &&
    //         validateClientCity() &&
    //         validateClientVillage() &&
    //         validateClientPostal() &&
    //         validateClientNif()
    //     );
    // });
});

// // search user input handler
//     $("#find-user-input").bindWithDelay(
//         "keyup",
//         function() {
//             var query = $(this).val().trim().toLowerCase();
//             $('.user').each(function(){
//                 var username = $(this).find('.media-heading a').html().toLowerCase();
//                 var pos = username.indexOf(query);
//                 if (pos != -1) {
//                     $(this).show();
//                 } else {
//                     $(this).hide();
//                 }
//             });
//         },
//         250, true);

(function($){
    $('#local-search-clients').bindWithDelay(
        "keyup",
        function() {
            var query = $(this).val().trim().toLowerCase();
            $('.client_row').each(function(){
                var $row = $(this);
                var client_name = $row.find('td>a').text().trim().toLowerCase();

                if(client_name.indexOf(query) !== -1) {
                    $row.show();
                } else {
                    $row.hide();
                }
            });

            if($('.client_row:visible').length === 0) {
                $('table + p').removeClass('hidden');
            } else {
                $('table + p').addClass('hidden');
            }
        },
        250,
        true
    );
})(jQuery)

// function validateInput(value, pattern, object) {
//     var OK = pattern.exec(value);

//     if(!OK) { // invalid input
//         object.next().removeClass('hide');
//         object.parents('.form-group').addClass('has-error');
//         return false;
//     } else {
//         object.next().addClass('hide');
//         object.parents('.form-group').removeClass('has-error');
//         return true;
//     }
// }

// function validateSignInUsername() {
//     var username = $("#input_username_1").val().trim();
//     return validateInput(username, /^[a-z0-9A-Z._]{4,64}$/, $("#input_username_1"));
// }

// function validateSignInPassword() {
//     var password = $("#input_password_1").val().trim();
//     return validateInput(password, /^[a-zA-Z0-9.,-:;_!#$%&*~]{6,30}$/, $("#input_password_1"));
// }

// function validateNewUsername() {
//     var username = $("#input_username_2").val().trim();
//     console.log("here");
//     return validateInput(username, /^[a-z0-9A-Z._]{4,64}$/, $("#input_username_2"));
// }

// function validateNewPassword() {
//     var password = $("#input_password_2").val().trim();
//     return validateInput(password, /^[a-zA-Z0-9.,-:;_!#$%&*~]{6,30}$/, $("#input_password_2"));
// }

// function matchPasswords() {
//     var password1 = $("#input_password_2").val().trim();
//     var password2 = $("#input_password_3").val().trim();

//     if(password1 != password2) {
//         $("#input_password_3").next().removeClass("hide");
//         $("#input_password_3").parent(".form-group").addClass("has-error");
//         return false;
//     } else {
//         $("#input_password_3").next().addClass("hide");
//         $("#input_password_3").parent(".form-group").removeClass("has-error");
//         return true;
//     }
// }

// function validateClientName() {
//     var input_name = $("#input_name");
//     var name = input_name.val().trim();
//     return validateInput(name, /^([a-zA-Z\u00C0-\u00ff,-.]+ )+[a-zA-Z,-.]+$/, input_name);
// }

// function validateClientAddress() {
//     var address = $("#input_address").val().trim();
//     return validateInput(address, /^[a-zA-Z0-9\u00C0-\u00ff,:-_ ªº]{6,}$/, $("#input_address"));
// }

// function validateClientCity() {
//     var city = $("#input_city").val().trim();
//     return validateInput(city, /^[a-zA-Z\u00C0-\u00ff. ]{3,}$/, $("#input_city"));
// }

// function validateClientVillage() {
//     var village = $("#input_village").val().trim();
//     return validateInput(village, /^[a-zA-Z\u00C0-\u00ff. ]{3,}$/, $("#input_village"));
// }

// function validateClientPostal() {
//     var postal = $("#input_postal").val().trim();
//     return validateInput(postal, /^[0-9]{4}(-[0-9]{3})?$/, $("#input_postal"));
// }

// function validateClientNif() {
//     nif_input = $("#input_nif");
//     var nif = nif_input.val().trim();
//     if(validateInput(nif, /^[125689][0-9]{8}$/, nif_input)) {
//         if(!validateNif(nif)){
//             nif_input.next().text("NIF inválido.");
//             nif_input.next().removeClass('hide');
//             nif_input.parents('.form-group').addClass('has-error');
//             return false;
//         } else {
//             nif_input.next().text("Deve ter 9 algarismos e começar por um dos seguintes: 1, 2, 5, 6, 7, 8 ou 9.");
//             nif_input.next().addClass('hide');
//             nif_input.parents('.form-group').removeClass('has-error');
//             return true;
//         }
//     }
// }

// function validateNif(nif) {
//     var control = nif[0] * 9;
//     for(var i = 2; i <= 8; i++) {
//         control += nif[i-1] * (10-i);
//     }
//     control = 11 - (control % 11);
//     if(control >= 10) {
//         control = 0;
//     }
//     return nif[8] == control;
// }

// function checkNifType() {
//     var nif = $("#input_nif").val().trim();
//     if("12".indexOf(nif[0]) != -1) {
//         $("#input_nif").parent().prev().text("NIF");
//     } else if("56789".indexOf(nif[0]) != -1) {
//         $("#input_nif").parent().prev().text("NIPC");
//     } else {
//         $("#input_nif").parent().prev().text("NIF/NIPC");
//     }
// }

