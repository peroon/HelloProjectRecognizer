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
var d = getUrlVars();
console.log("q=" + d['q']);

$( document ).ready(function() {
    $(".face-image").balloon();
    $('#sample1 a').balloon();
});

// util
function zeroPadding(number, length){
    return (Array(length).join('0') + number).slice(-length);
}

// JSON
//var json_path = "../../resources/json/N0c-jH-r_lo.json";
var json_path = "../../resources/json/testbed.json";
console.log("json");
$.getJSON(json_path, function(obj) {
    var total_frames = obj['total_frames'];
    console.log(total_frames);

    // each idol
    idol_num = 3;
    var template = $("#template div");
    var container = $("#container");
    for(var i=0; i<idol_num; i++){
        var key = i.toString();
        frame_list = obj[key];
        var idol_name = idol_data[i+1][2];
        console.log('Add UI bar for ' + idol_name);

        var tc = template.clone();
        var ui_container = tc.find('div .ui-container').prevObject;
        console.log(ui_container);
        var face = tc.find('.face-image');
        var icon_path = face.attr('src');
        var new_icon_path = icon_path.substring(0, icon_path.length - 8) + zeroPadding(i, 4) + '.jpg';
        face.attr('src', new_icon_path);

        // add face icons
        var span_face = tc.find('.span-face');
        var lst = obj[i.toString()];
        for(var frame of lst){
            console.log(i, frame);
            var percentage = 100 * frame / total_frames;
            var sfc = span_face.clone();
            sfc.css('left', 'calc(' + percentage + '% - 16px)');
            sfc.appendTo(ui_container);
        }
        tc.appendTo(container);
    }

    // delete template
    template.remove();
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