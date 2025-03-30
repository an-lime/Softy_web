let loading = false;

function getCurrentDateTime() {
    const now = new Date();
    const day = String(now.getDate()).padStart(2, '0');
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const year = now.getFullYear();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    return `${day}-${month}-${year} ${hours}:${minutes}:${seconds}`
}

let lastDateTime = getCurrentDateTime();

function loadPosts() {
    if (loading) return;
    loading = true;

    fetch(`/api/posts/?lastDateTime=${lastDateTime}`, {
        method: 'GET',
        headers: {
            'JS-Request': 'True',
            'Content-Type': 'application/json',
        }
    })
        .then(response => response.json())
        .then(data => {
            const postsContainer = document.getElementById('right-column-content')
            data['posts'].forEach(post => {
                postsContainer.appendChild(createHtmlPost(post));
                addMoreButton()
                lastDateTime = post['post_date']
            });
            loading = false;

        })
}

function onScroll() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
        loadPosts()
    }
}

function addMoreButton(isFirst = 0) {
    const wrapperContainer = document.querySelectorAll('.post_in_news_feed');
    let lastPost;
    if (isFirst === 1) {
        lastPost = wrapperContainer[0]
    } else {
        lastPost = wrapperContainer[wrapperContainer.length - 1]
    }
    const container = lastPost.querySelector('.middle-container-text');
    const moreButton = lastPost.querySelector('.more-button');
    const textContent = lastPost.querySelector('.post-text');

    function isOverflowing() {
        return textContent.scrollHeight > container.clientHeight;
    }

    function toggleText() {
        container.classList.toggle('expanded');
        lastPost.classList.toggle('expanded');
        moreButton.textContent = container.classList.contains('expanded') ? 'Свернуть' : 'Показать полностью';
    }

    if (isOverflowing()) {
        moreButton.style.display = 'flex';
    } else {
        moreButton.style.display = 'none';
    }
    moreButton.addEventListener('click', toggleText);
}

function createHtmlPost(post) {

    const postElement = document.createElement('div');
    postElement.id = `post_in_news_feed_${post['id']}`
    postElement.className = 'post_in_news_feed';
    postElement.innerHTML = `
                            <div class="container-text">
                                <div class="middle-container-text">
                                    <div style="word-break: break-all" class="post-text">${post['post_text']}</div>
                                </div>
                                <div class="more-button-div">
                                    <div class="more-button" style="display: none">Показать полностью</div>
                                </div>
                            </div>`

    if (post['post_image']) {
        postElement.insertAdjacentHTML('afterbegin', `<div class="post-img-div">
                                                                        <img class="post-img" alt="post-img" src="${post['post_image']}">
                                                                    </div>`)
    } else {
        post['post_image'] = ""
    }

    const servicesBtnParent = document.createElement('div');
    servicesBtnParent.className = 'services-btn-parent'

    const divAuthor = document.createElement('div');
    divAuthor.className = 'div-author'
    servicesBtnParent.insertAdjacentElement('afterbegin', divAuthor)

    const goAuthorProfile = document.createElement('a');
    goAuthorProfile.className = 'go-author-profile';
    goAuthorProfile.href = `/user/profile/${post['author']['id']}`
    goAuthorProfile.text = `${post['author']['first_name'] + ' ' + post['author']['last_name']}`;
    divAuthor.appendChild(goAuthorProfile)

    postElement.insertAdjacentElement("afterbegin", servicesBtnParent)

    // кнопка удаления, если пользователь - автор поста
    if (post['is_author'] === true) {
        const divServicesBtn = document.createElement('div');
        divServicesBtn.id = 'services-btn';

        const deletePostBtn = document.createElement('label');
        deletePostBtn.id = 'delete-post-btn';
        deletePostBtn.textContent = 'Удалить';

        deletePostBtn.addEventListener('click', async function ()  {
            const response = await fetch(`/api/posts/${post['id']}/`, {
                method: 'DELETE',
                headers: {
                    'JS-Request': 'True',
                }
            });
            if (response.ok) {
                postElement.remove();
            } else {
                alert('Ошибка удаления');
            }
        })

        divServicesBtn.insertAdjacentElement('afterbegin', deletePostBtn);

        divAuthor.insertAdjacentElement('afterend', divServicesBtn)
    }

    return postElement
}

window.addEventListener("DOMContentLoaded", async () => {
    document.title = "Главная";
    loadPosts()
})

window.addEventListener('scroll', onScroll);