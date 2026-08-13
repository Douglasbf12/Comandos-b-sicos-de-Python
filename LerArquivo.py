import os
import csv

caminho_da_pasta = r"C:\Users\dougl\Desktop\Trabalho_sql\1-lh_nautical_csv"
# A letra "r" serve para ler as barras invertidas como texto.

# Pega a lista com TODOS os arquivos da pasta
todos_os_arquivos = os.listdir(caminho_da_pasta)
# O os.listdir() vai até a pasta configurada e pega uma lista com os 
# nomes de tudo o que está lá dentro (arquivos, pastas, etc.) e guarda na variável todos_os_arquivos.

# O 'for' passa por arquivo por arquivo dessa lista:
for arquivo in todos_os_arquivos:
    
    # 3. O seu 'if' entra aqui testando um por um!
    if arquivo.endswith('.csv'):
    #Testa se o nome do arquivo da vez termina com a extensão .csv. 
    #Se sim, ele deixa entrar e executar o bloco interno. Se for outro tipo de arquivo, ele ignora.
        caminho_completo = os.path.join(caminho_da_pasta, arquivo)
    #Junta o endereço da pasta com o nome do arquivo da vez (ex: 
    #C:\...\1-lh_nautical_csv + orders.csv = 
    #C:\...\1-lh_nautical_csv\orders.csv). Isso garante que o Python ache o arquivo sem erros.
        with open(caminho_completo, mode="r", encoding="utf-8") as f:
    #encoding="utf-8": Garante a leitura correta de ç, acentos e caracteres especiais.
    #as f: Dá o apelido temporário f para esse arquivo aberto.
         leitor = csv.reader(f) 
    #csv.reader(f): Prepara o leitor para entender o conteúdo do arquivo f como uma tabela CSV.
         colunas = next(leitor)
    #next(leitor): Lê apenas a primeira linha do arquivo (que contém o nome das colunas) e salva essa lista dentro da variável colunas.
         print(f"Tabela: {arquivo}")
         print(f"Colunas: {colunas}\n")
    #O \n serve para pular uma linha em branco no final, deixando o resultado organizado e fácil de ler no terminal.