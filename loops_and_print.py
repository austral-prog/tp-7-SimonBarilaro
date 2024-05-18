def enumerate_list(list):
    indice=0
    nuevo_indice = 0
    milista=[]
    while indice<len(list):
        elemento = list[indice]
        if elemento:
            palabra=f"{nuevo_indice}. {elemento}"
            milista.append(palabra)
            nuevo_indice += 1
        indice+=1
    return milista


def enumerate_backwards(list):
    indice=0
    nuevo_indice = 0
    milista=[]
    while indice<len(list):
        elemento = list[indice]
        if elemento:
            palabra=f"{nuevo_indice}. {elemento[::-1]}"
            milista.append(palabra)
            nuevo_indice += 1
        indice+=1
    return milista
