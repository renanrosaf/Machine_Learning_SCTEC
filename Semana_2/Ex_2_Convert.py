imoveis=["Casa", "Apartamento", "Apartamento", "Sitio", "Casa", "Galpao","Casa", "Casa"]
contador_casas=imoveis.count("Casa") #contando o numero de casas
imoveis_codificados=[] #nova lista


for imovel in imoveis:
    
    if imovel=="Casa":  #adiciono 0 na lista no lugar de casa
        imoveis_codificados.append(0)
    elif imovel=="Apartamento": #adiciono 1 no lugar de apartamento
        imoveis_codificados.append(1)
    elif imovel=="Sitio": #Adiciono 2 no lugar de sitio
        imoveis_codificados.append(2)
    else: #qualquer outro tipo de imovel considero -1
        imoveis_codificados.append(-1)
        
    
print(f"{imoveis_codificados}")
print(f"Quantidade casas encontradas:{contador_casas}")