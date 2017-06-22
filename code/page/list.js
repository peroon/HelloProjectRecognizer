var csv_path = "./data/videos.csv";
var req = new XMLHttpRequest();
req.open("get", csv_path, true);
req.send(null);
req.onload = function(){
    loadCSV(req.responseText);
}

var videos = [];
function loadCSV(str){
    var tmp = str.split("\n");
    tmp = tmp.slice(1);

    for(var i=0;i<tmp.length;++i){
        if(tmp[i] == ''){
            continue;
        }
        videos[i] = tmp[i].split(',');
    }

    onCompleteLoad();
}

function onCompleteLoad(){
    var ul = $('#movie_list');
    var li = $('.li_template');

    console.log(ul);
    console.log(li);

    for(var video of videos){
        console.log('generate', video);
        var youtube_id = video[0];

        var json_path = '../../resources/json/' + youtube_id + '.json';
        console.log(json_path);

        var clone = li.clone();
        var thumbnail_url = "https://i.ytimg.com/vi/" + youtube_id + "/hqdefault.jpg"
        clone.find('.movie_thumbnail').attr('src', thumbnail_url);
        var movie_url = "./viewer.html?q=" + youtube_id;
        clone.find('.movie_url').attr('href', movie_url);


        clone.appendTo(ul);
    }

    li.remove();
}