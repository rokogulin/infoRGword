'''
ime = 'rokoabc'
rezultat = 19
rijec='STALE'
'''
listrepo='lista.txt'
lista_spremljena=[]


def listwrite(name, score, word):
    place=0
    with open(listrepo, 'r', encoding='utf_8') as lista:
        lenght=len(lista.readlines())
        lista.seek(0)
        for i in range(lenght):
            lista_spremljena.append(lista.readline().split(' '))

    for i in range (len(lista_spremljena)):
        if score > int(lista_spremljena[i][0]):
            place=i+1
    lista_spremljena.insert(place, [score, name, word])
    with open(listrepo, 'w', encoding='utf_8') as lista:
        for x in lista_spremljena:
            lista.write(str(x[0])+' '+x[1]+' '+x[2])

def printl():
    with open(listrepo, 'r', encoding='utf_8') as lista:
        print(lista.read())
        exitt=input('exit')
if __name__=='__main__':
    printl()
    