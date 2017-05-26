console.log("hello js");
var d = getUrlVars();
console.log(d['q']);

// on load
$(function() {
    console.log( "ready!" );

    var player = $("#ytplayer");
    var url = player.attr("src");
    var new_url = url.replace("YOUTUBE_ID", d['q']);
    console.log(new_url);
    player.attr("src", new_url)
});

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