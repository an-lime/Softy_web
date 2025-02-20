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