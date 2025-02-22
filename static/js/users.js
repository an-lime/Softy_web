const togglePassword = document.getElementById('togglePasswordBtn');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');
const form = document.getElementById("form-login");
const inputLogin = document.getElementById("username");

function setNext() {
    const url = window.location.href;
    const paramNext = new URL(url).searchParams.get("next");
    if (paramNext) {
        const form = document.getElementById("form-login");
        let input = document.createElement("input")
        input.type = "hidden";
        input.name = "next"
        input.value = paramNext;
        form.insertAdjacentElement("afterbegin", input);
    }
}

togglePassword.addEventListener('click', () => {

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
        password2.setAttribute('type', password.getAttribute('type'))
    }
});

window.addEventListener("load", () => {

    if (localStorage.getItem("username")) {
        inputLogin.value = localStorage.getItem("username");
    }

    setNext();
})

form.addEventListener("submit", () => {
    localStorage.setItem("username", inputLogin.value)
})