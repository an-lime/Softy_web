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
            setAvatar(userAvatarBase, data)
            const goProfileBtn = document.getElementById('go-profile-btn');
            goProfileBtn.href = (goProfileBtn.href.replaceAll('None', `${data['user_id']}`))
        }
    } catch (error) {
        alert('Произошла ошибка при загрузке. Попробуйте снова.');
    }
})