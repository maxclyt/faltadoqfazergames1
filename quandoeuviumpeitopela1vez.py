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
                   
       
#resenha 2
import time

seepeito = 1
spectator = 1

print("when spectator see peito pela primeira vez print:" )
time.sleep(2)
if spectator == seepeito:
    print("meu deus do ceu pai")
    time.sleep(1)
    print("nossa senhora ta")
    time.sleep(1)
    print("deus abencoe")
    
    
