import tkinter as tk
import main

root = tk.Tk()


def validador_cpf(stringvar: tk.StringVar, button: tk.Button):
    cpf = stringvar.get()

    if main.is_valid(cpf):
        button.config(
            text='OK', activeforeground='green', foreground='green'
        )
    else:
        button.config(
            text='Inválido', activeforeground='red', foreground='red'
        )


def generator_cpf(stringvar: tk.StringVar, button: tk.Button):
    cpf = main.generator()
    cpf_formatado = main.formater(cpf)
    stringvar.set(cpf_formatado)


main_title = tk.Label(
    root,
    text='Gerador/Validador de CPF',
    bg='#fff',
    font=('Helvetica', 12, 'bold')
)
main_title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

validador_label = tk.Label(root, text='Validar:', bg='#fff',)
validador_label.grid(row=1, column=0)

validador_stringvar = tk.StringVar()
validador_entry = tk.Entry(
    root,
    bd=5,
    relief='flat',
    textvariable=validador_stringvar
)
validador_entry.grid(row=1, column=1, pady=10)

validador_button = tk.Button(root, text='Validar')
validador_button.grid(row=1, column=2, sticky='we')
validador_button.configure(command=lambda: validador_cpf(
    validador_stringvar, validador_button
))

validador_label = tk.Label(root, text='Gerar:', bg='#fff',)
validador_label.grid(row=2, column=0)

gerador_stringvar = tk.StringVar()
gerador_entry = tk.Entry(
    root,
    bd=5,
    relief='flat',
    textvariable=gerador_stringvar
)
gerador_entry.grid(row=2, column=1, pady=10)

gerador_button = tk.Button(root, text='Gerar')
gerador_button.grid(row=2, column=2, sticky='we')
gerador_button.configure(command=lambda: main.gerador(
    gerador_stringvar, validador_button
))


root.title('Gerador/Validador de CPF')
root.config(background='#fff', padx=20, pady=20)
root.mainloop()
