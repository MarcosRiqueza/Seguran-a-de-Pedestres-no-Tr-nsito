import tkinter as tk
import pyttsx3
import time


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Segurança no Trânsito para Crianças,deficientes visuais acompanhados e idosos")

        self.label = tk.Label(root, text="Clique no botão para começar a travessia de rua")
        self.label.pack(pady=10)

        self.button = tk.Button(root, text="Iniciar Simulação", command=self.iniciar_simulacao)
        self.button.pack(pady=5)

        self.textbox = tk.Text(root, height=8, width=50)
        self.textbox.pack(pady=10)

        self.engine = pyttsx3.init()

    def iniciar_simulacao(self):
        self.textbox.delete("1.0", tk.END)
        self.label.config(text="Aguarde...")

        # Instruções de segurança
        self.textbox.insert(tk.END, "Olhe para o lado esquerdo da rua...\n")
        self.engine.say("Olhe para o lado esquerdo da rua")
        self.engine.runAndWait()
        time.sleep(3)

        self.textbox.insert(tk.END, "Olhe para o lado direito da rua...\n")
        self.engine.say("Olhe para o lado direito da rua")
        self.engine.runAndWait()
        time.sleep(3)

        self.textbox.insert(tk.END, "Espere pelo sinal verde e atravesse pela faixa de pedestres, se disponível.\n")
        self.engine.say("Espere pelo sinal verde e atravesse pela faixa de pedestres, se disponível")
        self.engine.runAndWait()

        time.sleep(3)  # Dá um pequeno tempo antes da última instrução

        self.textbox.insert(tk.END, "Parabéns, você está seguro agora.\n")
        self.engine.say("Parabéns, você está seguro agora")
        self.engine.runAndWait()

        self.label.config(text="Clique no botão para começar a travessia de rua novamente")


# Criar e iniciar a aplicação
root = tk.Tk()
app = App(root)
root.mainloop()
