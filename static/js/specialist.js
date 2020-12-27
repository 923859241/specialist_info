
function add_schoollist() {
    return true;
}

function update_respecial() {
    var phone = $('#phone').val();
    var email = $('#email').val();

    var rePhone = /^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/
    var reEmail = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/
    
    $('#phone').removeClass("input-error");
    $('#email').removeClass("input-error");

    if (!rePhone.test(phone)) {
        $('#phone').addClass("input-error");
        return false;
    }

    if (!reEmail.test(email)) {
        $('#email').addClass("input-error");
        return false;
    }

    return true;
}