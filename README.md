# Automação de Cadastro de Produtos com Python

Este é um projeto de automação robótica de processos (RPA) desenvolvido em Python utilizando a biblioteca **PyAutoGUI**. O objetivo do script é realizar o login automatizado em um sistema empresarial web e cadastrar em massa uma lista de produtos extraída de um arquivo `.csv` utilizando a biblioteca **Pandas**.

---

# Funcionalidades

- **Abertura automática** do navegador Google Chrome.
- **Login automatizado** no sistema por meio de comandos de teclado/mouse simulados.
- **Preenchimento inteligente** de formulários com tratamento para campos opcionais (ex: observações).
- **Cadastro em massa** em alta velocidade com navegação estruturada via teclado (`TAB` e `ENTER`).

---

# Tecnologias e Bibliotecas Utilizadas

- **[Python](https://python.org)** (Linguagem base)
- **[PyAutoGUI](https://readthedocs.io)** (Controle do mouse e teclado)
- **[Pandas](https://pydata.org)** (Manipulação e leitura da base de dados `.csv`)
- **[Time](https://python.org)** (Gerenciamento de pausas e sincronização)

---

# Pré-requisitos e Instalação

Antes de rodar o script, certifique-se de ter o Python instalado em sua máquina e as bibliotecas necessárias.

1. Clone este repositório ou baixe os arquivos do projeto.
2. Abra o terminal na pasta do projeto e instale as dependências executando:

```bash
pip install pyautogui pandas opencv-python
```

3. Certifique-se de que o arquivo **`produtos.csv`** está presente no mesmo diretório do script principal.

---

# Como Executar o Projeto

1. Abra o arquivo principal do script no seu editor ou terminal.
2. Certifique-se de que sua tela principal não possui janelas cobrindo a área de execução do navegador.
3. Execute o script Python:

```bash
python seu_script.py
```

4. **Importante:** Não mexa no mouse ou no teclado enquanto o robô estiver em execução para evitar que ele clique ou digite fora do navegador.

---

# Observações de Configuração (Calibração)

Como o **PyAutoGUI** interage diretamente com a interface gráfica, algumas variáveis podem precisar de ajuste dependendo do seu monitor:
- **Resolução da Tela:** Caso o primeiro clique do formulário ou o clique no campo de e-mail falhem, ajuste as coordenadas `x` e `y` nas funções `pyautogui.click()` utilizando um script auxiliar com `pyautogui.position()`.
- **Aviso de Senhas do Chrome:** Se o navegador exibir pop-ups de segurança sobre vazamento de senhas, o script está configurado para pressionar a tecla `ESC` para fechá-lo automaticamente antes do cadastro de produtos.

---
Desenvolvido como parte do Intensivão de Python
