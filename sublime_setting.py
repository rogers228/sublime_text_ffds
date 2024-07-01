if True:
    import os, sys
    import click, json, re
    import PySimpleGUI as sg
    sg.theme('SystemDefault')

    # glogal
    sys.path.append(os.getenv('GRST_PATH'))             # 添加 GRST_PATH 路徑
    from global_config import OPTION, current_base_path # 匯入 global_config
    # current_base_path() 目前電腦 的 所有倉庫的上層路徑
    from tool_path import (_p, full_file)
    # _p(full_file) 上層路徑

    # environment
    from environment import lis_projects


debug = False # True | False
if True:
    if OPTION.get('SUBLIME_SETTING_PATH', '') == '':
        raise TypeError('SUBLIME_SETTING_PATH is not found!') # 找不到參數
    sublime_setting = OPTION.get('SUBLIME_SETTING_PATH')[os.environ['COMPUTERNAME']]

@click.command() # 命令行入口
@click.option('-mode', help='your setting mode', required=True, type=int)    # 設定方式 0依照預設值 1依專案設定值
@click.option('-project', help='your project name', required=True, type=str) # 專案名稱
def main(mode, project):
    if debug: print(f'mode: {mode} type: {type(mode)}\nproject name: {project}')

    with open('default.sublime-settings', encoding='utf-8') as f: # 讀取預設值
        df = json.loads(f.read()) # dic_default

    if mode == 0: # 0依照預設值
        pass

    if mode == 1: # 1依專案設定值

        if project not in lis_projects:
            sg.popup(f'{project} no regist!') # debug
            return

        project_path = os.path.join(current_base_path(), project)
        if debug: print(f'project path: {project_path}')

        pj_config = os.path.join(project_path, 'sublime_hide.py') # 取得專案設定config
        if debug: print(f'project config: {pj_config}')

        is_hide = get_is_hide(pj_config) # 依專案設定 取得 is_hide
        if debug: print(f'is_hide: {is_hide}')

        if is_hide: # 欲隱藏 檔案或資料夾
            lis_files   = get_hide_files(pj_config)   # 依專案設定 取得 隱藏檔案  list
            lis_folders = get_hide_folders(pj_config) # 依專案設定 取得 隱藏資料夾 list
            if debug:
                print('\nhide files:')
                for e in lis_files:
                    print(f'    {e}')
                print('\nhide folders:')
                for e in lis_folders:
                    print(f'    {e}')

            df['file_exclude_patterns'] = lis_files     # 設定 sublime_setting 隱藏檔案
            df['folder_exclude_patterns'] = lis_folders # 設定 sublime_setting 隱藏資料夾
        else:
            df['file_exclude_patterns'] = []
            df['folder_exclude_patterns'] = []

    json_str = json.dumps(df, indent = 4) # 格式化
    if debug: print(f'\nsublime-settings:\n{json_str}')

    with open(sublime_setting, 'w') as f: # 儲存 sublime_setting
        f.write(json_str)

    if debug: sg.popup(f'程式執行結束，按ok後離開') # debug

def get_hide_files(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'custom_hide_files\s*=\s*\[([^]]*)\]', re.DOTALL)
    match = pattern.search(content)
    lis = []
    if match:
        match_content = match.group(1) # 欲隱藏者 使用註解掉 符合使用者習慣
        lis = re.findall(r'#\s*\'([^\']*)\'', match_content)

    lis = list(filter(lambda e: e != 'sublime_hide.py', lis)) # 排除 sublime_hide.py
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

def get_is_hide(file):
    with open(file, encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'is_hide\s*=\s*(\w+)', content)
    if match:
        is_hide_value = match.group(1)
        is_hide = True if is_hide_value.lower() == 'true' else False
        return is_hide
    else:
        return False

def test1():
    print('test1')

if __name__ == '__main__':
    # test1()
    main()

