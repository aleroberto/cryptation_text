# Criptografia Vigenère
Implementação de criptografia usando palavra definida pelo usuário para criptografar ou descriptografar um texto.

## Descrição

Essa técnica para criptografia realiza uma substituição usando uma série de diferentes "cifras de César" usando as letras de uma palavra-chave. 

## Funcionalidades

- Criptografar texto usando uma chave fornecida pelo usuário.
- Descriptografar texto criptografado usando a mesma chave.
- Aceita texto com espaços.

## Como Usar

1. Clone este repositório:
```
   git clone https://github.com/aleroberto/cryptation_text.git
   cd cryptation_text
```

2. Execute o script:
```
   python vigenere.py
```

3. Siga as instruções fornecedidas pelo programa na linha de comando:
```
   - Insira a chave que desejar para ser utilizada na criptografia.
   - Escolha se deseja criptografar ou descriptografar o texto.
   - Digite o texto a ser processado.
```
## Exemplo

Para criptografar a palavra "BRASIL PENTA CAMPEÃO MUNDIAL" com a chave "ESSE PROJETO É TOP":
```
Forneça a chave: ESSE PROJETO É INCRIVEL
Digite o texto a ser criptografado: BRASIL PENTA CAMPEÃO MUNDIAL
Texto retornado: FJSWBAGSWXTQTSIMNQDCIHTED
```

Para descriptografar o texto criptografado:
```
Forneça a chave: ESSE PROJETO É INCRIVEL
Digite o texto a ser descriptografado: FJSWBAGSWXTQTSIMNQDCIHTED
Texto retornado: BRASIL PENTA CAMPEÃO MUNDIAL
```

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa é necessária.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Faça um fork deste repositório, faça suas alterações e envie um pull request.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.
