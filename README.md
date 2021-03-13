# krypto
# v1.0-beta

This proejct was created for the projects contest.

Version 0.8 was the latest version presented at the contest.

So it took first place then.


Полнофункциональное приложение для шифрования сообщений.
    Данное приложение сделано в качестве эксперимента, чтобы наглядно
    продемонстрировать действие различных криптографических машин для
    кодирования в упрощенном виде.

    Список версий и изменений:
    v0.1-alpha:
	 - В список шифруемых символов добавлена кириллица.
         - Добавлены messagebox, simpledialog из библиотеки Tkinter.
         - Реализовано диалоговое окно для ввода команд.
         - Реализовано диалоговое окно для ввода текста.
         - Реализована шифровка из кириллицы в присвоенный каждому символу код.
         Версия v0.1 закончена 29.12.19 в 18:25.

    v0.2-alpha:
	 - Реализовано удаление пробелов между отдельными буквами и вывод
           окончательной шифровки в виде единой строки, содержащей одно число.
         - Добавлены строчные буквы кириллицы.
         - Исправлен баг с невозможностью несколько раз подряд шифровать.
         Версия v0.2 закончена 30.12.19 в 19:44.

    v0.3-alpha:
	 - Реализован showerror при вводе неверной или несуществующей команды.
         Версия v0.3 закончена 31.12.19 в 19:54.

    v0.4-alpha:
 	 - Удалено управление при помощи команд.
         - Осуществлено управление при помощи кнопок.
         - Осуществлено сохранение только что произведенной
           шифровки в буфер обмена.
         - Реализован более удобный и красивый интерфейс программы.
         Версия v0.4 закончена 10.01.20 в 21:46.

    v0.5-alpha:
 	 - Реализована функция дешифровки сообщений.
           (Планируется реализовать расшифровку скопированного в буфер
            обмена сообщения, т.к. диалоговое окно не поддерживает функцию
            вставки строк, что ограничивает реализованный в настоящее время
            функционал, значительно усложняет и замедляет функцию дешифровки,
            а также это просто неудобно. Есть вариант замены диалогового окна
            askstring, но для этого придется переделывать всю программу в корне,
            что сразу отбрасывает мысль об использовании данной идеи.)
         - Изменена иконка приложения.
         - Добавлен латинский алфавит (заглавные и строчные буквы).
         Версия v0.5 закончена 11.01.20 в 21:26.

    v0.6-alpha:
 	 - Реализована функция мгновенной вставки скопированного в буфер обмена
           зашифрованного кода в дешифровщик.
         - В символы, допустимые к шифровке и последующей дешифровке допущен
           переход на новую строку, а также множество других символов (точка,
           вопросительный знак, знак вопроса, табуляция).
         Версия v0.6 закончена 12.01.20 в 4:20.

    v0.7-alpha:
 	 - Исправлен недочет с заглавными/строчными буквами (при расшифровке
           все буквы выводились капсом).
         - Добавлены новые символы.
         - Исправлены мелкие недочеты.
         Версия v0.7 закончена 12.01.20 в 19:52.

    v0.8-alpha:
 	 - Добавлена возможность самому ввести текст в дешифровщик при
           отсутствии какого-либо скопированного текста в буфере обмена.
         - Исправлены баги.
         Версия v0.8 закончена 12.01.20 в 20:18.

    v0.9-alpha:
	 - Возобновлена разработка приложения.
	 - Исправлено окно About - добавлена возможность прокручивать текст
	   посредством переписывания функции отображения диалогового окна
	   (создается новое окно с виджетом Text). При редактировании рядовым
	   пользователем каких-либо данных ничего не изменяется.
	 - Добавлено множество пояснений и комментариев к коду. Планируется
	   составление документации к функциям.
	 Версия v0.9 закончена 15.06.20 в 22:08.

    v0.9.1-alpha:
	 - Исправлены некоторые ошибки.
	 - Проведена подготовка к большому обновлению и выходу в стадию beta.
	 Версия v0.9.1-alpha закончена 16.06.20 в 15:48.

    v1.0-beta:
	 - Добавлена кнопка работы с файлами.
	 - Реализовано чтение файла, его последующая дешифровка/шифровка
	   и запись в отдельно созданный файл.
	 - Планируется добавить выбор имени для файла. Если имя не было
	   выбрано, то используется имя по умолчанию + номер файла.
	 - Планируется сделать более удобную работу с файловой системой.
	 - Были исправлены мелкие баги.
	 Версия v1.0-beta закончена 17.06.20 в 16:08.	 
--------------------------------------------------------------------------------------



    Главный разработчик (и единственный!) - Лукич.
