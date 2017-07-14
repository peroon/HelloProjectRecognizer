var json_path = "../../data/list.json";
$.getJSON(json_path, function(d) {
    var videos = d['video_list'];
    drawVideos(videos);
});

function drawVideos(videos){
    var ul = $('#movie_list');
    var li = $('.li_template');

    console.log(ul);
    console.log(li);

    for(let[index, video] of videos.entries()){
        console.log('generate', video);
        var youtube_id = video['youtube_id'];
        var clone = li.clone();

        if(index % 2 == 1){
            clone.addClass('gray-bg');
        }


        // thumbnail
        var thumbnail_url = "https://i.ytimg.com/vi/" + youtube_id + "/mqdefault.jpg"
        clone.find('.movie_thumbnail').attr('src', thumbnail_url);
        var movie_url = "../viewer/viewer.html?q=" + youtube_id;
        clone.find('.movie_url').attr('href', movie_url);

        // title
        clone.find('.movie_title').text(video['title']);

        // ranking
        var ranking_ul = clone.find('.idol_ranking');
        var ranking_data = video['ranking'];
        ranking_ul.empty();
        for(var i=0; i<3; i++){
            var name = ranking_data[i]['name'];
            var ratio = ranking_data[i]['ratio'];
            var percentage = (ratio * 100.0).toFixed(1);
            var text = name + ' ' + percentage + "%";
            ranking_ul.append('<li>' + text + '</li>');
        }

        clone.appendTo(ul);
    }

    li.remove();
}