import json


def read_hero_skin_data_file():
    rfile = open("./hero/heroskin.json","r",encoding="utf-8")
    skin_result = json.load(rfile)
    return skin_result




def main():
    hero_data = read_hero_skin_data_file()
    # print(hero_data)
    item = {}
    hero_name_list = []
    skin_length_list = []
    for element in hero_data:
        hero_name = element["hero_name"]
        skin_length = len(element["hero_skin_list"])

        hero_name_list.append(hero_name)
        skin_length_list.append(skin_length)
    item["hero_name_x"] = hero_name_list
    item["skin_length_y"] = skin_length_list
    # print(item)

    wfile = open("./hero/herodata.json","w",encoding="utf-8")
    json.dump(item,
              wfile,
              ensure_ascii=False,)
    print("保存成功了")



if __name__ == '__main__':
    main()