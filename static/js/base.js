const left_column_content_a = document.getElementById("left-column-content-a")
const btnExit = document.getElementById("btn-exit")

if (btnExit != null) {
    btnExit.addEventListener("click", () => {
        localStorage.clear();
    })
}

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