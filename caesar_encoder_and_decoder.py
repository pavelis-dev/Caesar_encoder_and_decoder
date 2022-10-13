def ru_shifr():
    for c in message:
        if c in ('".,:;!? #$%&*+\'-=@^_0123456789'):
            print(c, end='')
        elif c == c.upper() and (ord(c) + key) > 1071:
            print(chr(ord(c) + key - 32), end='')
        elif c == c.upper() and (ord(c) + key) < 1071:
            print(chr(ord(c) + key), end='')
        elif c == c.lower() and (ord(c) + key) > 1103:
            print(chr(ord(c) + key - 32), end='')
        else:
            print(chr(ord(c) + key), end='')


def ru_deshifr():
    for c in message:
        if c in ('".,:;!? #$%&*+\'-=@^_0123456789'):
            print(c, end='')
        elif c == c.upper() and (ord(c) - key) < 1040:
            print(chr(ord(c) - key + 32), end='')
        elif c == c.upper() and (ord(c) - key) > 1040:
            print(chr(ord(c) - key), end='')
        elif c == c.lower() and (ord(c) - key) < 1072:
            print(chr(ord(c) - key + 32), end='')
        else:
            print(chr(ord(c) - key), end='')


def en_shifr():
    for c in message:
        if c in ('".,:;!? #$%&*+\'-=@^_0123456789'):
            print(c, end='')
        elif c == c.upper() and (ord(c) + key) > 90:
            print(chr(ord(c) + key - 26), end='')
        elif c == c.upper() and (ord(c) + key) < 90:
            print(chr(ord(c) + key), end='')
        elif c == c.lower() and (ord(c) + key) > 122:
            print(chr(ord(c) + key - 26), end='')
        else:
            print(chr(ord(c) + key), end='')


def en_deshifr():
    for c in message:
        if c in ('".,:;!? #$%&*+\'-=@^_0123456789'):
            print(c, end='')
        elif c == c.upper() and (ord(c) - key) < 65:
            print(chr(ord(c) - key + 26), end='')
        elif c == c.upper() and (ord(c) - key) > 65:
            print(chr(ord(c) - key), end='')
        elif c == c.lower() and (ord(c) - key) < 97:
            print(chr(ord(c) - key + 26), end='')
        else:
            print(chr(ord(c) - key), end='')


vid_op = input('Шифровать (1), Расшифровать (2): ')
while vid_op not in ('1', '2'):
    vid_op = input('Введите число! Шифровать (1), Расшифровать (2): ')
vid_op = int(vid_op)

key = input('Введите ключ шифрования (целое число): ')
while not key.isdigit():
    key = input('Введите ключ шифрования (целое число): ')
key = int(key)

language = input('Введите язык текста (ru или en): ')
while language.lower() not in ('ru', 'en'):
    language = input('Введите язык текста (ru или en): ')
language = language.lower()

if vid_op == 1:
    message = input('Введите текст для шифрования: ')
else:
    message = input('Введите текст, который необходимо расшифровать: ')

if language == 'ru' and vid_op == 1:
    ru_shifr()
elif language == 'ru' and vid_op == 2:
    ru_deshifr()
elif language == 'en' and vid_op == 1:
    en_shifr()
elif language == 'en' and vid_op == 2:
    en_deshifr()
