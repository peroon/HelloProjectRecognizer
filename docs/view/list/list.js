var page = 1
var video_num_per_page = 2;
var totalPage = 10;
var videos;
var json_path = "../../data/list.json";
$.getJSON(json_path, function(d) {
    videos = d['video_list'];
    drawVideos();
});

function drawVideos(){
    var ul = $('#movie_list');
    var li = $('.li_template');

    console.log(ul);
    console.log(li);

    var p = page - 1;
    var videos_subset = videos.slice(p * video_num_per_page, (p+1) * video_num_per_page);

    for(let[index, video] of videos_subset.entries()){
        console.log('generate', video);
        var youtube_id = video['youtube_id'];
        var clone = li.clone();

        if(index % 3 == 0){
            clone.addClass('bg-color-0');
        }else if(index % 3 == 1){
            clone.addClass('bg-color-1');
        }else{
            clone.addClass('bg-color-2');
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

function onClickNext(){
    console.log('onClickNext');
    page += 1;
    if(page > totalPage){
        console.log('over');
        page = totalPage;
    }else{
        drawVideos();
        updatePage();
    }
}

function onClickPrev(){
    page -= 1;
    if(page < 1){
        console.log('over');
        page = 1;
    }else{
        drawVideos();
        updatePage();
    }
}

function updatePage(){
    var pageText = page.toString() + '/' + totalPage.toString();
    $('.page-ui').text(pageText);
}