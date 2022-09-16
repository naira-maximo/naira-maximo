import smtplib
from smtplib import SMTP # Importar o módulo smtplib
from email.message import EmailMessage
from email.utils import 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

de = "khaliapi@outlook.com"
para = "naira.maximo@hotmail.com"
titulo = "E-mail automático - Senha cadastrada para Avaliação 360°"
mensagem = EmailMessage(f"""
<p>Olá, usuário!</p>

<p>Aqui está sua senha gerada automaticamente, para acesso à plataforma de Avaliação 360°:</p>
<p>E-MAIL CADASTRADO:</p>
<p>SENHA:</p>

<p>*Sua senha é intrasferível, não compartilhe com ninguém.*</p>

<p>Não responda a este e-mail.</p>
""", 'html', 'utf-8')

mensagem['From'] = de
mensagem['To'] = ', '.join(para)
mensagem['Subject'] = titulo

s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login(de, "SenhaKhali10")
s.send_message(mensagem)
s.quit()
