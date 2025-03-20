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

function checkImage(event) {
    const file = event.target.files[0];
    if (file) {

        const allowedTypes = ['image/png', 'image/jpeg', 'image/jpg'];
        const allowedExtensions = ['png', 'jpeg', 'jpg'];
        const fileExtension = file.name.split('.').pop().toLowerCase();

        if (!allowedTypes.includes(file.type) || !allowedExtensions.includes(fileExtension)) {
            alert('Выберите файл изображения');
            event.target.value = '';
        } else if (file.size > 8 * 1024 * 1024) {
            alert('Файл слишком большой. Максимальный размер - 8 Мб');
            event.target.value = '';
        }
    }
}

document.getElementById('avatar').addEventListener('change', (event) => {
    checkImage(event)
})