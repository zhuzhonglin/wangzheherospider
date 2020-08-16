# coding:utf-8
import json
import os
import requests
import useragentutil


def read_hero_info_file_from_json():
    """读取文件,获取数据"""
    # hero_file = open("./hero/hero.json", "r", encoding="utf-8")
    # hero_info_list = json.load(hero_file)
    # return hero_info_list
    with open('./hero/hero.json') as hero_file:
        hero_info_list = json.load(hero_file)
        return hero_info_list


def create_hero_image_save_dirs(datas):
    """创建存放英雄图片的目录  ./hero/pictures/名字"""
    for hero_element in datas:
        # 英雄名称
        dir_path_name = hero_element.get("hero_name")
        # print(dir_path_name)
        # 目录名
        dir = "./hero/pictures/" + dir_path_name
        # print(dir)
        # 目录不存在则创建
        if not os.path.exists(dir):
            os.makedirs(dir)
            print("目录[%s]已创建成功,谢谢.." % dir)
    print("所有存放英雄的目录信息已创建成功!!!")


def download_hero_pictures(datas):
    # ./hero/pictures/名字/1名字.jpg
    for hero_element in datas:
        # 英雄名称(与目录对应)
        file_name = hero_element["hero_name"]
        # 图片地址(下载图片)
        image_url = hero_element["hero_image_url"]
        # print("名称:%s,图片地址:%s"%(file_name,image_url))
        # 爬取图片的内容,再把内容写入到一个文件中,下载
        image_response = requests.get(image_url, headers=useragentutil.get_headers())
        # 图片内容
        image_content = image_response.content  # 二进制数据
        # 图片
        file = open("./hero/pictures/" + file_name + "/1" + file_name + ".jpg", "wb")
        file.write(image_content)
        # file.read()
        file.close()
        print("正在下载英雄图片(%s)...,请稍后!" % file_name)
    print("所有英雄图片已下载成功,谢谢!")


def main():
    # 读取文件,获取数据
    hero_info_datas = read_hero_info_file_from_json()
    # print(hero_info_datas)

    # 创建目录
    create_hero_image_save_dirs(hero_info_datas)

    # 下载图片
    download_hero_pictures(hero_info_datas)


if __name__ == '__main__':
    main()
