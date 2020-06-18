# Попытка импорта необходимых модулей для работы программы.
try:
    from tkinter import *
    from tkinter import messagebox, simpledialog, Tk

except ModuleNotFoundError:
    print("Не найдены необходимые для работы модули.\n"
          + "Пожалуйста, прочитайте README.md для устранения ошибки.\n"
          + "Если предложенные вам решения не помогли,\nвы можете"
          + " обратиться к разработчику напрямую (контакты указаны в README.md).")


version = open("README.md")
while True:
    line = version.readline()
    if "v" in line:
        version = line
        break
    else:
        continue


# Главный цикл программы.
root = Tk()

root.title("Krypto " + version)
root.geometry("300x250")
try:
    root.iconbitmap('sunnamed.ico')
except TclError:
    pass
root["bg"] = "#49423d"
