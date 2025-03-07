const btnExit = document.getElementById("btn-exit")
const userAvatarBase = document.getElementById('user_avatar')

if (btnExit != null) {
    btnExit.addEventListener("click", () => {
        localStorage.clear();
    })
}

function setAvatar(userAvatar, data) {
    if (data['avatar'] != null)
    userAvatar.src = data['avatar']
}

window.addEventListener('load', () => {
    fetch('/user/get_current_user/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            setAvatar(userAvatarBase, data)
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