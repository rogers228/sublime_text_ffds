import configparser

def write_state(mystr):
    cf = configparser.ConfigParser()
    cf.read('switch_windows.ini')
    cf.set('program', 'state', str(mystr))
    with open('switch_windows.ini', 'w') as f:
        cf.write(f)

def test1():
    write_state('ready') # run | ready
    print('ok')

if __name__ == '__main__':
    test1()