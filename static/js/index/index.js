const now = new Date();
const day = String(now.getDate()).padStart(2, '0');
const month = String(now.getMonth() + 1).padStart(2, '0');
const year = now.getFullYear();
const hours = String(now.getHours()).padStart(2, '0');
const minutes = String(now.getMinutes()).padStart(2, '0');
const seconds = String(now.getSeconds()).padStart(2, '0');

let lastDateTime = `${day}-${month}-${year} ${hours}:${minutes}:${seconds}`;
let loading = false;

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
    postElement.id = `post_in_news_feed_${post['id']}_${post['author_ref']}`
    postElement.className = 'post_in_news_feed';
    postElement.innerHTML = `
                            <div id="container-text" class="container-text">
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

    // кнопка удаления, если пользователь - автор поста
    if (post['is_author'] === true) {
        postElement.insertAdjacentHTML("afterbegin", `<div id="services-btn-parent">
                                                                        <div id="services-btn">
                                                                            <label id="delete-post-btn">Удалить</label>
                                                                        </div>   
                                                                    </div>`
        )
    }
    return postElement
}

window.addEventListener("DOMContentLoaded", async () => {
    document.title = "Главная";
    loadPosts()
})

window.addEventListener('scroll', onScroll);