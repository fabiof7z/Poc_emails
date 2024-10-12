import pandas as pd
import smtplib
from email.mime.text import MIMEText

print("iniciando")
# Lê a planilha
try:
    df = pd.read_excel('lista_emails.xlsx')
    print("planilha lida")
except Exception as e:
    print(f"An error occurred while reading the Excel file: {e}")

# Configurações do servidor de e-mail
smtp_server = 'postfix-server'
smtp_port = 25

# Enviar e-mails
try:
    print("pre-iteracao")
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        print(f"Conectando ao servidor SMTP {smtp_server} na porta {smtp_port}...")
        for index, row in df.iterrows():
            print("iterando")
            msg = MIMEText(row['Mensagem'])
            msg['Subject'] = 'Poc Nova divida'
            msg['From'] = 'seu-email@localdomain'
            msg['To'] = row['Email']

            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            print(f"E-mail enviado para {row['Email']}")
except Exception as e:
    print(f"An error occurred during email sending: {e}")
