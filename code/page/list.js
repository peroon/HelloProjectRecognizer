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
    console.log(videos[0]);
    console.log(videos[1]);
}