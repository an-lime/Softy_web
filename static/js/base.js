const btnExit = document.getElementById("btn-exit")
const btnYourLikes = document.getElementById("btn-your-likes")
const btnYorComments = document.getElementById("btn-your-comments")
const leftColumnContent = document.getElementById('left-column-content')

if (btnExit != null) {
    btnExit.addEventListener("click", () => {
        localStorage.clear();
    })
}

document.addEventListener("DOMContentLoaded", () => {
    fetch('/get_current_user/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            if (btnExit != null) {
                if (data['is_authenticated']) {
                    leftColumnContent.insertAdjacentHTML("afterbegin",
                        "<div class=\"profile-div\">\n" +
                        "<img src=\"https://kamtk.ru:9096/el-zurnal/el-dnevnik/Css/image1/profile.png\" alt=\"profile_image\"\n" +
                        "class=\"img_profile\">\n" +
                        "<a href=\"#\">Профиль</a>\n" +
                        "</div>")

                    btnYourLikes.style.display = 'block';
                    btnYorComments.style.display = 'block';
                    btnExit.style.display = 'block';
                } else {
                    leftColumnContent.insertAdjacentHTML("afterbegin",
                        "<div class=\"profile-div\">\n" +
                        "<a href=\"#\" id=\"login-a\">Авторизация</a>\n" +
                        "<a href=\"#\" id=\"register-a\">Регистрация</a>\n" +
                        "</div>")

                    const loginBtn = document.getElementById("login-a")
                    const registerBtn = document.getElementById("register-a")

                    fetch('/user/get_login_url/', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken'),
                            'Content-Type': 'application/json'
                        }
                    })
                        .then(response => response.json())
                        .then(data => {
                            loginBtn.href = data['login_url']
                        })

                    fetch('/user/get_register_url/', {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken'),
                            'Content-Type': 'application/json'
                        }
                    })
                        .then(response => response.json())
                        .then(data => {
                            registerBtn.href = data['register_url']
                        })

                    btnYourLikes.style.display = 'none';
                    btnYorComments.style.display = 'none';
                    btnExit.style.display = 'none';
                }
            }
        })
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}