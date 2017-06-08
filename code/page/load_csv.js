function getCSV(){
    var req = new XMLHttpRequest();
    req.open("get", "../../../data/csv/idols.csv", true);
    req.send(null);

    req.onload = function(){
    	convertCSVtoArray(req.responseText);
    }
}

var idol_data = [];
function convertCSVtoArray(str){
    var tmp = str.split("\n");
    tmp = tmp.slice(1);

    for(var i=0;i<tmp.length;++i){
        if(tmp[i] == ''){
            continue;
        }
        console.log(tmp[i]);
        idol_data[i] = tmp[i].split(',');
    }
}

function get_idol_name(idol_id){
    return idol_data[idol_id][2];
}

getCSV();