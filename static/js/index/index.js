window.addEventListener("load", () => {
    document.title = "Главная"
})

let page = 1;
let loading = false;

function loadPosts() {
    if (loading) return;
    loading = true;
    fetch(`/get-posts/?page=${page}`, {
        method: 'GET',
        headers: {
            'JS-Request': 'True'
        }
    })
        .then(response => response.json())
        .then(data => {
            const postsContainer = document.getElementById('right-column-content')
            data['posts'].forEach(post => {
                const postElement = document.createElement('div');
                postElement.className = 'post_in_news_feed';

                postElement.innerHTML = ` <div class="post-img-div">
                                            <img class="post-img" src="${post['post_image']}" alt="">
                                        </div>
                                        <div class="container-text">
                                            <div class="middle-container-text">
                                                <div style="word-break: break-all" class="post-text">${post['post_text']}</div>
                                            </div>
                                            <div class="more-button-div">
                                                <div class="more-button" style="display: none">Показать полностью</div>
                                            </div>
                                        </div> `
                postsContainer.appendChild(postElement);
            });

            const wrapperContainer = document.querySelectorAll('.post_in_news_feed');
            wrapperContainer.forEach(wrapper => {
                const container = wrapper.querySelector('.middle-container-text');
                const moreButton = wrapper.querySelector('.more-button');
                const textContent = wrapper.querySelector('.post-text');

                function isOverflowing() {
                    return textContent.scrollHeight > container.clientHeight;
                }

                function toggleText() {
                    container.classList.toggle('expanded');
                    wrapper.classList.toggle('expanded');
                    moreButton.textContent = container.classList.contains('expanded') ? 'Свернуть' : 'Показать полностью';
                }

                if (isOverflowing()) {
                    moreButton.style.display = 'flex';
                } else {
                    moreButton.style.display = 'none';
                }
                moreButton.addEventListener('click', toggleText);
            })

            if (data['has_next']) {
                page++;
            } else {
                window.removeEventListener('scroll', onScroll)
            }
            loading = false;
        })
}

function onScroll() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 100) {
        loadPosts()
    }
}

window.addEventListener('scroll', onScroll);
loadPosts()