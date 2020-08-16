# coding:utf-8
import json
from selenium import webdriver


def read_hero_info_file_from_json():
    """读取json文件，获取数据"""
    hero_file = open("./hero/hero.json", "r", encoding="utf-8")
    hero_result = json.load(hero_file)
    return hero_result


def catch_hero_skin_url_list(http_url):
    """爬取英雄的链接地址,获得所有英雄皮肤"""
    pjs_path = r"E:\PythonTools\chrome\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    browser = webdriver.PhantomJS(pjs_path)
    browser.maximize_window()
    # 请求
    browser.get(http_url)
    # 提取英雄皮肤标签列表
    li_list = browser.find_elements_by_xpath("//div[@class='pic-pf']/ul/li")
    # print(li_list)
    # print(len(li_list))
    # 皮肤列表
    hero_skin_list = []
    # 遍历
    for li_element in li_list:
        # 空字典  --对应一个皮肤
        skin_item = {}
        # 皮肤名字
        skin_name = li_element.find_element_by_xpath("./p").text
        # print(skin_name)
        skin_item["skin_name"] = skin_name
        # 皮肤链接
        skin_href_url = "https:" + li_element.find_element_by_xpath(".//img").get_attribute("data-imgname")
        # print(skin_href_url)
        skin_item["skin_href_url"] = skin_href_url
        # print(skin_item)
        hero_skin_list.append(skin_item)
    # 关闭
    browser.quit()
    return hero_skin_list


def save_hero_skin_file(datas):
    """保存皮肤数据信息"""
    skin_file = open("./hero/heroskin.json", "w", encoding="utf-8")
    json.dump(datas,
              skin_file,
              ensure_ascii=False,
              indent=2)


def main():
    # 读取文件
    hero_info_datas = read_hero_info_file_from_json()
    # print(hero_info_datas)
    # 空列表
    hero_skin_info_list = []
    # 遍历
    for hero_element in hero_info_datas:
        # 空字典  --对应一个英雄
        hero_item = {}
        # 英雄名字
        hero_name = hero_element["hero_name"]
        hero_item["hero_name"] = hero_name
        # 链接
        hero_href_url = hero_element["hero_href_url"]
        # print(hero_href_url)
        # 爬取皮肤页面
        hero_skin_info_datas = catch_hero_skin_url_list(hero_href_url)
        # print("正在保存英雄[%s]的皮肤信息:" % hero_name, hero_skin_info_datas)
        hero_item["hero_skin_list"] = hero_skin_info_datas
        # print(hero_item)
        # 添加到列表中
        hero_skin_info_list.append(hero_item)
        # for循环中,保存皮肤数据信息到json文件,数据保存操作  --添加到列表中,就保存  --稳妥
        save_hero_skin_file(hero_skin_info_list)
        print("正在下载英雄(%s)的皮肤信息,请稍后..." % hero_name)
    # for循环外,保存操作  --所有数据都提取成功后,则保存
    print("所有英雄的皮肤数据信息已保存成功,谢谢!")


if __name__ == '__main__':
    main()
