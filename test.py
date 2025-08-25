import sys, inspect, vnpy
import vnpy.trader.database as vdb

print("vnpy package file:", vnpy.__file__)
print("loader:", vnpy.__loader__)
print("python exe:", sys.executable)
print("sys.path[0:5]:", sys.path[:5])
print("database impl from:", inspect.getsourcefile(vdb))

from vnpy.trader.database import get_database
db = get_database()
print("DB backend class:", type(db), "from", inspect.getmodule(type(db)).__file__)

# import os, inspect
# import vnpy.trader.setting as S

# print("CWD:", os.getcwd())
# print("setting.py file:", inspect.getsourcefile(S))
# print("SETTING_FILENAME:", S.SETTING_FILENAME)

# for k in sorted(S.SETTINGS):
#     if k.startswith("database."):
#         print(k, "=", S.SETTINGS[k])

# from vnpy.trader.utility import load_json
# print(load_json("vt_setting.json"))
