import smtplib
from email.message import EmailMessage
import time

def generar_email_aut(email,estado):
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        msg = EmailMessage()
        msg['From']='kashsantxl@gmail.com'
        msg['To']=email
        msg['Subject']='Cambio de estado de su caso'
        if estado==estado:
            print(estado) 
                   
        elif estado==1:
          cuerpo_email= f'Tu caso ha cambiado de estado: abierto, por favor verifica en la plataforma'
          msg.set_content(cuerpo_email)
        elif estado ==2:
          cuerpo_email= f'Tu caso ha cambiado de estado: proceso, por favor verifica en la plataforma'
          msg.set_content(cuerpo_email)
        elif estado == 3:
           cuerpo_email= f'Tu caso ha cambiado de estado: finalizado, por favor verifica en la plataforma'
           msg.set_content(cuerpo_email)
      
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('mamorales812@misena.edu.co','hhdwmlmkrbfpavov')
        server.send_message(msg)
        time.sleep(5)
        print('se envio correo')
        
            
        