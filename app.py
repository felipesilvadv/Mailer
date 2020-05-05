from src.mailer import sendMail

sender = "ejemplo@gmail.com"
to = "ejemplo@mail.org"
asunto = "Prueba"
mensaje = "Hola te estoy mandando un email"
sendMail(sender, to, asunto, mensaje)
