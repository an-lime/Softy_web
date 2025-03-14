const openModalBtn = document.getElementById('openModalAddPostBtn');
const modal = document.getElementById('modal');
const closeModalBtn = document.querySelector('.close');
const addPostBtn = document.getElementById('addPostBtn');

openModalBtn.addEventListener('click', () => {
    modal.style.display = "block";
})

closeModalBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Добавление нового поста
addPostBtn.addEventListener('click', function (e) {

    e.preventDefault()
    const postContent = document.getElementById('post_text').value;
    if (postContent.trim() !== '') {

        const formData = new FormData()
        formData.append('post_text', postContent);
        const fileInput = document.getElementById('add-post-img');
        if (fileInput.files.length > 0) {
            formData.append('post_image', fileInput.files[0]);
        }

        fetch('/user/get_current_user/', {
            method: 'GET',
            headers: {
                'JS-Request': 'True',
                'Content-Type': 'application/json'
            }
        })
            .then(response => response.json())
            .then(data => {

                formData.append('user', data['user_id']);

                fetch('/add-new-post/', {
                    method: 'POST',
                    body: formData,
                })
                    .then(response => response.json())
            })

    } else {
        const divError = document.getElementById('div-post-error');
        if (!divError) {
            addPostBtn.parentElement.insertAdjacentHTML("afterend",
                "<div id='div-post-error'>* Текст обязательно должен быть заполнен!</div>");
        }
    }
});

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});