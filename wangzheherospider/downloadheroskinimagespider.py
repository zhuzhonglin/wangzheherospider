# coding:utf-8
import json
import requests
import useragentutil


def read_hero_skin_file_from_json():
    """文件，获取数据信息"""  # Shift+F6
    skin_file = open("./hero/heroskin.json", "r", encoding="utf-8")
    hero_result = json.load(skin_file)
    # print(hero_result)
    return hero_result


def main():
    # （1）读取英雄皮肤文件，获取数据信息；
    hero_skin_datas = read_hero_skin_file_from_json()
    # print(hero_skin_datas)
    # （2）遍历获取单个的英雄信息，提取名称、皮肤列表；
    i = 0
    while i < len(hero_skin_datas):
        # 单个英雄
        hero = hero_skin_datas[i]
        # print("第%d个英雄:"%i,hero)
        # 英雄名称
        hero_name = hero.get("hero_name")
        # print("名称:",hero_name)  # ./hero/pictures/上官婉儿/Python.jpg
        hero_path_name = "./hero/pictures/" + hero_name
        # print("存放路径:",hero_path_name)
        # 皮肤列表
        skin_list = hero.get("hero_skin_list")
        # print(skin_list)
        # headers = useragentutil.get_headers()  # 下载多个皮肤都用同一个请求头
        # （3）遍历皮肤列表，获得单个皮肤；
        for skin_element in skin_list:
            # print("皮肤:",skin_element)
            # 皮肤名称
            skin_name = skin_element["skin_name"]
            # 图片链接地址
            skin_image_url = skin_element["skin_href_url"]
            # （4）下载皮肤图片。
            # 获取到图片的内容
            headers = useragentutil.get_headers()  # 下载一个皮肤都用一个请求头(不容易识别是爬虫)
            response = requests.get(skin_image_url, headers=headers)
            image_content = response.content

            # 保存到文件中
            # file = open(hero_path_name+"/"+skin_name+".jpg","wb")
            # file.write(image_content)
            # file.close()
            with open(hero_path_name + "/" + skin_name + ".jpg", "wb") as file:
                file.write(image_content)  # 效率高一些
            print("正在下载英雄(%s)的皮肤图片,皮肤名称:%s" % (hero_name, skin_name))
        print("英雄(%s)的皮肤图片已保存完毕!!!" % hero_name)
        i += 1
    print("所有皮肤图片均已下载完毕,谢谢!")


if __name__ == '__main__':
    main()
