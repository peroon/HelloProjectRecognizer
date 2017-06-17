console.log('hello list');

var csv_path = "./data/videos.csv";
$.getJSON(csv_path, function(obj) {
   console.log('loaded');
});
