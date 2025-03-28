const userAvatarProfile = document.getElementById('img-profile-menu')

window.addEventListener("load", async () => {

    document.title = "Профиль";

    const pathParts = window.location.pathname.split('/');
    const userId = pathParts[pathParts.length - 2]

    try {
        const response = await fetch(`/user/api/users/${userId}`, {
            method: 'GET',
            headers: {
                'JS-Request': 'True',
            }
        });
        if (response.ok) {
            const data = await response.json()
            document.getElementById('user_first_name').textContent = data['first_name']
            document.getElementById('user_last_name').textContent = data['last_name']
            setAvatar(userAvatarProfile, data)
            setAvatar(userAvatarBase, data)
        }
    } catch (error) {
        alert('Произошла ошибка при загрузке. Попробуйте снова.');
    }
})