const btnExit = document.getElementById("btn-exit")
const userAvatarBase = document.getElementById('user_avatar')

if (btnExit != null) {
    btnExit.addEventListener("click", () => {
        localStorage.clear();
    })
}

function setAvatar(userAvatar, data) {
    if (data['avatar'] && userAvatar) {
        userAvatar.src = data['avatar']
    }
}

window.addEventListener('load', () => {
    if (!(window.location.href.includes('/user/login/') || window.location.href.includes('/user/register/'))) {
        fetch('/user/get_current_user/', {
            method: 'GET',
            headers: {
                'JS-Request': 'True',
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => {
                setAvatar(userAvatarBase, data)
            })
    }
})