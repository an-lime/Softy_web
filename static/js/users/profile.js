const userAvatarProfile = document.getElementById('img-profile-menu')

window.addEventListener("load", () => {

    document.title = "Профиль";
    fetch('/user/get_current_user/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('user_first_name').textContent = data['first_name']
            document.getElementById('user_last_name').textContent = data['last_name']
            setAvatar(userAvatarProfile, data)
        })
})