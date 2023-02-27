import argparse
import logging
import winreg
import time
import sys
import os

# A (hopefully/mostly) fool proof method of getting a logging dir 
try:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         'SOFTWARE\\Daniel Vahsholtz\\WOW6432Node\\Wlchgr', 0, winreg.KEY_READ)
    reg_value, ____regtype = winreg.QueryValueEx(key, 'WlchgrEXELogLocation')
    winreg.CloseKey(key)
except Exception:
    reg_value = None
    reg_exception = sys.exc_info()[1]
else:
    reg_exception = None

if reg_exception != None:
    try:
        os.chdir('C:/Program Files (x86)/Daniel Vahsholtz/wlchgr/Logs')
    except Exception:
        print('Error happened when trying to set the directory. Trying to fix that.')
        print(f'Error: {sys.exc_info()[1]}')
        try:
            os.mkdir(
                'C:/Program Files (x86)/Daniel Vahsholtz/wlchgr/Logs')
            os.chdir(
                'C:/Program Files (x86)/Daniel Vahsholtz/wlchgr/Logs')
        except Exception:
            print(f'wlchgr wasn\'t able to start properly. Error: {sys.exc_info()[1]}. Killing wlchgr.exe.')
            sys.exit('Killed wlchgr.exe')

elif reg_exception == None:
    if reg_value != None:
        try:
            os.chdir(reg_value)
        except Exception:
            print('Error happened when trying to set the directory. Trying to fix that.')
            print(f'Error: {sys.exc_info()[1]}')
            try:
                os.mkdir(reg_value)
                os.chdir(reg_value)
            except Exception:
                print(
                    'Error happened when trying to set the directory. Trying to fix that.')
                print(f'Error: {sys.exc_info()[1]}')
                try:
                    os.mkdir(
                        'C:/Program Files (x86)/Daniel Vahsholtz/wlchgr/Logs')
                    os.chdir(
                        'C:/Program Files (x86)/Daniel Vahsholtz/wlchgr/Logs')
                except Exception:
                    print(f'wlchgr wasn\'t able to start properly. Error: {sys.exc_info()[1]}. Killing wlchgr.exe.')
                    sys.exit('Killed wlchgr.exe')
    else:
        print('An internal error has occured. Killing wlchgr.exe. Error: reg_value == \'None\'')
        sys.exit('Killed wlchgr.exe')

else:
    print('An internal error has occured. Killing wlchgr.exe. Error: reg_exception was neither \'== None\' or \'!= None\'.')
    sys.exit('Killed wlchgr.exe')

# Logging logs
____lfn = time.strftime('%m-%d-%Y__%H;%M;%S')
logging.basicConfig(filename= ____lfn + '.log', encoding='utf-8', level=logging.DEBUG, format='%(pathname)s : %(asctime)s:%(msecs)d : %(levelname)s : %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.info('Logger set up')

# Starting Vars
program_version = '0.1'

program_name = f'''Wlchgr CLI [Version {program_version}] | (c) 2022-Present Daniel Vahsholtz'''

logging.debug('program_name = ' + program_name)

program_name = f'''Wlchgr CLI [Version {program_version}]
(c) 2022-Present Daniel Vahsholtz
'''
program_description = '''Wlchgr is a command line interface for the wallpaper on Windows made by Daniel Vahsholtz'''

# Parser
parser = argparse.ArgumentParser(prog='wlchgr', description=program_name, epilog='', formatter_class=argparse.RawDescriptionHelpFormatter, allow_abbrev=False, prefix_chars='-/')

logging.debug('Parser has been setup.')

parser.add_argument("filepath", help="the location of the file to be set as wallpaper by %(prog)s.")
parser.add_argument('-?', '/?', '/h', '/help', action='help', help='show this help message and exit')
parser.add_argument('-v', '--version', action='version', version=f'{program_name}\n{program_description}\n ')

logging.debug('Args have been setup.')

args = parser.parse_args()

def getreg(path, name, hkey=winreg.HKEY_LOCAL_MACHINE, rights=winreg.KEY_READ):
    try:
        k = winreg.OpenKey(hkey, path, 0, rights)
        value, regtype = winreg.QueryValueEx(k, name)
        winreg.CloseKey(k)
        return value
    except Exception:
        return f'Error: {sys.exc_info()[1]}'


if __name__ == '__main__':
    pass
