import os
os.system('')
import random
import sort
import bojanje

def game(name):
    l=[]
    check=[]
    check_state=0
    cilj=''
    guess=''
    uk_slova=5
    pokusaji=0
    ime=name
    #lista_spremljena=[[]]
    #lista_nova=[[]]
    states=[0]*uk_slova
    cilj_state=[2]*uk_slova
    wrepo="words2.txt"
    crepo="words.txt"
    listrepo="lista.txt"
    '''
    def listwrite(name, score):
        with open(listrepo, 'r', encoding='utf_8') as lista:
            for i in range(len(lista.readlines())):
                lista_spremljena+=lista.readline().split(' ')
        for i in range (len(lista_spremljena)):
            if score < int(lista_spremljena[i][1]):
                place=i
        lista_nova=lista_spremljena.insert(place, [name, score])
        print (lista_nova)
    '''        
    
          
    with open (wrepo, 'r', encoding='utf_8') as f:
        l=f.readlines()
        cilj=l[random.randint(0,len(l)-1)]
        
    with open(crepo, 'r', encoding='utf_8') as c:
        check=c.readlines()
    '''    
    with open(listrepo, 'r', encoding='utf_8') as lista:
        lista_spremljena=lista.readlines()
    '''
    while states != cilj_state:
            guess=input('')
            if len(guess) != uk_slova:
                  print('Mora bit ' +  str(uk_slova) + ' slova')
            elif (guess.upper() not in check or guess.lower() not in check) and check_state==1:
                print('nije rijec')
            else:
                pokusaji+=1
                for i in range(uk_slova):
                    if guess[i].upper() in cilj:
                        states[i] = 1
                        if guess[i].upper()==cilj[i]:
                                states[i] = 2
                    else:
                        states[i]=0
                print ('\033[1A\033[K', end='')
                print(bojanje.bojanje(states, guess))
                ##print(states)
    print('POBJEDA')
    sort.listwrite(ime, pokusaji, cilj)
    exitt=input('exit')

    
    
    
                    
                    
            
    '''
    def prGreen(s): print("\033[92m {}\033[00m".format(s))
    def prYellow(s): print("\033[93m {}\033[00m".format(s))
    def prRed(s): print("\033[91m {}\033[00m".format(s))
    def prLightGray(s): print("\033[97m {}\033[00m".format(s))
    
    prYellow("It's")
    prGreen("Geeks")
    '''
