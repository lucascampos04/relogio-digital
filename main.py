import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime('%H:%M:%S')
    label.config(text=time_string)
    label.after(1000, update_time)

# Cria a janela
window = tk.Tk()
window.title('Relógio Digital')

# Cria o rótulo para exibir o horário
label = tk.Label(window, font=('Arial', 80), bg='black', fg='white')
label.pack(padx=50, pady=50)

# Inicia a atualização do horário
update_time()

# Inicia o loop principal da janela
window.mainloop()
