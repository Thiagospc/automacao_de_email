# 1° parte

# mensagem de texto geral
from string import Template
from datetime import datetime

data_atual = datetime.now().strftime('%d/%m/%Y')

with open('prova_prova.html', 'r') as file:
    temp = Template(file.read())
    mensagem = temp.safe_substitute(nome='Thiago Santos Pinheiro Costa', data=data_atual)
# mensagem de texto geral

# 2° parte

# preparando arquivos e edestinatário
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# troque as informações
email_do_destinatario = 'email@gmail.com'
seu_email = 'email@gmail.com'
senha = '**********'

# definindo variável para armazenar informações que serão enviadas no email
msg = MIMEMultipart()

# destinatários
msg['from'] = 'Thiago'
msg['to'] = email_do_destinatario # cliente
msg['subject'] = 'seu_email para Thiago de Thiago'

texto = MIMEText(mensagem, 'html')
msg.attach(texto)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

# enviando e se conectando com o servidor
import smtplib as s

with s.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(seu_email, senha) # conta usada para enviar
    smtp.send_message(msg)

print("****************************")
print("EMAIL ENVIADO COM SUCESSO :)")
print("****************************")
