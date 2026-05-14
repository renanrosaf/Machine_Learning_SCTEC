class CanalAlerta:
    def __init__(self,nome_destinatario):
        self.nome_destinatario=nome_destinatario
      
    def  enviar(self,mensagem):#Todo método de instância precisa receber self como primeiro parâmetro.
        raise NotImplementedError
# raise lança uma exceção, ou seja, interrompe a execução do código e sinaliza que algo errado aconteceu.
## Com raise — interrompe e exibe o erro

#Classe Alerta Email criada:
class AlertaEmail(CanalAlerta):
    def enviar(self,mensagem):
        print("Email enviado com sucesso")
#Classe Alerta SMS criada
class AlertaSMS(CanalAlerta):
    def enviar(self,mensagem):
        print("SMS enviado com sucesso")

class AlertaWhattsApp(CanalAlerta):
    def enviar(self,mensagem):
        print("Mensagem enviada ao WhattsApp com sucesso")

def disparar_alerta_geral(canal,mensagem):
    #A função  recebe o canal pronto como parâmetro, então é só chamar o método nele
    canal.enviar(mensagem)

