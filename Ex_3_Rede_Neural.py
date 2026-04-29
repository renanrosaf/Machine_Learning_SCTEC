erro_atual=100.0
taxa_aprendizado=5.5
epoca=1

while erro_atual>10:
    
    erro_atual-=taxa_aprendizado #erro atual diminuo da taxa de aprendizado a cada varredura de erro
    
    if erro_atual >=20 and erro_atual <=30:
        print(f"Atenção:Entrando na zona de ajuste fino na época {epoca}")
    epoca+=1 #nova epoca 
    
print(f"Treinamento concluido na época  {epoca} com erro final de {erro_atual} ")
