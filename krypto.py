# Попытка импорта необходимых модулей для работы программы.
try:
    from tkinter import *
    from tkinter import messagebox, simpledialog, Tk
    from tkinter import scrolledtext
    from tkinter import filedialog as fd
    import os
    import re
    import encryption as encr
    import decryption as decr
    import read_file as rf
    import root as rt

except ModuleNotFoundError:
    print("Не найдены необходимые для работы модули.\n"
          + "Пожалуйста, прочитайте README.md для устранения ошибки.\n"
          + "Если предложенные вам решения не помогли,\nвы можете"
          + " обратиться к разработчику напрямую (контакты указаны в README.md).")


# Функция просмотра информации о проекте и авторе.
def about_tk():
    try:
        about_author = open('README.md', 'r')
    except FileNotFoundError:
        return "Не найден файл README.md"

    about_root = Tk()

    text = Text(about_root)
    text.pack(expand=YES, fill=BOTH)
    text.insert('2.0', about_author.read())

    scroll = Scrollbar(text, width=16, command=text.yview)
    scroll.pack(side=RIGHT, fill=Y)

    text['yscrollcommand'] = scroll.set

    about_root.title("About")
    about_root.geometry("700x500")
    about_root["bg"] = "#49423d"

    about_root.mainloop()


encryption_btn = Button(rt.root, text="Зашифровать", background="#555",
                        foreground="#ccc", padx="20", pady="8",
                        command=encr.get_message_for_encr)
decryption_btn = Button(rt.root, text="Расшифровать", background="#555",
                        foreground="#ccc", padx="17", pady="8",
                        command=decr.get_message_for_decr)
info_btn = Button(rt.root, text='About', background="#555",
                  foreground="#ccc", padx="42", pady="8",
                  command=about_tk)
read_file_btn = Button(rt.root, text='Считать файл', background='#555',
                       foreground='#ccc', padx='20', pady='8',
                       command=rf.read_file)
encryption_btn.pack()
decryption_btn.pack()
read_file_btn.pack()
info_btn.pack()

rt.root.mainloop()
