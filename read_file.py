# Попытка импорта необходимых модулей для работы программы.
try:
    from tkinter import *
    from tkinter import messagebox, simpledialog, Tk
    from tkinter import scrolledtext
    from tkinter import filedialog as fd
    import os
    import re
    import decryption as decr
    import encryption as encr
    import dict
    import root as rt

except ModuleNotFoundError:
    print("Не найдены необходимые для работы модули.\n"
          + "Пожалуйста, прочитайте README.md для устранения ошибки.\n"
          + "Если предложенные вам решения не помогли,\nвы можете"
          + " обратиться к разработчику напрямую (контакты указаны в README.md).")


def read_file():
    file = fd.askopenfilename()

    try:
        file_name = open(file, "r")
        _file = True
    except FileNotFoundError:
        messagebox.showinfo("Ошибка", "Не выбран файл")
        return
    readed_file = file_name.read()

    if _file:
        enc_or_decr = messagebox.askquestion('Действие', 'Вы хотите зашифровать?')

        if enc_or_decr == 'yes':
            messagebox.showinfo("Шифровка", encr.encryption(readed_file))
            write(encr.encryption(readed_file))
            number_of_encr = 0
            while True:
                if os.path.exists("ENCR" + str(number_of_encr) + ".txt"):
                    number_of_encr += 1
                else:
                    break
            with open("ENCR" + str(number_of_encr) + ".txt", 'w') as encr_filename:
                encr_filename.write(encr.encryption(readed_file))
                messagebox.showinfo("Внимание", "Шифровка файла была сохранена в файл под названием "
                                    + encr_filename.name)
        else:
            enc_or_decr1 = messagebox.askquestion("Действие", "Вы хотите дешифровать?")
            if enc_or_decr1 == 'yes':
                messagebox.showinfo("Расшифровка", decr.decryption(readed_file))
                write(decr.decryption(readed_file))
                number_of_decr = 0
                while True:
                    if os.path.exists("DECR" + str(number_of_decr) + ".txt"):
                        number_of_decr += 1
                    else:
                        break
                with open("DECR" + str(number_of_decr) + ".txt", "w") as decr_filename:
                    decr_filename.write(decr.decryption(readed_file))
                    messagebox.showinfo("Внимание", "Дешифровка файла была сохранены в файл под названием "
                                        + decr_filename.name)


# Функция записи сообщения в буфер обмена.
def write(e):
    rt.root.clipboard_clear()
    rt.root.clipboard_append(e)


# Функция считывания зашифрованного сообщения в буфер обмена.
def read(e):
    encrypt_for_decrypt = rt.root.clipboard_get()
    return encrypt_for_decrypt

