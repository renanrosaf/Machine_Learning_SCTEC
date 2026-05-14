#Função que retorne o cracha do funcionário: Nome, Idade e Cargo
def gerar_cracha(nome, idade, cargo):
    #A função deve retornar um crachá em formato de string
    print(f"Crachá:{nome},{idade} anos-{cargo}")
   
#gerar_cracha(nome="Renan",idade=30,cargo="Engenheiro de Machine Learning") - Forma 1

#Forma 2:
registro=0
while registro==0:

    nome_cracha=(input("Insira o nome do funcionário:"))
    id_cracha=int(input("Insira a idade do funcionário:"))
    cargo_cracha=(input("Insira o cargo do funcionário:"))
    gerar_cracha(nome=nome_cracha,idade=id_cracha,cargo=cargo_cracha)

    registro=int(input("Você quer registrar o cracha de outro funcionário? 1- Não e 0- Sim:"))
    
print('O registro do crachá dos funcionários foi encerrado')