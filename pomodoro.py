import tkinter as tk
from tkinter import messagebox
import time

# Configurações do Pomodoro
tempo_trabalho = 25 * 60  # 25 minutos de trabalho
tempo_descanso_curto = 5 * 60  # 5 minutos de pausa curta
tempo_descanso_longo = 15 * 60  # 15 minutos de pausa longa

# Função para atualizar o temporizador
def atualizar_temporizador(tempo_restante):
    minutos, segundos = divmod(tempo_restante, 60)
    tempo_label.config(text=f"{minutos:02}:{segundos:02}")
    janela.after(1000, atualizar_temporizador, tempo_restante - 1)
    if tempo_restante == 0:
        finalizar_pomodoro()

# Função para iniciar um Pomodoro
def iniciar_pomodoro():
    global tempo_atual, estado_atual
    if estado_atual == "Trabalho":
        tempo_atual = tempo_trabalho
    elif estado_atual == "Pausa Curta":
        tempo_atual = tempo_descanso_curto
    else:
        tempo_atual = tempo_descanso_longo
    atualizar_temporizador(tempo_atual)
    estado_atual = "Trabalho" if estado_atual != "Trabalho" else "Pausa Curta"
    iniciar_button.config(state=tk.DISABLED)
    parar_button.config(state=tk.NORMAL)

# Função para finalizar um Pomodoro
def finalizar_pomodoro():
    messagebox.showinfo("Pomodoro", f"Tempo para {estado_atual} terminou!")
    iniciar_button.config(state=tk.NORMAL)
    parar_button.config(state=tk.DISABLED)

# Configuração da janela
janela = tk.Tk()
janela.title("Pomodoro")
janela.geometry("300x200")

# Configuração da interface
tempo_label = tk.Label(janela, text="", font=("Arial", 40))
tempo_label.pack(pady=10)
iniciar_button = tk.Button(janela, text="Iniciar", command=iniciar_pomodoro)
iniciar_button.pack()
parar_button = tk.Button(janela, text="Parar", command=finalizar_pomodoro, state=tk.DISABLED)
parar_button.pack()

# Variáveis globais
tempo_atual = tempo_trabalho
estado_atual = "Trabalho"

janela.mainloop()
