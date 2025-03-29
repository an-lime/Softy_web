const btnExit = document.getElementById("btn-exit")
const userAvatarBase = document.getElementById('user_avatar');

if (btnExit != null) {
    btnExit.addEventListener("click", () => {
        localStorage.clear();
    })
}

function setAvatar(userAvatar, data) {
    userAvatar.src = data['avatar']
}

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

window.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch(`/user/api/users/current_user/`, {
            method: 'GET',
            headers: {
                'JS-Request': 'True',
            }
        });
        if (response.ok) {
            const data = await response.json()
            if (data['is_authenticated'] === true) {
                setAvatar(userAvatarBase, data)

                // создание кнопки перехода на страницу профиля
                const goProfileBtn = document.createElement('a');
                goProfileBtn.id = 'go-profile-btn';
                goProfileBtn.href = `/user/profile/${data['user_id']}`
                goProfileBtn.text = 'Профиль'
                userAvatarBase.insertAdjacentElement('afterend', goProfileBtn);
            }
        }
    } catch (error) {
        alert('Произошла ошибка при загрузке. Попробуйте снова.');
    }
})