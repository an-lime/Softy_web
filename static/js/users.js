const togglePassword =
    document.getElementById('togglePasswordBtn');

const password =
    document.getElementById('password');

const password2 =
    document.getElementById('password2');

togglePassword.addEventListener('click', function (e) {

    const type = password.getAttribute(
        'type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);

    if (password.getAttribute(
        'type') === 'password') {
        togglePassword.src = pathToImages.concat("password_show.png");
    } else {
        togglePassword.src =
            pathToImages.concat("password_hide.png");
    }

    if (password2 != null) {
        console.log(123)
        password2.setAttribute('type', password.getAttribute('type'))
    }

    if (password2 == null) {
        console.log(1234)}
});