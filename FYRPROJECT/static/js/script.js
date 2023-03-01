let menu = document.getElementById('menu-btn')
let navlinks = document.getElementById('nav-links')


menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navlinks.classList.toggle('active');
}

window.onscroll = () =>{
    menu.classList.remove('fa-times')
    navlinks.classList.remove('active')
}



