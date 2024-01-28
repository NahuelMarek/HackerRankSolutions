def print_rangoli(size):
    size+=-1
    ragnoli=""
    ragnoli+=poner_letras(size,size)+"\n"
    for j in range(size-1,-1,-1):
        ragnoli+=poner_letras(j,size)+"\n"
    
    for j in range(1,size+1,1):
        ragnoli+=poner_letras(j,size)+"\n"

    print(ragnoli)

def poner_letras(i,num_of_letras):
    letter="abcdefghijklmnopqrstuvwxyz"
    rag=""
    for letra in range(num_of_letras,i,-1):
        rag+=letter[letra]+"-"
    rag_right = rag[::-1]
    texto=rag+letter[i]+rag_right
    texto=texto.center(num_of_letras*3+num_of_letras+1, "-")
    return texto

print(print_rangoli(5))