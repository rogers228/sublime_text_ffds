import click

import PySimpleGUI as sg



@click.command() # 命令行入口
@click.option('-project', help='your project name', required=True, type=str) # required 必要的
def main(project):

    sg.theme('SystemDefault')
    sg.popup(f'project: {project}', title='title')
    # print(f'project: {project}')
    # ...



if __name__ == '__main__':
    main()
    input("Press Enter to exit...")