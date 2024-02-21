#Persistent
#SingleInstance force ;禁止多開
SetTitleMatchMode, 2  ; 設定標題匹配模式
#Include %A_ScriptDir%\JSON.ahk

FileRead, content_json, %A_ScriptDir%\regist_project.json
obj := JSON.Load(content_json)
arr_pj := []
for key, _ in obj {
    arr_pj.Push(key)
    ; MsgBox, % "Key: " key "`nValue: " value
}
; for _, value in arr_pj{
;     MsgBox, %value%
; }

Loop
{
    WinGetActiveTitle, curr_title ; 獲取當前活動視窗的標題
    if (title != curr_title && curr_title != "")
    {
        ; MsgBox, %curr_title%  ; 顯示標題
        title := curr_title
        test()
    }
}

test(){
    Global arr_pj
    Global title
    WinGet, ahk_exe, ProcessName, A  ; 獲取當前活動視窗的可執行文件名
    if (ahk_exe == "sublime_text.exe")
    {
        ; MsgBox, %title%
        for _, value in arr_pj{
            ; MsgBox, %value%
            if (InStr(title, value))
            {
                MsgBox, %title%
            }
        }
    }

}