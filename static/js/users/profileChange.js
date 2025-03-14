window.addEventListener("load", () => {
    fetch('/user/get_current_user/', {
        method: 'GET',
        headers: {
            'JS-Request': 'True',
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log(123)
            document.getElementById('first_name').value = data['first_name']
            document.getElementById('last_name').value = data['last_name']
        })
})

document.getElementById('avatar').addEventListener('change', (event) => {
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
})