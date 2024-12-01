import importlib
import os
import inspect
import dearpygui.dearpygui as dpg
import pyautogui
import re
from pathlib import Path

dpg.create_context() #必须放在第一行
# dpg.show_documentation()  #内置文档能够搜索各种函数以及用法
# dpg.show_style_editor()   #界面主体样式工具（能够调整各种边框、字体颜色等）
# dpg.show_debug()          #调试debugger工具
# dpg.show_about()          #关于软件的版本信息
# dpg.show_metrics()        #能够看见当前设备的实时刷新率、各种设备监听
# dpg.show_font_manager()   #字体管理工具，显示所有加载的字体及其适当的大小
# dpg.show_item_registry()  #项目注册表
# ------------------------------
视口宽度,视口高度 = pyautogui.size()



# ------------------------------
#固定套路万年不变↓

dpg.create_viewport(title='DPG viewport tool', width=视口宽度-100, height=视口高度-100)
dpg.setup_dearpygui()
# GM = 界面管理员类.GM("zn")

dpg.show_viewport()
dpg.start_dearpygui()   # ←真正的循环点
dpg.destroy_context()