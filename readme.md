# sublime_text_ffds
files and folders display setting by sublime text project.
在sublime text編程時，切換視窗後，依據不同的project來隱藏檔案或資料夾

# 工作原理
使用ahk監控切換視窗，

## 檔案說明
|檔案|說明|
|--|--|
|regist_project.json | 註冊啟用的sublime text project       |
|switch_windows.ahk  | windows層級，監看視窗切換，觸發執行py |