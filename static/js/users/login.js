const togglePassword = document.getElementById('togglePasswordBtn');
const password = document.getElementById('password');
const form_login = document.getElementById("form-login");

function setNext() {
    const url = window.location.href;
    const paramNext = new URL(url).searchParams.get("next");
    if (paramNext) {
        const form_login = document.getElementById("form-login");
        let input = document.createElement("input")
        input.type = "hidden";
        input.id = 'next'
        input.name = "next"
        input.value = paramNext;
        form_login.insertAdjacentElement("afterbegin", input);
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
});

window.addEventListener("load", () => {

    document.title = "Авторизация";
    setNext();
})

form_login.addEventListener("submit", async function (event) {
    event.preventDefault()
    const formData = new FormData(form_login)

    try {
        const response = await fetch(`/user/api/auth/login/`, {
            method: 'POST',
            headers: {
                'JS-Request': 'True',
            },
            body: formData,
        });

        if (response.ok) {
            const data = await response.json()
            window.location.href = data.redirected_url
        } else {
            const btnEnter = document.getElementById('btn-enter');
            btnEnter.insertAdjacentHTML('afterend', `<div style="position: absolute" id="div-error-parent">
                                                                        <div id="message">
                                                                            Неверный логин или пароль!
                                                                        </div>
                                                                    </div>`);
            const divErrorParent = document.getElementById('div-error-parent');
            if (divErrorParent) {
                setTimeout(() => {
                    divErrorParent.remove()
                }, 2500);
            }
        }
    } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
        alert('Произошла ошибка при авторизации. Попробуйте снова.');
    }
})