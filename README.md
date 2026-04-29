##Exercícios referentes a aula do curso profissionalizante de machine learning - SCTEC. 

1. Limpeza de Dados (Data Cleaning)

Neste exercício, foi trabalhado um conjunto de dados contendo idades com inconsistências, como:

valores negativos
valores fora do intervalo esperado
dados textuais no lugar de números

O objetivo foi aplicar regras de tratamento para gerar uma nova lista contendo apenas dados válidos ou corrigidos.

Regras aplicadas:
Idades entre 18 e 100 → mantidas
Idades menores que 18 → rejeitadas com aviso
Idades negativas ou maiores que 100 → substituídas por um valor padrão (35)
Dados textuais → ignorados

Conceitos aplicados:
Estruturas condicionais (if/elif/else)
Laços de repetição (for)
Validação de tipos (isinstance)
Boas práticas em limpeza de dados

 2. Codificação de Variáveis Categóricas
 3. 
Este exercício simula um cenário comum em Machine Learning, onde dados categóricos precisam ser convertidos para valores numéricos.

A lista de imóveis (ex: "Casa", "Apartamento") foi transformada em uma representação numérica.

Mapeamento realizado:
"Casa" → 0
"Apartamento" → 1
"Sítio" → 2
Outros valores → -1 (outliers)

Também foi realizada a contagem de ocorrências da categoria "Casa".

Conceitos aplicados:

Label Encoding
Estruturas de decisão
Uso de listas e loops
Manipulação de strings

3. Simulação de Treinamento de Modelo

Neste exercício, foi implementada uma simulação simplificada do processo de treinamento de um modelo, baseada na redução progressiva do erro ao longo das épocas.

Funcionamento:
O erro inicial começa em 100.0
A cada época, o erro é reduzido com base em uma taxa de aprendizado
O treinamento continua até que o erro seja menor ou igual a 10.0

Durante o processo:

É exibido um alerta quando o erro entra na faixa entre 20 e 30 (ajuste fino)
Ao final, é exibido o número de épocas e o erro final

Conceitos aplicados:

Estrutura de repetição (while)
Simulação de aprendizado iterativo
Controle de fluxo
Conceito de Gradient Descent (Descida do Gradiente)
