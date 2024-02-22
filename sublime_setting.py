import os, sys
import click, json, re
import PySimpleGUI as sg
sg.theme('SystemDefault')

if True:
    dic_sublime_settings = {
        'VM-TESTER': r'C:\Users\user\AppData\Roaming\Sublime Text 3\Packages\User\Preferences.sublime-settings',
    }
    computer = os.environ['COMPUTERNAME']
    if computer not in list(dic_sublime_settings.keys()):
        raise TypeError('computer is not found!') # 不同電腦將引發錯誤
    sublime_setting = dic_sublime_settings.get(computer)
    ps = sublime_setting


@click.command() # 命令行入口
@click.option('-mode', help='your setting mode', required=True, type=int)    # 設定方式 0依照預設值 1依專案設定值
@click.option('-project', help='your project name', required=True, type=str) # 專案名稱
def main(mode, project):
    print(f'mode: {mode}')
    print(f'project name: {project}')

    # 寫入預設值
    with open('default.sublime-settings', encoding='utf-8') as f:
        content_default = f.read()
    with open(sublime_setting, 'w') as f:
        f.write(content_default)

    if mode == 1: # 1依專案設定值

        with open('regist_project.json', encoding='utf-8') as f: # 讀取專案路徑
            dic = json.loads(f.read())
        # print(f'project path: {dic[project]}')

        if project not in list(dic.keys()):
            sg.popup(f'{project} no regist!') # debug
            return

        pj_config = os.path.join(dic[project], 'sublime_hide.py') # 取得專案設定config
        # print(f'project config: {pj_config}')

        sys.path.append(dic[project])     # 添加專案路徑
        from sublime_hide import is_hide  # 匯入 is_hide
        # print(f'project is_hide: {is_hide}')

        if is_hide: # 欲隱藏 檔案或資料夾

            lis_files   = get_hide_files(pj_config)   # 依專案設定 取得 隱藏檔案  list
            lis_folders = get_hide_folders(pj_config) # 依專案設定 取得 隱藏資料夾 list
            # print('hide files:')
            # for e in lis_files:
            #     print(f'    {e}')
            # print('\nhide folders:')
            # for e in lis_folders:
            #     print(f'    {e}')

            with open(sublime_setting, encoding='utf-8') as f: # 讀取目前 sublime_setting
                dic = json.loads(f.read())

            dic['file_exclude_patterns'] = lis_files         # 設定 sublime_setting 隱藏檔案
            dic['folder_exclude_patterns'] = lis_folders     # 設定 sublime_setting 隱藏資料夾
            json_str = json.dumps(dic, indent = 4) #格式化
            # print(json_str)
            with open(sublime_setting, 'w') as f:            # 儲存 sublime_setting
                f.write(json_str)

    # sg.popup(f'程式執行結束，按ok後離開') # debug


def get_hide_files(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'custom_hide_files\s*=\s*\[([^]]*)\]', re.DOTALL)
    match = pattern.search(content)
    lis = []
    if match:
        match_content = match.group(1) # 欲隱藏者 使用註解掉 符合使用者習慣
        lis = re.findall(r'#\s*\'([^\']*)\'', match_content)

    lis = list(filter(lambda e: e != os.path.basename(__file__), lis)) # 排除自身
    return lis

def get_hide_folders(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'custom_hide_folders\s*=\s*\[([^]]*)\]', re.DOTALL)
    match = pattern.search(content)
    if match:
        match_content = match.group(1) # 欲隱藏者 使用註解掉 符合使用者習慣
        lis = re.findall(r'#\s*\'([^\']*)\'', match_content)
        return lis

def set_option(lis_files=[], lis_folders=[]):
    # lis_file     隱藏檔案
    # lis_folders  隱藏資料夾
    with open(sublime_setting, encoding='utf-8') as data:
        dic = json5.loads(data.read())
    dic['file_exclude_patterns'] = lis_files
    dic['folder_exclude_patterns'] = lis_folders
    json_str = json.dumps(dic, indent = 4) #格式化
    with open(ps, 'w') as outfile:
        outfile.write(json_str)
    # print('write hide is finished')

def test1():
    print('test1')

if __name__ == '__main__':
    # test1()
    main()
