# Collect idol face images from Youtube

## Youtube API

* API_KEYを発行する。APIを有効にするボタンを押す
* GETで正しくURLを入れる。ブラウザで十分
* プレイリストIDから全動画URLが取りたかったので、
* GET用URL例
	* https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PL1U0DlJ2bZPQi-dQsg4nAAKs57oHpXFsv&maxResults=50&key=XXXX
* JSON内の、items/resourceId/videoIdに_4nww-s_q_cなどと書かれているので、再生URLはyoutube.com/watch?v=_4nww-s_q_cとなる
* 50件ずつしか取れないので、nextPageTokenを使う。1ページ目取得時にJSON内に書かれている
* 2ページ目をGETするURLは、pageTokenを指定する。例は、
	* https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PL1U0DlJ2bZPQi-dQsg4nAAKs57oHpXFsv&maxResults=50&key=XXXX&pageToken=CDIQAA
* TODO
	* Python一発で200件のリストが生成されるようにする


## Download from Youtube

* https://github.com/NFicano/pytube
* mp4 720pで落とすと、1時間ほどなのでファイルサイズは1GB
* 200本ある
* JPGにすると500KB
* 5秒ごとの静止画にすると60 * 60 / 5 = 720枚 → 360MB
* 手間が増える割にはサイズは小さくならないので、静止画ではなく、動画で管理する

## Appropriate video size

* If 720p is specified, 1280x720 video can be acquired and it is sufficient.