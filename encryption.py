# Попытка импорта необходимых модулей для работы программы.
try:
    from tkinter import *
    from tkinter import messagebox, simpledialog, Tk
    from tkinter import scrolledtext
    from tkinter import filedialog as fd
    import os
    import re
    import dict as dc
    import root as rt

except ModuleNotFoundError:
    print("Не найдены необходимые для работы модули.\n"
          + "Пожалуйста, прочитайте README.md для устранения ошибки.\n"
          + "Если предложенные вам решения не помогли,\nвы можете"
          + " обратиться к разработчику напрямую (контакты указаны в README.md).")


# Функция для шифрования передаваемых сообщений.
def encryption(message):
    encryption_2 = []
    encryption_1 = list(message)
    len_of_message = len(encryption_1)

    for i in range(0, len_of_message):
        if encryption_1[i] in dc.k_words:
            encrypt_word = dc.k_words.get(encryption_1[i])
            encryption_2.append(encrypt_word)
        i += 1
    end_of_encryption = ''.join(encryption_2)
    return end_of_encryption.replace(" ", "")
    del encryption_1
    del encryption_2
    del end_of_encryption
    del encrypt_word


# Функция, вызываемая для получения зашифрованного сообщения.
def get_message_for_encr() -> str:
    message = simpledialog.askstring('. . .', 'Вводите... ')
    messagebox.showinfo('Шифровка', encryption(message))
    write(encryption(message))
    return message


# Функция нахождения ключа для символа во встроенном словаре.
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


# Функция записи сообщения в буфер обмена.
def write(e):
    rt.root.clipboard_clear()
    rt.root.clipboard_append(e)


# Функция считывания зашифрованного сообщения в буфер обмена.
def read(e):
    encrypt_for_decrypt = rt.root.clipboard_get()
    return encrypt_for_decrypt



