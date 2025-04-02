const changeForm = document.getElementById('change-form')
let currentUserId;

window.addEventListener('load', async () => {
    const response = await fetch(`/user/api/users/current_user/`, {
        method: 'GET',
        headers: {
            'JS-Request': 'True',
        }
    });
    if (response.ok) {
        const data = await response.json();
        currentUserId = data['user_id']
        document.getElementById('first_name').value = data['first_name']
        document.getElementById('last_name').value = data['last_name']
    }
})

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

document.getElementById('avatar').addEventListener('change', (event) => {
    checkImage(event)
})

changeForm.addEventListener('submit', async function (event) {
    event.preventDefault();
    const formData = new FormData(changeForm);
    const avatar = document.getElementById('avatar');

    if (avatar.files.length === 0) {
        formData.delete('avatar');
    }

    try {
        const response = await fetch(`/user/api/users/${currentUserId}/`, {
            method: 'PATCH',
            headers: {
                'JS-Request': 'True',
            },
            body: formData
        });
        if (response.ok) {
            const data = await response.json();
            window.location.href = data['location']
        }

    } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
        alert('Произошла ошибка при изменении профиля. Попробуйте снова.');
    }
})