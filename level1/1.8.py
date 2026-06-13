"""
Легенда
На першій лекції з кібербезпеки викладач розповів про шифр Цезаря — найпростіший шифр підстановки, де кожна літера зсувається на фіксовану кількість позицій в алфавіті. «Зламати його може навіть першокурсник!» — сказав він. Студентка Марія вирішила довести це на практиці й написати одразу і шифратор, і дешифратор.
Шифруються лише латинські літери (регістр зберігається), всі інші символи залишаються без змін.
Вхідні дані
Перший рядок містить символ операції: E (encrypt) або D (decrypt).
Другий рядок містить ціле число KK K — зсув
Третій рядок містить рядок довжиною від 11 1 до 10410^4 104.
Вихідні дані
Виведіть зашифрований або розшифрований рядок.
Приклад
Input:
E
3
Hello, World!

Output:
Khoor, Zruog!
Input:
D
3
Khoor, Zruog!

Output:
Hello, World!

E(x) = (x + k) mod N
D(x) = (x - k) mod N
unicode alpahbet 65 <= & <= 90 | 97 <= & <= 122
"""
def caesar():
    type = input()
    delta = int(input())
    text = input()
    result = ""
    if type == "E":
        for i in range(len(text)):
            if ((65 <= ord(text[i]) and ord(text[i]) <= 90) or (97 <= ord(text[i]) and ord(text[i]) <= 122)):
                if (text[i].isupper()):
                    ind = (((int(ord(text[i]) - 64) + delta) % 26) + 64)
                    if (ind == 64):
                        ind += 26
                    result += chr(ind)
                else:
                    ind = (((int(ord(text[i]) - 96) + delta) % 26) + 96)
                    if (ind == 96):
                        ind += 26
                    result += chr(ind)
            else:
                result += text[i]
    elif type == "D":
        for i in range(len(text)):
            if ((65 <= ord(text[i]) and ord(text[i]) <= 90) or (97 <= ord(text[i]) and ord(text[i]) <= 122)):
                if (text[i].isupper()):
                    ind = (((int(ord(text[i]) - 64) - delta) % 26) + 64)
                    if (ind == 64):
                        ind += 26
                    result += chr(ind)
                else:
                    ind = (((int(ord(text[i]) - 96) - delta) % 26) + 96)
                    if (ind == 96):
                        ind += 26
                    result += chr(ind)
            else:
                result += text[i]
    print(result)

caesar()