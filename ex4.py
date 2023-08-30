qtd = {}
vogais = 'aeiou'

texto = input('texto:').lower()

for i in texto: #percorre a string
    if i in vogais:
        if i not in qtd: #verifica se chava nõa existe no dicionario
            qtd[i]=1
        else:
            qtd[i]+=1 #depois de envontra a vogal soma 

print(qtd)


#conta caracter
qtd = {}
vogais = 'aeiou'

texto = input('texto:').lower()

for i in texto:
        if i not in qtd: #verifica se chava nõa existe no dicionario
            qtd[i]=1
        else:
            qtd[i]+=1 #depois de envontra a vogal soma 

print(qtd)