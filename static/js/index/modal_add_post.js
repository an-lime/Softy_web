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

// валидация изображения
document.getElementById('add-post-img').addEventListener('change', (event) => {
    checkImage(event)
})

// Добавление нового поста
addPostBtn.addEventListener('click', async function (e) {

    e.preventDefault()
    let postContent = document.getElementById('post_text');
    if (postContent.value.trim() !== '') {

        const formData = new FormData()
        formData.append('post_text', postContent.value);
        const fileInput = document.getElementById('add-post-img');
        if (fileInput.files.length > 0) {
            formData.append('post_image', fileInput.files[0]);
        }

        const response = await fetch(`/api/posts/`, {
            method: 'POST',
            headers: {
                'JS-Request': 'True',
            },
            body: formData,
        });
        if (response.ok) {
            const data = await response.json()
            const postsContainer = document.getElementById('right-column-content')
            postsContainer.insertAdjacentElement("afterbegin", createHtmlPost(data))
            addMoreButton(1)
        }

        postContent.value = ''
        fileInput.value = null
        modal.style.display = 'none';

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