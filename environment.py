# environment config
import os

computer = os.environ['COMPUTERNAME']

# 依照電腦 設定專案資料夾的位置
dic_base = {
    'VM-TESTER': r'C:\Users\user\Documents\Rogers',
}

# 依照電腦 設定sublime-setting位置
dic_sublime_settings = {
    'VM-TESTER': r'C:\Users\user\AppData\Roaming\Sublime Text 3\Packages\User\Preferences.sublime-settings',
}

# 註冊專案 regist project 專案名稱必須是專案資料夾名稱
# 統一使用單引號' 一行一個專案，  供autohotkey正則抓取
# 專案後方的 # project 不可刪除  供autohotkey正則抓取

lis_projects = [
    'ys_yrpc',           # project
    'sublime_text_ffds', # project
    'password_note',     # project
    ]

def test1():
    print(f'your computer name is {computer}.')
    print(f'dic_base is {dic_base[computer]}.')
    print(f'dic_sublime_settings is {dic_sublime_settings[computer]}.')
    print('projects:', lis_projects)

if __name__ == '__main__':
    test1()