// URL parameter
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
var q = d['q'];
console.log("q", q);

$( document ).ready(function() {
    console.log('document is ready.');
});

var json_path = "../../data/viewer.json";
var idols;
var groups;
$.getJSON(json_path, function(d) {
    idols = d['idols'];
    groups = d['groups'];
    console.log(json_path, 'loaded.')
});

// util
function zeroPadding(number, length){
    return (Array(length).join('0') + number).slice(-length);
}
function min_sec_str(second){
    var min = Math.floor(second / 60);
    var sec = second - min * 60;
    return zeroPadding(min, 2) + ':' + zeroPadding(sec, 2);
}

// JSON
var video_json_path = "../../json/" + q + ".json";
$.getJSON(video_json_path, function(obj) {
    console.log(video_json_path, 'loaded.')
    var total_frames = obj['total_frames'];
    var fps = obj['fps'];
    console.log('total_frames', total_frames);

    // each idol
    idol_num = 55;
    var $groups = $("#groups");
    var $template = $("#template div");
    var $container = $("#container-template");
    var containers = [];
    var group_num = 7;

    for(var i=0; i<group_num; i++){
        var cc = $container.clone();
        cc.attr('id', 'container-group-' + i.toString());
        cc.appendTo($groups);
        containers.push(cc);
        console.log('append');

        var group_name = groups[i];
        var gn = cc.find('.group-name');
        gn.text(group_name);
        gn.on('click', (function(){
            var nxt = gn.next();
            return function(){
                console.log('clicked');
                nxt.toggle();
            };
        })());
    }

    for(var i=0; i<idol_num; i++){
        var key = i.toString();
        frame_list = obj['idols'][key];
        if(frame_list.length == 0){
            continue;
        }
        var idol_name = idols[i][2];
        var group_id = idols[i][1];
        var tc = $template.clone();
        var ui_container = tc.find('div .ui-container').prevObject;
        var face = tc.find('.face-image');
        var icon_path = face.attr('src');
        var new_icon_path = icon_path.substring(0, icon_path.length - 8) + zeroPadding(i, 4) + '.jpg';
        face.attr('src', new_icon_path);

        // color
        var color = 'background-color:' + idols[i][4] + ';';
        ui_container.attr('style', color);

        // add face icons
        var span_face = tc.find('.span-face');
        for(var frame of frame_list.reverse()){
            var percentage = 100 * frame / total_frames;
            var sfc = span_face.clone();
            sfc.css('left', 'calc(' + percentage + '% - 16px)');

            var sec = Math.floor(frame / fps);

            // update pop up info
            var new_title = idols[i][2] + ' ' + min_sec_str(sec);
            sfc.find('img').prop('title', new_title);

            sfc.find('a').on('click', (function(){
                var current = sec;
                return function(){
                    console.log('a');
                    onClickFaceImage(current);
                }
            })());

            sfc.appendTo(ui_container);
        }
        span_face.remove();
        tc.appendTo(containers[group_id].find('.ui-bars'));
    }
    $container.remove();

    // delete template
    $template.remove();

    $(".face-image").balloon();
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
function onPlayerReady(event) {
    console.log('YT player is ready.');

    // set dummy space
    var header_height = $("#header").height();
    console.log('header H', header_height);
    var $space = $("#dummyspace"); ///////////////
    $space.height(header_height + height);
}
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
    if(player != null){
        player.seekTo(second);
    }
    console.log('seek to', second);
}