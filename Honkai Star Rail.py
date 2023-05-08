from get_width import get_width
import time

def main():
    print("脚本将于5秒后运行,请确保你的游戏置顶")
    time.sleep(5)
    get_width()
    from tool.map import map
    map_instance = map()
    print("开始运行，请勿移动鼠标和键盘\n若脚本运行无反应,请使用管理员权限运行")
    map_instance.auto_map_1_1()  # 基座舱段
    map_instance.auto_map_1_2()  # 收容舱段
    map_instance.auto_map_1_3()  # 支援舱段
    map_instance.auto_map_2_1()  # 城郊雪原
    map_instance.auto_map_2_2()  # 边缘通路
    map_instance.auto_map_2_3()  # 残响回廊
    print("脚本已经完成运行")


if __name__ == '__main__':
    main()