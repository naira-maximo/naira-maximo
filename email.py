from cadastroadm import email_lider, email_client
from string import Template
import smtplib # Importar o módulo smtplib
s = smtplib.SMTP(host='naira.maximo@hotmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)


# Função caso os e-mail sejam acessados pelo arquivo CSV
def read_template(nome_arq_csv):
    with open(nome_arq_csv, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# Função caso os e-mail sejam resgatados diretamente da Entry
listcontacts = [email_lider, email_client]

# Função para ler os contatos cadastrados na caixa de entrada
# e vincular com uma senha gerada automaticamente
def get_contacts(listcontacts):
    lider = email_lider
    client = email_client
    with open(listcontacts, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            lider.append(a_contact + senha_gerada)
            client.append(a_contact + senha_gerada)
    return lider, client
