# sublime_text_ffds
**files and folders display by project.**

1. 在windows系統使用sublime text編程時，切換視窗後，Sidebar依據不同的project來隱藏檔案或資料夾
2. 儲存config後可立即更新

## Why ffds
sublime text 可以進行設定來達到隱藏檔案或資料夾，在專案側邊欄適當的隱藏很少用的檔案可以讓畫面清爽，工作更專注。但很遺憾sublime text 相當陽春，當切換另一個專案視窗時需要重新設定，頻繁的切換專案已經是工作的常態，非常迫切需要更簡單的作法，我只能就我的微量技術來完成這個任務。所幸現在 ffds 工作正常，對我產生非常大的幫助。

## 工作原理
使用autohotkey監控視窗切換，當切換sublime text視窗時，觸發執行py，
讀取專案config 設定sublime-settings後，即完成隱藏檔案或資料夾。

## 檔案說明

|檔案|說明|
|--|--|
|environment.py           | 環境與專案設定                        |
|switch_windows.ahk       | windows層級，監看視窗切換，觸發執行py   |
|sublime_setting.py       | setting sublime by python             |
|sublime_hide.py          | project config                        |
|default.sublime-settings | sublime-settings default value 預設值 |

## 切換sublime text後更新
完成以下步驟後可達成，切換sublime text後，自動隱藏檔案或資料夾。

1. 你的環境應該是windows系統，電腦必須安裝 python ,autohotkey, 當然包含sublime text。
2. environment.py 註冊專案名稱, 設定專案資料夾路徑，sublime-setting路徑。
3. 複製 sublime_hide.py 到您的專案資料夾底下，設定後儲存即可。
4. 運行 switch_windows.ahk

## project config: 'sublime_hide.py'

- 'sublime_hide.py'，放在個別專案資料夾底下，每個專案可以個別設定，
- 採用註解符號 # 來控制單引號'file_name' 中的檔案名稱，進行隱藏，符合編程習慣。
- 隱藏'sublime_hide.py'本身將自動失效，避免config被隱藏。
- 可用編輯器的預設快速鍵 **Ctrl + /** 來切換註解 #
- 不同的 project config 應保持相同命名為 'sublime_hide.py'

```
    # '.gitattributes', --> hide
    # '.gitignore',     --> hide
    'readme.md',        --> display
```

## 儲存後更新
完成以下步驟後可達成，儲存'sublime_hide.py'後，立即更新。

1. 安裝 SublimeOnSaveBuild (sublime套件) 設定為儲存後自動執行
2. sublime text設定: Preferences > Package Setting > SublimeOnSaveBuild > Setting-User

輸入以下
```json
{
  "build_on_save": 1,
  "filename_filter": "sublime_hide\\.py$",
}
```

