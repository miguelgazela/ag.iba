
var BASE_URL = "http://localhost:8000/agiba/";

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

$(document).ready(function() {

    
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


// local search for clients
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

    $('#local_search_car').bindWithDelay(
        'keyup',
        function() {
            var query = $(this).val().trim().toLowerCase();
            $('.client_car_row').each(function() {
                var $row = $(this);
                var brand = $row.find('td:nth-child(2)').text().trim().toLowerCase();

                if(brand.indexOf(query) !== -1) {
                    $row.show();
                } else {
                    $row.hide();
                }
            });

            if($('.client_car_row:visible').length === 0) {
                $('table + p').removeClass('hidden');
            } else {
                $('table + p').addClass('hidden');
            }
        },
        250,
        true
    );
})(jQuery);

function payTax(link, taxId, currentUrl) {
    $link = $(link);
    var limitDate = new Date($link.parents('tr').attr('data-limit-date'));
    var nextDate = new Date(limitDate.getFullYear()+1, limitDate.getMonth(), limitDate.getDate());

    changeTax(limitDate, nextDate, taxId, currentUrl, 'api/impostos/pagar');
    return false; // prevent default behavior
}

function cancelTax(link, taxId, currentUrl) {
    $link = $(link);
    var limitDate = new Date($link.parents('tr').attr('data-limit-date'));
    var previousDate = new Date(limitDate.getFullYear()-1, limitDate.getMonth(), limitDate.getDate());

    changeTax(limitDate, previousDate, taxId, currentUrl, 'api/impostos/cancelar');
    return false; // prevent default behaviour
}

function changeTax(currentDate, changedDate, taxId, currentUrl, requestUrl) {
    var warning = "Alterar data limite de pagamento de " + currentDate.getDate() + "/" + (currentDate.getMonth()+1) + "/" + currentDate.getFullYear();
    warning += " para " + changedDate.getDate() + "/" + (changedDate.getMonth()+1) + "/" + changedDate.getFullYear() + "?";

    var confirmation = confirm(warning);

    if(confirmation) {
        $.ajax({
            url: BASE_URL + requestUrl + '/' + taxId,
            method: 'POST',
            dataType: 'json',
            success: function(response) {
                if(response['status'] === 'success') {
                    window.location = BASE_URL + currentUrl;
                } else {
                    alert("Ooops, alguma coisa correu mal. Tenta outra vez mais tarde.");
                }
            }
        }).fail(function() {
            alert("Ooops, alguma coisa correu mal. Tenta outra vez mais tarde.");
        });
    }
}

function removeClient(url) {

    var confirmation = confirm("Tem a certeza que deseja apagar este cliente?");

    if(confirmation) {
        $.ajax({
            url: url,
            method: 'POST',
            dataType: 'json',
            success: function(response) {
                if(response['status'] === 'success') {
                    window.location = '/agiba/clientes';
                } else {
                    alert("Ooops, alguma coisa correu mal. Tenta outra vez mais tarde.");
                }
            }
        }).fail(function() {
            alert("Ooops, alguma coisa correu mal. Tenta outra vez mais tarde.");
        });
    }
}

function removeTax(url, nextUrl) {
    $.ajax({
        url: url,
        method: "POST",
        dataType: "json",
        success: function(response) {
            if(response['status'] === 'success') {
                window.location = nextUrl;
            } else {
                alert("Ooops, alguma coisa correu mal. Tenta outra vez mais tarde.");
            }
        }
    }).fail(function() {
        alert("Ooops, alguma coisa correu mal. Tenta outra vez mais tarde.");
    });
}

