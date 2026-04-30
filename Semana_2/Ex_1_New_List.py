idades_brutas=[25,42,-5,105,"Trinta",34,15,-12,45,99] #coluna com dados brutos
idades_limpas=[] #nova lista a ser preenchida

#realizar o tratamento de idade das idades brtas
for idade in idades_brutas:
    
    if isinstance(idade,str): #Se a idade for string: rejeita o dado
        print("Dado inválido")
        continue

    if  idade >=18 and idade <=100: #Criando nova lista, com idade entre 18 e 100 anos
        idades_limpas.append(idade)
    
    elif idade <0 or idade > 100: #Substituindo diade invalidas por 35
        print(f"Idade {idade} inválida. Substitua pe idade médida: 35 anos")
        idades_limpas.append(35)
        
    elif idade >=0 and idade <=18: #Rejeitado idades menores de 18 anos
        print(f"Idade {idade} idade rejeitada: Menor de idade ")


print(f"Nova lista: {idades_limpas}")