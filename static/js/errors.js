window.addEventListener('load', () => {
        const message = document.getElementById('message');
        if (message) {
            message.classList.add('show');
            setTimeout(() => {
                message.classList.add('hidden');
            }, 1700);
            setTimeout(() => {
                message.style.position = 'fixed';
            }, 2300)
        }
    }
);