import win32com.client as win32  # Biblioteca que possibilita a interagração com o e-mail

# Criar interação com outlook
outlook = win32.Dispatch('outlook.application')

# Criar um e-mail
email = outlook.CreateItem(0)

# Configuraras informações do seu e-mail
enviar1 = email.To
assunto1 = email.Subject
corpo1 = email.HTMLBody

email.To = 'ngpmaximo@gmail.com'
email.Subject = 'E-mail automático - Senha cadastrada para Avaliação 360°'
email.HTMLBody = f"""
<p>Olá, usuário!</p>

<p>Aqui está sua senha gerada automaticamente, para acesso à plataforma de Avaliação 360°:</p>
<p>E-MAIL CADASTRADO:</p>
<p>SENHA:</p>

<p>*Sua senha é intrasferível, não compartilhe com ninguém.*</p>

<p>Não responda a este e-mail.</p>
"""

email.Send()
print("E-mail Enviado")