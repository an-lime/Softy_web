window.addEventListener("load", () => {

    document.title = "Профиль";
    fetch('/user/get_current_user/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            const first_name = document.getElementById('user_first_name')
            const last_name = document.getElementById('user_last_name')

            first_name.textContent = data['first_name']
            last_name.textContent = data['last_name']
        })
})