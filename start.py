import os
import project
import sort
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'pick-2.6.0/src')
print(vendor_dir)
sys.path.append(vendor_dir)

from pick import pick

os.system('cls' if os.name == 'nt' else 'clear')
ime=input('ime')


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    #mode = int(input('1 igraj \n2 lista \n3 exit\n4 promijeni ime\n'))
    options=['igraj', 'lista', 'izlaz', 'promijeni ime']
    option, mode = pick(options, 'odabir')
    if mode == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        project.game(ime)
    elif mode == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        sort.printl()
    elif mode == 2:
        print('byeeeee')
        exit()
    elif mode == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        ime=input('novo ime')
 
