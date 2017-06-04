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

    for(var i=0;i<tmp.length;++i){
        idol_data[i] = tmp[i].split(',');
    }

    console.log(idol_data[1][2]);
}

getCSV();