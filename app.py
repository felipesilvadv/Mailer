from src.mailer import sendMail

to = "example@example.org, otherexample@example.org"
asunto = "Prueba"
mensaje = "Hola te estoy mandando un email"
sendMail(to, asunto, mensaje)
