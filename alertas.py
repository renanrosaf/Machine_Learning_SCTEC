class CanalAlerta:
    def __init__(self,nome_destinatario):
        self.nome_destinatario=nome_destinatario
      
    def  enviar(self,mensagem):#Todo método de instância precisa receber self como primeiro parâmetro.
        raise NotImplementedError
# raise lança uma exceção, ou seja, interrompe a execução do código e sinaliza que algo errado aconteceu.
## Com raise — interrompe e exibe o erro