# coding:utf-8
import lxml.html
import os
import json
from selenium import webdriver
import time


def parse_hero_url(http_url):
    """发送请求；获取页面结果"""
    # 获得浏览器对象
    pjs_path = r"E:\PythonTools\chrome\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    browser = webdriver.PhantomJS(pjs_path)
    # 请求网址
    browser.get(http_url)
    time.sleep(2)
    # 暂停  --操作页面数据  find_elements_by_xpath()  find_element_by_xpath()
    # 获得网页源代码  page_source
    hero_html_content = browser.page_source
    # print(hero_html_content)
    # 关闭
    browser.quit()
    return hero_html_content


def get_hero_info_list(html_content):
    """提取英雄数据信息"""
    metree = lxml.html.etree
    hero_info_parser = metree.HTML(html_content)
    # 开始解析
    li_list = hero_info_parser.xpath("//div[@class='herolist-content']/ul[@class='herolist clearfix']/li")
    # print(li_list)
    # print(len(li_list))
    # 空列表,存放英雄信息的
    hero_info_list = []
    # 遍历
    for li_element in li_list:
        # 空字典
        item = {}
        # 英雄名称
        hero_name = li_element.xpath("./a/text()")[0]
        # print(hero_name)
        # item["英雄名称"] = hero_name
        item["hero_name"] = hero_name
        # 英雄图片地址
        hero_image_url = "https:" + li_element.xpath("./a/img/@src")[0]
        # print(hero_image_url)
        item["hero_image_url"] = hero_image_url
        # 详情链接地址
        hero_href_url = "https://pvp.qq.com/web201605/" + li_element.xpath("./a/@href")[0]
        # print(hero_href_url)   # 独立
        item["hero_href_url"] = hero_href_url
        # print(item)
        hero_info_list.append(item)
    # print(hero_info_list)
    return hero_info_list


def save_hero_info_file(datas):
    # 新建文件夹
    path_name = "./hero"
    # 不存在则创建
    if not os.path.exists(path_name):
        os.makedirs(path_name)
        print("目录[%s]已创建成功..." % path_name)
    # 保存数据
    hero_file = open(path_name + "/hero.json", "w", encoding="utf-8")
    json.dump(datas,
              hero_file,
              ensure_ascii=False,
              indent=2)
    print("所欲英雄数据已保存成功,谢谢!")


def main():
    # 网址
    hero_url = "https://pvp.qq.com/web201605/herolist.shtml"
    # parse_hero_url(hero_url)
    hero_html_datas = parse_hero_url(hero_url)
    # print(hero_html_datas)

    # 格式化:Ctrl+Alt+L
    # 获取数据
    hero_info_datas = get_hero_info_list(hero_html_datas)
    # print(hero_info_datas)

    # 保存英雄数据到文件中
    save_hero_info_file(hero_info_datas)


if __name__ == '__main__':
    main()
