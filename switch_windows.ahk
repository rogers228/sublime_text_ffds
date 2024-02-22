#Persistent ;持續執行
#SingleInstance force ;禁止多開
SetTitleMatchMode, 2  ; 設定標題匹配模式
#Include %A_ScriptDir%\JSON.ahk ;引用

FileRead, content_json, %A_ScriptDir%\regist_project.json ;讀取文字檔案 內容應為json
obj := JSON.Load(content_json) ;解析json文字為object
arr_pj := [] ; 建立陣列 值為專案名稱
for key, _ in obj {
    arr_pj.Push(key)
}

Loop
{
    WinGet, ahk_exe, ProcessName, A    ; 獲取當前活動視窗的 ahk_exe
    if (ahk_exe == "sublime_text.exe") ; 僅針對 sublime text
    {
        WinGetActiveTitle, curr_title  ; 獲取當前活動視窗的標題
        RegexMatch(curr_title, "\((.*?)\)", match) ; 正則擷取括號內的文字
        curr_pj = %match1% ;取得一個括號 為當前專案名稱
        if (project != curr_pj && curr_pj != "") ; 僅專案名稱改變時
        {
            ; MsgBox, %curr_pj%  ; 顯示標題
            project := curr_pj   ; 儲存專案名稱
            run_py() ; 帶參數執行 python
        }
    }
}

run_py(){
    Global arr_pj
    Global project
    mode := 0 ; # mode 設定方式 0依照預設值 1依專案設定值
    for _, value in arr_pj{
        if (project == value) ; 僅針對有註冊的專案
        {
            mode = 1
            break  ; 跳出循环
        }
    }
    Run, python sublime_setting.py -mode %mode% -project %project%, , Hide ; 帶參數執行 python 參數為專案名稱
}