# -*- coding: utf-8 -*-

import os

from idol import Idol


def get_cute_list():
    cute_list = []
    group_name = 'C-ute'
    cute_list.append(Idol('矢島舞美', 'maimi-yajima', group_name))
    cute_list.append(Idol('中島早貴', 'saki-nakajima', group_name))
    cute_list.append(Idol('鈴木愛理', 'airi-suzuki', group_name))
    cute_list.append(Idol('岡井千聖', 'chisato-okai', group_name))
    cute_list.append(Idol('萩原舞', 'mai-hagiwara', group_name))
    return cute_list


def get_musume_list():
    musume_list = []
    group_name = 'musume'
    musume_list.append(Idol('譜久村聖', 'mizuki-fukumura', group_name))
    musume_list.append(Idol('生田衣梨奈', 'erina-ikuta', group_name))
    musume_list.append(Idol('飯窪春菜', 'haruna-iikubo', group_name))
    musume_list.append(Idol('石田亜佑美', 'ayumi-ishida', group_name))
    musume_list.append(Idol('佐藤優樹', 'masaki-sato', group_name))
    musume_list.append(Idol('工藤遥', 'haruka-kudo', group_name))
    musume_list.append(Idol('小田さくら', 'sakura-oda', group_name))
    musume_list.append(Idol('尾形春水', 'haruna-ogata', group_name))
    musume_list.append(Idol('野中美希', 'miki-nonaka', group_name))
    musume_list.append(Idol('牧野真莉愛', 'maria-makino', group_name))
    musume_list.append(Idol('羽賀朱音', 'akane-haga', group_name))
    musume_list.append(Idol('加賀楓', 'kaede-kaga', group_name))
    musume_list.append(Idol('横山玲奈', 'reina-yokoyama', group_name))
    return musume_list


def get_angerme_list():
    idol_list = []
    group_name = 'angerme'
    idol_list.append(Idol('和田彩花', 'ayaka-wada', group_name))
    idol_list.append(Idol('中西香菜', 'kana-nakanishi', group_name))
    idol_list.append(Idol('竹内朱莉', 'akari-takeuchi', group_name))
    idol_list.append(Idol('勝田里奈', 'rina-katsuta', group_name))
    idol_list.append(Idol('室田瑞希', 'muzuki-murota', group_name))
    idol_list.append(Idol('相川茉穂', 'maho-aikawa', group_name))
    idol_list.append(Idol('佐々木莉佳子', 'rikako-sasaki', group_name))
    idol_list.append(Idol('上國料萌衣', 'moe-kamikokuryo', group_name))
    idol_list.append(Idol('笠原桃奈', 'momona-kasahara', group_name))
    return idol_list


def get_juice_list():
    idol_list = []
    group_name = 'juice=juice'
    idol_list.append(Idol('宮崎由加', 'yuka-miyazaki', group_name))
    idol_list.append(Idol('金澤朋子', 'tomoko-kanazawa', group_name))
    idol_list.append(Idol('高木紗友希', 'sayuki-takagi', group_name))
    idol_list.append(Idol('宮本佳林', 'karin-miyamoto', group_name))
    idol_list.append(Idol('植村あかり', 'akari-uemura', group_name))
    return idol_list


def get_country_list():
    idol_list = []
    group_name = 'country'
    idol_list.append(Idol('嗣永桃子', 'momoko-tsugunaga', group_name))
    idol_list.append(Idol('山木梨沙', 'risa-yamaki', group_name))
    idol_list.append(Idol('森戸知沙希', 'chisaki-morito', group_name))
    idol_list.append(Idol('小関舞', 'mai-ozeki', group_name))
    idol_list.append(Idol('梁川奈々美', 'nanami-yanagawa', group_name))
    idol_list.append(Idol('船木結', 'yui-funaki', group_name))
    return idol_list


def get_kobushi_list():
    idol_list = []
    group_name = 'kobushi'
    idol_list.append(Idol('藤井梨央', 'rio-fujii', group_name))
    idol_list.append(Idol('広瀬彩海', 'ayaka-hirose', group_name))
    idol_list.append(Idol('野村みな美', 'minami-nomura', group_name))
    idol_list.append(Idol('小川麗奈', 'rena-ogawa', group_name))
    idol_list.append(Idol('浜浦彩乃', 'ayano-hamaura', group_name))
    idol_list.append(Idol('田口夏実', 'natsumi-taguchi', group_name))
    idol_list.append(Idol('和田桜子', 'sakurako-wada', group_name))
    idol_list.append(Idol('井上玲音', 'rei-inoue', group_name))
    return idol_list


def get_tsubaki_list():
    idol_list = []
    group_name = 'tsubaki'
    idol_list.append(Idol('山岸理子', 'riko-yamagishi', group_name))
    idol_list.append(Idol('小片リサ', 'risa-ogata', group_name))
    idol_list.append(Idol('新沼希空', 'kisora-niinuma', group_name))
    idol_list.append(Idol('谷本安美', 'ami-tanimoto', group_name))
    idol_list.append(Idol('岸本ゆめの', 'yumeno-kishimoto', group_name))
    idol_list.append(Idol('浅倉樹々', 'kiki-asakura', group_name))
    idol_list.append(Idol('小野瑞歩', 'mizuho-ono', group_name))
    idol_list.append(Idol('小野田紗栞', 'saori-onoda', group_name))
    idol_list.append(Idol('秋山眞緒', 'mao-akiyama', group_name))
    return idol_list


def get_idol_all_list():
    return get_cute_list() + get_musume_list() + get_angerme_list() + get_juice_list() + get_country_list() + get_kobushi_list() + get_tsubaki_list()


def __make_directory():
    idol_list = get_idol_all_list()
    idol_list = idol_list[2:]
    for idol in idol_list:
        dir_path = '../resources/face/' + idol.directory_name
        os.mkdir(dir_path)
        dir_path = '../resources/search/' + idol.directory_name
        os.mkdir(dir_path)


if __name__ == '__main__':
    #__make_directory()
    pass
