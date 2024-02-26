; C:\Users\user\Documents\Rogers\sublime_text_ffds
; windows層級，監看視窗切換，觸發執行py

#Persistent ;持續執行
#SingleInstance force ;禁止多開
SetTitleMatchMode, 2  ; 設定標題匹配模式
Menu, Tray, Icon, hide.ico ;設定圖示
arr_pj := get_projects() ; 取得所有註冊的專案 讀取 environment.py

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
            run_py() ; 執行 python
        }
    }
}

run_py(){
    Global arr_pj
    Global project
    mode := 0 ; # mode 設定方式 0依照預設值 1依專案設定值
    for _, item in arr_pj{
        if (project == item) ; 僅針對有註冊的專案
        {
            mode := 1
            break
        }
    }
    Run, python sublime_setting.py -mode %mode% -project %project%, , Hide ; 帶參數執行 python
}

get_projects(){
    FileRead, FileContent, environment.py
    is_match = true
    startIndex := 1
    arr_pj := []
    while %is_match%
    {
        RegExMatch(FileContent, "\s*\'(.*)\',\s*#\s*project\s*", match, startIndex)
        if (match1 == ""){
            is_match = false
        }
        else{
            is_match = true
            match_vlaue := match1
            arr_pj.Push(match_vlaue)

            RegExMatch(FileContent, "P)\s*\'(.*)\',\s*#\s*project\s*", match, startIndex)
            match_pos := MatchPos1
            match_len := MatchLen1
            startIndex := match_pos + match_len
        }
    }
    return arr_pj
}