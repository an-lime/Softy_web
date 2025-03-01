const togglePassword = document.getElementById('togglePasswordBtn');
const username = document.getElementById("username");
const password1 = document.getElementById('password1');
const password2 = document.getElementById('password2');
form_register = document.getElementById("form-register")

togglePassword.addEventListener('click', () => {

    const type = password1.getAttribute(
        'type') === 'password' ? 'text' : 'password';
    password1.setAttribute('type', type);

    if (password1.getAttribute(
        'type') === 'password') {
        togglePassword.src = pathToImages.concat("password_show.png");
    } else {
        togglePassword.src =
            pathToImages.concat("password_hide.png");
    }

    if (password2 != null) {
        password2.setAttribute('type', password1.getAttribute('type'))
    }
});

window.addEventListener("load", () => {

    document.title = "Регистрация";

    if (localStorage.getItem("username")) {
        username.value = localStorage.getItem("username");
    }
})

form_register.addEventListener("submit", () => {
    localStorage.setItem("username", username.value);
})