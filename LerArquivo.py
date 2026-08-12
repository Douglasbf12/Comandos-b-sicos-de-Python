import os

caminho_da_pasta = r"C:\Users\dougl\Desktop\Trabalho_sql\1-lh_nautical_csv"
# 1. Pega a lista com TODOS os arquivos da pasta
todos_os_arquivos = os.listdir(caminho_da_pasta)

# 2. O 'for' passa por arquivo por arquivo dessa lista:
for arquivo in todos_os_arquivos:
    
    # 3. O seu 'if' entra aqui testando um por um!
    if arquivo.endswith('.csv'):
        print(arquivo)
