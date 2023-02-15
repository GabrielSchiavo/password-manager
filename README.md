# Password Manager

<p align="left">
    <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge"/>
    <!-- <img src="https://img.shields.io/github/license/GabrielSchiavo/password-manager?color=blue&style=for-the-badge"/> -->
</p>

Gerenciador de senhas em Python3 com criptografia.

## :hammer: Funcionalidades do projeto
- `Cadastro de senhas:` é possível cadastrar o nome da conta, nome de usuário e senha. Todas as senhas são salvas no arquivo "passwords.txt".
- `Criptografia das senhas:` as senhas salvas no arquivo "passwords.txt" são todas criptografadas.
- `Senha Mestre:` só poderá acessar as senhas quem possuir a Senha Mestre.

## :file_folder: Acesso ao projeto
Você pode [acessar o código-fonte do projeto](https://github.com/GabrielSchiavo/password-manager) ou [baixá-lo](https://github.com/GabrielSchiavo/password-manager/archive/refs/heads/main.zip).

## 	:hammer_and_wrench: Abrir e rodar o projeto
Após baixar o projeto, você pode abrir com o Visual Studio Code. Para o projeto funcionar você deve ter configurado no seu PC:

* Python - Versão >=3.10.5

Agora, você deve executar em um terminal na pasta do projeto o seguinte comando para instalar a biblioteca Cryptography do Python:
```bash
pip install cryptography
```

Agora para iniciar o projeto execute este comando em um terminal na pasta do projeto:
```bash
python password-manager.py
```

<!-- ##### OBS: Senha Mestre padrão = 12345 -->

## :white_check_mark: Tecnologias utilizadas
* `Cryptography - 37.0.4`
* `Python - 3.10.5`

## :page_facing_up: Referências
* `Tech With Tim:` [YouTube](https://www.youtube.com/watch?v=DLn3jOsNRVE&list=WL&index=3&t=4667s)
* `Fernet (symmetric encryption):` https://cryptography.io/en/latest/fernet/
