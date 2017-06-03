// URL paramter
function getUrlVars(){
    var vars = [], max = 0, hash = "", array = "";
    var url = window.location.search;
    hash  = url.slice(1).split('&');
    max = hash.length;
    for (var i = 0; i < max; i++) {
        array = hash[i].split('=');
        vars.push(array[0]);
        vars[array[0]] = array[1];
    }
    return vars;
}
console.log("hello jss");
var d = getUrlVars();
console.log(d['q']);

$( document ).ready(function() {
    $(".face-image").balloon();
    $('#sample1 a').balloon();
});

// JSON
var json_path = "../../resources/json/N0c-jH-r_lo.json";
console.log("json");
$.getJSON(json_path, function(obj) {
    Object.keys(obj).forEach(function (key) {
        console.log(obj[key]);
    });
});

// Youtube
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
var player;
var width = $(window).width();
var height = width * (390 / 640);
function onYouTubeIframeAPIReady() {
player = new YT.Player('player', {
  height: height.toString(),
  width: width.toString(),
  videoId: d['q'],
  events: {
    'onReady': onPlayerReady,
    'onStateChange': onPlayerStateChange
  }
});
}
function onPlayerReady(event) {}
var done = false;
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
        setTimeout(stopVideo, 6000);
        done = true;
    }
}
function stopVideo() {
    player.stopVideo();
}


function onClickFaceImage(second){
    console.log(second);
    player.seekTo(second);
}