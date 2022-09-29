import smtplib 

smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
smtp.login("projetokhali.api@gmail.com","fwhwscuvoeztzeeo")
smtp.sendmail("projetokhali.api@gmail.com", "ngpmaximo@gmail.com", "Email automático Senha cadastrada para Avaliação 360")

smtp.quit() 
print ("Email sent successfully!") 
