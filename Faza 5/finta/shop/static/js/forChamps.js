//Slavko Krstic 2019/0028

let seconds = 0;
let handler = null;
let timeBetween = 1800;

function tick(){
    seconds--;

    h = Math.floor(seconds / 3600);
    m = Math.floor((seconds - h * 3600) / 60);
    s = seconds % 60;

    if(h < 10){
        h = "0" + h;
    }

    if(m < 10){
        m = "0" + m;
    }

    if(s < 10){
        s = "0" + s;
    }


    $("#time").text(h + ":" + m + ":" + s);
    if(seconds == 0) {
        clearInterval(handler);
    }
}

function startTimer(param){
    seconds = timeBetween - param;
    handler = setInterval(tick, 1000);
}

$(document).ready(function (){

})