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
})

form_register.addEventListener("submit", async function (event) {
    event.preventDefault()
    const formData = new FormData(form_register)

    try {
        const response = await fetch(`/user/api/auth/register/`, {
            method: 'POST',
            headers: {
                'JS-Request': 'True',
            },
            body: formData
        });
        if (response.ok) {
            const data = await response.json()
            window.location.href = data.redirected_url
        } else {
            const errorData = await response.json();
            console.log(errorData)
        }

    } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
        alert('Произошла ошибка при регистрации. Попробуйте снова.');
    }
})

document.getElementById('avatar').addEventListener('change', (event) => {
    checkImage(event)
})