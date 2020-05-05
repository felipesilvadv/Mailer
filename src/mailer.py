# Modulo encargado de mandar mails a los vendedores

testing_module = __name__ == "__main__"
if testing_module:
    from mandar import SendMessage, CreateMessage
    from quickstart import setupService
else:
    from .mandar import SendMessage, CreateMessage
    from .quickstart import setupService


def sendMail(destinatario, asunto, mensaje):
    service, sender = setupService()
    msg = CreateMessage(sender, destinatario, asunto, mensaje)
    SendMessage(service, "me", msg)
