# sublime_text_ffds
**files and folders display by project.**

1. 在sublime text編程時，切換視窗後，Sidebar依據不同的project來隱藏檔案或資料夾
2. 設定後可立即更新

# 工作原理
使用ahk監控切換視窗，當切換sublime text視窗時，觸發執行py，讀取專案config 設定sublime-settings

## 檔案說明

|檔案|說明|
|--|--|
|regist_project.json      | 註冊啟用的sublime text project        |
|switch_windows.ahk       | windows層級，監看視窗切換，觸發執行py   |
|sublime_setting.py       | setting sublime by python             |
|sublime_hide.py          | project config                        |
|default.sublime-settings | sublime-settings default value 預設值 |

## 使用方式
1. 你的電腦必須安裝 python and autohotkey
2. regist_project.json  註冊專案名稱及路徑。
3. sublime_setting.py中 找到dic_sublime_settings 設定電腦名稱與sublime_settings路徑。
4. 複製 sublime_hide.py 到您的專案資料夾底下，設定後儲存即可。
5. 運行 switch_windows.ahk

## 專案config 'sublime_hide.py'

'sublime_hide.py'，放在個別專案資料夾底下，每個專案可以個別設定，

採用註解符號 # 來控制單引號'' 中的檔案名稱，進行隱藏，符合編程習慣。
可用編輯器的預設快速鍵 Ctrl + / 來切換註解 #
```
    # '.gitattributes', --> hide
    # '.gitignore',     --> hide
    'readme.md',        --> display
```