const leftColumnContent = document.getElementById('left-column-content')
const left_column_content_a = document.getElementById("left-column-content-a")
const btnExit = document.getElementById("btn-exit")

if (btnExit != null) {
    btnExit.addEventListener("click", () => {
        localStorage.clear();
    })
}

document.addEventListener("DOMContentLoaded", () => {
    fetch('/get_current_user/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            if (btnExit != null) {
                if (data['is_authenticated']) {
                    left_column_content_a.style.display = 'flex'
                } else {
                    left_column_content_a.style.display = 'none'
                }
            }
        })
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}