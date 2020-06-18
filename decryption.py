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


# Функция дешифровки сообщений.
def decryption(message):
    decryption_2 = []
    decryption_3 = re.findall(r'\d\d\d\d\d\d', message)
    len_of_message_1 = len(decryption_3)

    for i in range(0, len_of_message_1):
        decrypt_word = get_key(dc.k_words, decryption_3[i])
        decryption_2.append(decrypt_word)
        i += 1
    end_of_decryption = ''.join(decryption_2)
    return end_of_decryption
    del decryption_1
    del decryption_2
    del decryption_3
    del decrypt_word
    del end_of_decryption


# Функция, вызываемая для получения расшифрованного сообщения.
def get_message_for_decr() -> str:
    try:
        encrypt_for_decrypt = ''
        message = read(encrypt_for_decrypt)
        messagebox.showinfo('Расшифровка', decryption(message))
        write(decryption(message))

    except TclError:
        message = simpledialog.askstring('. . .', 'Вводите...')
        messagebox.showinfo('Расшифровка', decryption(message))
        write(decryption(message))


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





