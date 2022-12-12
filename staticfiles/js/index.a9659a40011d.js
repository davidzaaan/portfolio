const switchTheme = document.querySelector("#theme-toggler");

switchTheme.addEventListener("click", (event) => {
    document.body.classList.toggle("dark-mode");

    if (event.target.innerText === "Dark") {
        event.target.innerText = "Light";
    } else {
        event.target.innerText = "Dark";
    }

});