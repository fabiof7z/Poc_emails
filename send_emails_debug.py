import pandas as pd

print("Iniciando")

# Lê a planilha
try:
    df = pd.read_excel('lista_emails.xlsx')
    print("Planilha lida com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro ao ler a planilha: {e}")

# Itera sobre as linhas do DataFrame e imprime os dados
print("Iniciando iteração sobre os dados:")
for index, row in df.iterrows():
    print(f"Iteração {index}:")
    print(f"Email: {row['Email']}, Mensagem: {row['Mensagem']}")
