#resenha1

x = int(input("escreve a resenha:"))
moral = 1
tora = 0
def fat(x):
    global moral
    global tora
    for i in range(1,x+1):
        moral += moral*(i-1)
    return moral

       
       
fat(x)      
print(f'o fatorial da resenha {x} é {moral}')
                   
       
