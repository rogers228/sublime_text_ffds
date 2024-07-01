import os, sys
import subprocess

sys.path.append(os.getenv('GRST_PATH'))             # 添加 GRST_PATH 路徑
from global_config import OPTION, current_base_path # 匯入 global_config
# current_base_path() 目前電腦 的 所有倉庫的上層路徑
from tool_path import (_p, full_file)

def test_main():
    # 以下腳本可直接執行檢查
    # print(os.path.join(_p(full_file), 'sublime_setting.py'))
    subprocess.run(['python', os.path.join(_p(full_file), 'sublime_setting.py'), '-mode', '1', '-project', 'sublime_text_ffds'], check=True)


if __name__ == '__main__':
    test_main()
