# sublime_text_ffds
**files and folders display by project.**

1. 在sublime text編程時，切換視窗後，依據不同的project來隱藏檔案或資料夾
2. 設定後立即更新

# 工作原理
使用ahk監控切換視窗，當切換sublime text視窗時，觸發執行py，讀取專案config 設定sublime-settings

## 檔案說明

|檔案|說明|
|--|--|
|regist_project.json      | 註冊啟用的sublime text project        |
|switch_windows.ahk       | windows層級，監看視窗切換，觸發執行py   |
|sublime_setting.py       | windows層級，監看視窗切換，觸發執行py   |
|sublime_hide.py          | project config                        |
|default.sublime-settings | sublime-settings default value 預設值 |

## 使用方式
1. 執行 switch_windows.ahk
2. 複製 sublime_hide.py 至專案資料夾，設定後儲存即可。

## 專案config 'sublime_hide.py'

'sublime_hide.py'，放在個別專案資料夾底下，每個專案可以個別設定，

採用註解符號 # 來控制單引號'' 中的檔案名稱，進行隱藏，符合編程習慣


