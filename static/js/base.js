const btnExit = document.getElementById("btn-exit")

if (btnExit != null) {
    btnExit.addEventListener("click", () => {
        localStorage.clear();
    })
}

const leftColumnContent = document.getElementById("left-column-content")
if (currentUserIsAuthenticated === "True") {
    leftColumnContent.insertAdjacentHTML("afterbegin", "<div class=\"profile-div\">\n" +
        "                <img src=\"https://kamtk.ru:9096/el-zurnal/el-dnevnik/Css/image1/profile.png\" alt=\"profile_image\"\n" +
        "                     class=\"img_profile\">\n" +
        "                <a href=\"#\">Профиль</a>\n" +
        "            </div>")
}
else {
    leftColumnContent.insertAdjacentHTML("afterbegin", "            <div class=\"profile-div\">\n" +
        "                <a href=\"#\" id=\"login-a\">Авторизация</a>\n" +
        "                <a href=\"#\" id=\"register-a\">Регистрация</a>\n" +
        "            </div>")
}

function toggleBtnExit() {
    if (currentUserIsAuthenticated === "True") {
        btnExit.style.display = 'block'
    } else {
        btnExit.style.display = 'none'
    }
}

window.onload = toggleBtnExit