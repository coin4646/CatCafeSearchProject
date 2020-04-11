const titlePart = document.querySelector(".title-wrap");

    
function callRanNum() {
    ranNum = Math.floor((Math.random()*7)+1);
    return ranNum;
}

function loadPhoto() {
    ranNum = callRanNum();
    url = `../background-image/${ranNum}.jpg`
    titlePart.style.backgroundImage = `url(${url})`;
}

function init() {
    loadPhoto();
}   

init();