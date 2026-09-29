import pyautogui
import time
import pandas as pd

# Configuração de pausa padrão entre comandos do pyautogui
pyautogui.PAUSE = 0.3

# =========================================================================
# Passo 1: Entrar no sistema da empresa 
# =========================================================================
# Abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

# Tempo para o navegador abrir
time.sleep(3)

# Digitar o link do sistema e acessar
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Tempo essencial para a página carregar por completo
time.sleep(5)


# Passo 2: Fazer login
# 1. Dá um clique na tela para ativar a janela do navegador 
pyautogui.click(x=424, y=372)

# 2. Digita o e-mail diretamente no campo focado
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") 

# 3. Digita a senha no próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("esc")
time.sleep(4)

# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4 e 5: Cadastrar os produtos em repetição
for linha in tabela.index:
    # Clicar no primeiro campo (Código do produto) para iniciar o formulário
    pyautogui.click(x=433, y=264)
    
    # Extrair os dados da linha atual da tabela
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
    
    # Preencher cada campo navegando com a tecla TAB
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    # Verifica se o campo de observação não está vazio antes de digitar
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    # Pressionar ENTER para enviar/cadastrar o produto atual
    pyautogui.press("enter") 
    
    # Dar scroll tudo para cima para o próximo produto não errar a posição
    pyautogui.scroll(5000)
    time.sleep(1)

