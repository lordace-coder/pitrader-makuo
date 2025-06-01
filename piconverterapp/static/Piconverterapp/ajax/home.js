// home javascript programs

// info program

"use strict"

// loader program

var load = document.getElementById('loader')

window.onload = function () {
    setTimeout(() => {
        load.style.display = 'none';
    }, 3000);
}

// menu program




var menu_btn = document.getElementById('menu-btn');
var menu_body = document.getElementById('menu-show');
var is_show = false

menu_btn.onclick = function () {
    if (is_show == false) {
        menu_body.style.display = 'flex'
        menu_body.style.scale = '1'
        menu_btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">' +
  '<path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>' +
'</svg>'
        is_show = true
    }else{
        menu_body.style.display = 'none'
        menu_body.style.scale = '0.8'
        menu_btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-filter-left" viewBox="0 0 16 16">' +
                '<path d="M2 10.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5m0-3a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7a.5.5 0 0 1-.5-.5m0-3a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-11a.5.5 0 0 1-.5-.5"/>' + '</svg>'
        is_show = false
    }
}
window.onresize = function () {
    menu_body.style.display = 'none'
    menu_body.style.scale = '0.8'
    is_show = false
}

// observer program

var nav = document.getElementById('navagation');
var sect2 = document.getElementById('sect2');

const observer = new IntersectionObserver(
    callbackfunction,
    option,
)

function callbackfunction(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            nav.style.backgroundColor = 'rgb(109, 74, 180)';
        }
        else{
            nav.style.backgroundColor = 'transparent'
        }
    });
}

var option = {
    rootMargin: "0px",
    threshold: 0.2,
}

observer.observe(sect2);

// text observer program

var text = document.getElementsByClassName('authshow');
var sev = document.getElementsByClassName('serv');

var observer2 = new IntersectionObserver(
    callbackfunction2,
    option2,
)

function callbackfunction2(entre) {
    entre.forEach (ent => {
        if (ent.isIntersecting) {
            sev[0].style.scale = '1'
            sev[0].style.opacity = '1';

            sev[1].style.scale = '1'
            sev[1].style.opacity = '1';

            sev[2].style.scale = '1'
            sev[2].style.opacity = '1' ;
        }
    })
    
        
}

var option2 = {
    rootMargin: " 0px ",
    threshold: 1,
}

observer2.observe(sev[0]);
observer2.observe(sev[1]);
observer2.observe(sev[2]);

