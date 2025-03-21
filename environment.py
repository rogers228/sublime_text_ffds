# environment config
import os

# 註冊專案 regist project 專案名稱必須是專案資料夾名稱
# 統一使用單引號' 一行一個專案，  供autohotkey正則抓取
# 專案後方的 # project 不可刪除  供autohotkey正則抓取

lis_projects = [
    'ys_yrpc',           # project
    'sublime_text_ffds', # project
    'password_note',     # project
    'selecter',          # project
    'selecter_spic',     # project
    'selecter_fwjs',     # project
    'selecter_esbr',     # project
    'selecter_swaa',     # project
    'ys_pnss2',          # project
    'ys_rd_start',       # project
    'yspp_202501',       # project
    'sg_admin',          # project
    ]

computer = os.environ['COMPUTERNAME']

# # 依照電腦 設定sublime-setting位置
# dic_sublime_settings = {
#     'VM-TESTER': r'C:\Users\user\AppData\Roaming\Sublime Text 3\Packages\User\Preferences.sublime-settings',
# }

# # 依照電腦 設定專案資料夾的 path (專案資料夾的上層)
# dic_base = {
#     'VM-TESTER': r'C:\Users\user\Documents\Rogers',
#     'LAPTOP-LUGP3JBF': r'C:\Users\USER\Documents',
# }

def test1():
    print('projects:', lis_projects)

if __name__ == '__main__':
    test1()