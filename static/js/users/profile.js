const userAvatarProfile = document.getElementById('img-profile-menu')
const divInfoProfile = document.getElementById('div-info')

window.addEventListener("load", async () => {

    document.title = "Профиль";

    const pathParts = window.location.pathname.split('/');
    const userIdInPath = pathParts[pathParts.length - 2]

    try {
        const response = await fetch(`/user/api/users/${userIdInPath}/`, {
            method: 'GET',
            headers: {
                'JS-Request': 'True',
            }
        });
        if (response.ok) {
            console.log(response)
            const data = await response.json()
            document.getElementById('user_first_name').textContent = data['first_name']
            document.getElementById('user_last_name').textContent = data['last_name']
            setAvatar(userAvatarProfile, data)
        } else {
            console.log(response)
            alert('Страницы не существует')
        }
    } catch (error) {
        alert('Произошла ошибка при загрузке. Попробуйте снова.');
    }

    try {
        const response = await fetch(`/user/api/users/current_user/`, {
            method: 'GET',
            headers: {
                'JS-Request': 'True',
            }
        });
        if (response.ok) {
            const data = await response.json()

            if (parseInt(userIdInPath) === data['user_id']) {
                const goChangeProfileBtn = document.createElement('a');
                goChangeProfileBtn.id = 'go-change-profile-btn';
                goChangeProfileBtn.className = 'change-profile-btn'
                goChangeProfileBtn.href = '/user/profile/change/'
                goChangeProfileBtn.text = 'Изменить профиль'
                divInfoProfile.insertAdjacentElement('afterend', goChangeProfileBtn)

                setAvatar(userAvatarBase, data)
            }
        }
    } catch (error) {
        console.log(error)
        alert('Произошла ошибка при загрузке. Попробуйте снова.');
    }
})