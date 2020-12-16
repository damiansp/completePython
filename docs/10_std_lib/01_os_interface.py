import os
import shutil


print(os.getcwd())
#os.chdir('my/path')
os.system('mkdir 11_std_lib_2')

print('dir(os):')
print(dir(os))

shutil.copyfile('01_os_interface.py', '01_os_interface.py.bk')
shutil.move('01_os_interface.py.bk', '01_os.bk')
