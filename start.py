import os
import project
import sort
os.system('cls' if os.name == 'nt' else 'clear')
ime=input('ime')
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    mode = int(input('1 igraj \n2 lista \n3 exit\n4 promijeni ime\n'))
    if mode == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        project.game(ime)
    elif mode == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        sort.printl()
    elif mode == 3:
        print('byeeeee')
        exit()
    elif mode == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        ime=input('novo ime')
