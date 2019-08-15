#para inciciar o jogo
x = True
#para colocar os números no tabuleiro

c1 = [' ',' ',' ',' ','7',' ',' ','1',' ']
c2 = [' ','6','8',' ','5','9',' ',' ',' ']
c3 = ['4','9','7',' ',' ',' ',' ',' ','5']
c4 = [' ',' ',' ',' ','6',' ',' ','8',' ']
c5 = ['9',' ',' ',' ',' ',' ',' ',' ','7']
c6 = [' ','3',' ',' ','8',' ','9','6','4']
c7 = ['6','2','3',' ','9',' ',' ',' ',' ']
c8 = [' ','7',' ',' ',' ','8',' ','4',' ']
c9 = [' ',' ',' ',' ',' ','2',' ',' ',' ']

d1 = ['3','5','2','4','7','6','8','1','9']
d2 = ['1','6','8','3','5','9','4','7','2']
d3 = ['4','9','7','8','2','1','6','3','5']
d4 = ['2','4','5','9','6','7','3','8','1']
d5 = ['9','8','6','1','4','3','5','2','7']
d6 = ['7','3','1','2','8','5','9','6','4']
d7 = ['6','2','3','7','9','4','1','5','8']
d8 = ['5','7','9','6','1','8','2','4','3']
d9 = ['8','1','4','5','3','2','7','9','6']
#função para printar o tabuleiro
def tab():
    print(' |-1-2-3-4-5-6-7-8-9-')
    print(' A|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c1 [0], c1[1], c1[2], c1[3], c1[4], c1[5], c1[6], c1[7], c1[8]))
    print(' B|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c2 [0], c2[1], c2[2], c2[3], c2[4], c2[5], c2[6], c2[7], c2[8]))
    print(' C|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c3 [0], c3[1], c3[2], c3[3], c3[4], c3[5], c3[6], c3[7], c3[8]))
    print(' |-------------------')
    print(' D|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c4 [0], c4[1], c4[2], c4[3], c4[4], c4[5], c4[6], c4[7], c4[8]))
    print(' E|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c5 [0], c5[1], c5[2], c5[3], c5[4], c5[5], c5[6], c5[7], c5[8]))
    print(' F|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c6 [0], c6[1], c6[2], c6[3], c6[4], c6[5], c6[6], c6[7], c6[8]))
    print(' |-------------------')
    print(' G|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c7 [0], c7[1], c7[2], c7[3], c7[4], c7[5], c7[6], c7[7], c7[8]))
    print(' H|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c8 [0], c8[1], c8[2], c8[3], c8[4], c8[5], c8[6], c8[7], c8[8]))
    print(' I|{}|{}|{}|{}|{}|{}|{}|{}|{}|'.format(c9 [0], c9[1], c9[2], c9[3], c9[4], c9[5], c9[6], c9[7], c9[8]))
    print(' |-------------------' )

#função para definir se tem ganhador 
def tem_g():
    if c1 == d1 and c2 == d2 and c3 == d3 and c4 == d4 and c5 == d5 and c6 == d6 and c7 == d7 and c8 == d8 and c9 == d9:
        return True
    return False
#função para validar a jogada    
def jv():
    if l == 'A' and l == 'B' and l == 'C' and l == 'D' and l == 'E' and l == 'F' and l == 'G' and l == 'H' and l == 'I':
        return True
    if c == '1' and c == '2' and c == '3' and c == '4' and c == '5' and c == '7' and c == '8' and c == '9':
        return True
    else:
        return False
#função para acrescentar os números nas casas desejadas
def jog():
    #while para até não ter ganhador o jogo continuar rodando
    while  not tem_g() :
        tab()
        l = input ("qual linha você quer jogar: ").upper()
        c = input ("qual coluna você quer jogar: ")
        print (" numeros para serem acrescentados são de 1 à 9 ")
        n = input("qual o numero que você quer acrescentar: ")
        if l == 'A':
                if c == '1':
                    c1[0] = n
                elif c == '2':
                    c1[1] = n
                elif c == '3':
                    c1[2] = n
                elif c == '4':
                    c1[3] = n
                elif c == '5':
                    print ("está ocupada")
                elif c == '6':
                    c1[5] = n
                elif c =='7':
                    c1[6]= n
                elif c == '8':
                    print ("está ocupada")
                elif c == '9':
                    c1[8]= n
        elif l == 'B':
                if c == '1':
                    c2[0] = n
                elif c == '2':
                    print ("está ocupada")
                elif c == '3':
                    print ("está ocupada")
                elif c == '4':
                    c2[3] = n
                elif c == '5':
                    print ("está ocupada")
                elif c == '6':
                    print ("está ocupada")
                elif c =='7':
                    c2[6]= n
                elif c == '8':
                    c2[7]= n
                elif c == '9':
                    c2[8]= n
        elif l == 'C':
                if c == '1':
                    print ("está ocupada")
                elif c == '2':
                    print ("está ocupada")
                elif c == '3':
                    print ("está ocupada")
                elif c == '4':
                    c3[3] = n
                elif c == '5':
                    c3[4] = n
                elif c == '6':
                    c3[5] = n
                elif c =='7':
                    c3[6]= n
                elif c == '8':
                    c3[7]= n
                elif c == '9':
                    print ("está ocupada")
        elif l == 'D':
                if c == '1':
                    c4[0] = n
                elif c == '2':
                    c4[1] = n
                elif c == '3':
                    c4[2] = n
                elif c == '4':
                    c4[3] = n
                elif c == '5':
                    print ("está ocupada")
                elif c == '6':
                    c4[5] = n
                elif c == '7':
                    c4[6]= n
                elif c == '8':
                    print ("está ocupada")
                elif c == '9':
                    c4[8]= n
        elif l == 'E':
                if c == '1':
                    print ("está ocupada")
                elif c == '2':
                    c5[1] = n
                elif c == '3':
                    c5[2] = n
                elif c == '4':
                    c5[3] = n
                elif c == '5':
                    c5[4] = n
                elif c == '6':
                    c5[5] = n
                elif c =='7':
                    c5[6]= n
                elif c == '8':
                    c5[7]= n
                elif c == '9':
                    print ("está ocupada")
        elif l == 'F':
                if c == '1':
                    c6[0] = n
                elif c == '2':
                    print ("está ocupada")
                elif c == '3':
                    c6[2] = n
                elif c == '4':
                    c6[3] = n
                elif c == '5':
                    print ("está ocupada")
                elif c == '6':
                    c6[5] = n
                elif c =='7':
                    print ("está ocupada")
                elif c == '8':
                    print ("está ocupada")
                elif c == '9':
                    print ("está ocupada")
        elif l == 'G':
                if c == '1':
                    print ("está ocupada")
                elif c == '2':
                    print ("está ocupada")
                elif c == '3':
                    print ("está ocupada")
                elif c == '4':
                    c7[3] = n
                elif c == '5':
                    print ("está ocupada")
                elif c == '6':
                    c7[5] = n
                elif c =='7':
                    c7[6]= n
                elif c == '8':
                    c7[7]= n
                elif c == '9':
                    c7[8]= n
        elif l == 'H':
                if c == '1':
                    c8[0] = n
                elif c == '2':
                    print ("está ocupada")
                elif c == '3':
                    c8[2] = n
                elif c == '4':
                    c8[3] = n
                elif c == '5':
                    c8[4] = n
                elif c == '6':
                    print ("está ocupada")
                elif c =='7':
                    c8[6]= n
                elif c == '8':
                    print ("está ocupada")
                elif c == '9':
                    c8[8]= n
        elif l == 'I':
                if c == '1':
                    c9[0] = n
                elif c == '2':
                    c9[1] = n
                elif c == '3':
                    c9[2] = n
                elif c == '4':
                    c9[3] = n
                elif c == '5':
                    c9[4] = n
                elif c == '6':
                    print ("está ocupada")
                elif c =='7':
                    c9[6]= n
                elif c == '8':
                    c9[7]= n
                elif c == '9':
                    c9[8]= n
    print("PARABÉNS!!! VOCÊ VENCEU")
#função para o jogador escolher se joga ou não == menu
while x == True:
    print("1 para jogar..")
    print("2 para sair...")
    y = input(" ")
    if y == '1':
        #para limpar o tabuleiro
        c1 = [' ',' ',' ',' ','7',' ',' ','1',' ']
        c2 = [' ','6','8',' ','5','9',' ',' ',' ']
        c3 = ['4','9','7',' ',' ',' ',' ',' ','5']
        c4 = [' ',' ',' ',' ','6',' ',' ','8',' ']
        c5 = ['9',' ',' ',' ',' ',' ',' ',' ','7']
        c6 = [' ','3',' ',' ','8',' ','9','6','4']
        c7 = ['6','2','3',' ','9',' ',' ',' ',' ']
        c8 = [' ','7',' ',' ',' ','8',' ','4',' ']
        c9 = [' ',' ',' ',' ',' ','2',' ',' ',' ']
        jog()
        
    elif y == '2':
        x = False
