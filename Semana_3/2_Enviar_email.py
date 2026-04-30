#2- Função chama enviar_email e que recebe dois parametros padrão

def enviar_email(destinatario, assunto="Sem Assunto"):
    
    print(f"Enviando e-mail para {destinatario} com o assunto: {assunto}")
    
enviar_email("teste@email.com")
enviar_email("re.r.ferreira@email.com","Código em anexo")