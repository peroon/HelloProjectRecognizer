var json_path = "./data/list.json";
$.getJSON(json_path, function(d) {
    var videos = d['video_list'];
    drawVideos(videos);
});

function drawVideos(videos){
    var ul = $('#movie_list');
    var li = $('.li_template');

    console.log(ul);
    console.log(li);

    for(var video of videos){
        console.log('generate', video);
        var youtube_id = video['youtube_id'];
        var clone = li.clone();

        // thumbnail
        var thumbnail_url = "https://i.ytimg.com/vi/" + youtube_id + "/mqdefault.jpg"
        clone.find('.movie_thumbnail').attr('src', thumbnail_url);
        var movie_url = "./viewer.html?q=" + youtube_id;
        clone.find('.movie_url').attr('href', movie_url);

        // title
        clone.find('.movie_title').text(video['title']);

        // ranking
        clone.find('.idol_ranking').text('aa<br>bb');

        clone.appendTo(ul);
    }

    li.remove();
}