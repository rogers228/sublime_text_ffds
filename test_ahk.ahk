arr_pj := get_projects()
for _, item in arr_pj{
    Msgbox, %item%
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