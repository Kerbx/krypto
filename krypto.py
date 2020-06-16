# Попытка импорта необходимых модулей для работы программы.
try:
    from tkinter import *
    from tkinter import messagebox, simpledialog, Tk
    from tkinter import scrolledtext
    import re

except ModuleNotFoundError:
    print("Не найдены необходимые для работы модули.\n"
          + "Пожалуйста, прочитайте README.md для устранения ошибки.\n"
          + "Если предложенные вам решения не помогли,\nвы можете"
          + " обратиться к разработчику напрямую (контакты указаны в README.md).")

version = 'v0.9'


# Встроенный словарь с ключами к символам для шифровки/дешифровки.
k_words = {" ": '838599',   "\n": '918616',
           ".": '919838',   "\t": '912499',
           "!": '159902',   "\'": '012371',
           "@": '912452',   "\"": '217384',
           "#": '812455',   "(":  '527321',
           ")": '524667',   "*":  '568732',
           "&": '362596',   "?":  '893763',
           "%": '385235',   "^":  '364896',
           "№": '475238',   "$":  '765264',
           ";": '756824',   ",":  '937592',
           "/": '284602',   "\\":  '582645',
           "<": '467235',   ">":  '783785',
           "-": '764863',   "_":  '238592',
           "+": '923586',   "=":  '235977',
           "{": '825301',   "}":  '627689',
           "[": '127465',   "]":  '827207',
           "~": '852630',   "`":  '825491',

           "А": '982624',   "а": '902624',
           "Б": '249159',   "б": '259159',
           "В": '435483',   "в": '465483',
           "Г": '549284',   "г": '599284',
           "Д": '872288',   "д": '832288',
           "Е": '257509',   "е": '237509',
           "Ж": '090534',   "ж": '080534',
           "З": '301040',   "з": '381040',
           "И": '734697',   "и": '764697',
           "Й": '844838',   "й": '874838',
           "К": '781437',   "к": '781137',
           "Л": '492698',   "л": '462698',
           "М": '516587',   "м": '586587',
           "Н": '522278',   "н": '552278',
           "О": '045372',   "о": '065372',
           "П": '608717',   "п": '688717',
           "Р": '244390',   "р": '274390',
           "С": '638017',   "с": '678017',
           "Т": '249300',   "т": '299300',
           "У": '690483',   "у": '600483',
           "Ф": '311700',   "ф": '351700',
           "Х": '951946',   "х": '961946',
           "Ц": '422669',   "ц": '452669',
           "Ч": '009442',   "ч": '029442',
           "Ш": '431104',   "ш": '471104',
           "Щ": '746937',   "щ": '748937',
           "Ь": '847783',   "ь": '837783',
           "Ы": '726133',   "ы": '746133',
           "Ъ": '916625',   "ъ": '906625',
           "Э": '302488',   "э": '322488',
           "Ю": '196119',   "ю": '156119',
           "Я": '885662',   "я": '825662',

           "A": "972620",   "a": "952620",
           "B": "567922",   "b": "577922",
           "C": "650224",   "c": "690224",
           "D": "070694",   "d": "080694",
           "E": "081102",   "e": "021102",
           "F": "504875",   "f": "594875",
           "G": "961103",   "g": "951103",
           "H": "994224",   "h": "964224",
           "I": "142750",   "i": "132750",
           "J": "667244",   "j": "617244",
           "K": "875482",   "k": "815482",
           "L": "137847",   "l": "157847",
           "P": "027236",   "p": "007236",
           "R": "912731",   "r": "902731",
           "T": "480616",   "t": "470616",
           "Y": "863729",   "y": "843729",
           "U": "451539",   "u": "431539",
           "O": "735003",   "o": "795003",
           "V": "822887",   "v": "892887",
           "N": "300228",   "n": "310228",
           "M": "170171",   "m": "140171",
           "S": "351061",   "s": "381061",
           "Q": "360420",   "q": "320420",
           "W": "548449",   "w": "508449",
           "Z": "329741",   "z": "359741",
           "X": "583630",   "x": "533630",

           "1": '249671',   "2": '528118',
           "3": '509287',   "4": '123957',
           "5": '971161',   "6": '019626',
           "7": '193672',   "8": '192582',
           "9": '982461',   "0": '828135', }


# Функция записи сообщения в буфер обмена.
def write(e):
    root.clipboard_clear()
    root.clipboard_append(e)


# Функция считывания зашифрованного сообщения в буфер обмена.
def read(e):
    encrypt_for_decrypt = root.clipboard_get()
    return encrypt_for_decrypt


# Функция для шифрования передаваемых сообщений.
def encryption(message):
    encryption_2 = []
    encryption_1 = list(message)
    len_of_message = len(encryption_1)

    for i in range(0, len_of_message):
        if encryption_1[i] in k_words:
            encrypt_word = k_words.get(encryption_1[i])
            encryption_2.append(encrypt_word)
        i += 1
    end_of_encryption = ''.join(encryption_2)
    return end_of_encryption.replace(" ", "")
    del encryption_1
    del encryption_2
    del end_of_encryption
    del encrypt_word


# Функция нахождения ключа для символа во встроенном словаре.
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


# Функция дешифровки сообщений.
def decryption(message):
    decryption_2 = []
    decryption_1 = list(message)
    decryption_3 = re.findall(r'\d\d\d\d\d\d', message)
    len_of_message_1 = len(decryption_3)

    for i in range(0, len_of_message_1):
        decrypt_word = get_key(k_words, decryption_3[i])
        decryption_2.append(decrypt_word)
        i += 1
    end_of_decryption = ''.join(decryption_2)
    return end_of_decryption
    del decryption_1
    del decryption_2
    del decryption_3
    del decrypt_word
    del end_of_decryption


# Функция, вызываемая для получения зашифрованного сообщения.
def get_message_for_encr() -> str:
    message = simpledialog.askstring('. . .', 'Вводите... ')
    messagebox.showinfo('Шифровка', encryption(message))
    write(encryption(message))
    return message


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


# Функция просмотра информации о проекте и авторе.
def about_tk():
    about_author = open('README.md', 'r')
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


# Главный цикл программы.
root = Tk()

root.title("Krypto " + version)
root.geometry("300x250")
try:
    root.iconbitmap('sunnamed.ico')
except TclError:
    pass
root["bg"] = "#49423d"

encryption_btn = Button(root, text="Зашифровать", background="#555",
                        foreground="#ccc", padx="20", pady="8",
                        command=get_message_for_encr)
decryption_btn = Button(root, text="Расшифровать", background="#555",
                        foreground="#ccc", padx="17", pady="8",
                        command=get_message_for_decr)
info_btn = Button(root, text='About', background="#555",
                  foreground="#ccc", padx="42", pady="8",
                  command=about_tk)

encryption_btn.pack()
decryption_btn.pack()
info_btn.pack()

root.mainloop()
