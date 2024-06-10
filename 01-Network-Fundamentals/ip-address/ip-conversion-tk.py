import tkinter as tk
from tkinter import messagebox

def convert():
    operation = operation_var.get()
    number = entry_number.get()
    result = ""

    if operation == "1":
        # Binário para Decimal
        try:
            result = int(number, 2)
        except ValueError:
            result = "Por favor, insira um número binário válido."
    elif operation == "2":
        # Decimal para Binário
        try:
            decimal_number = int(number)
            result = bin(decimal_number)[2:]
        except ValueError:
            result = "Por favor, insira um número decimal válido."
    else:
        result = "Selecione uma operação válida."

    label_result.config(text="Resultado: " + str(result))

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor Binário/Decimal")

# Widgets da interface
tk.Label(root, text="Escolha a operação:").pack()

operation_var = tk.StringVar(value="")
tk.Radiobutton(root, text="Conversão Binário para Decimal", variable=operation_var, value="1").pack()
tk.Radiobutton(root, text="Conversão Decimal para Binário", variable=operation_var, value="2").pack()

tk.Label(root, text="Insira o número:").pack()
entry_number = tk.Entry(root)
entry_number.pack()

tk.Button(root, text="Converter", command=convert).pack()

label_result = tk.Label(root, text="Resultado: ")
label_result.pack()

# Inicia o loop principal
root.mainloop()
