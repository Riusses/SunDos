var password = document.getElementById("id_password"),
    confirm_password = document.getElementById("id_repeat_password");

function validatePassword() {
    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Les contrasenyes no coincideixen");
    }
    else {
        confirm_password.setCustomValidity('');
    }
}
password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;