#
    # 此檔案放在個專案資料夾底下  用來控制資料夾，檔案的隱藏狀態，有2種執行方式
    # 1. 由ahk監控切換sublime專案後執行：註冊 C:\Users\user\Documents\Rogers\sublime_text_ffds\regist_project.json
    # 2. 儲存本設定檔後自動執行：此腳本由 SublimeOnSaveBuild (sublime套件) 設定為儲存後自動執行
    # 採用註解符號 # 來控制單引號'' 中的檔案名稱，進行隱藏，符合編程習慣
import os, subprocess

is_hide = True  # True | False
custom_hide_files = [ # 檔案設定顯示隱藏 使用註解將被隱藏
    # -- file
    # '.gitattributes',
    # '.gitignore',

    # 'default.sublime-settings',
    'environment.py',
    # 'sublime_setting.py',
    # 'sublime_hide.py',
    'readme.md',

    # -- ahk
    # 'hide.ico',
    # 'switch_windows.ahk',

    # -- test
    # 'test.bat',
    # 'test_ahk.ahk',
    ]

custom_hide_folders = [
    # --git
    # '.git',
    # --python
    # '__pycache__',
]

def main():
    pj_name = os.path.basename(os.path.dirname(__file__))
    command = f'python sublime_setting.py -project {pj_name} -mode 1'
    cwd = r'C:\Users\user\Documents\Rogers\sublime_text_ffds'
    subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
if __name__ == '__main__':
    main()