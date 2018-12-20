import string

try:
    def encode(shift, Text):
        for num_lang in languages:
            lang = num_lang
            for counter1 in range(len(Text)):
                for counter2 in range(len(lang)):
                    if Text[counter1] == lang[counter2]:
                        num_s = counter2 + shift - ((counter2 + shift) // len(lang)) * len(lang)
                        Text = Text[0:counter1] + lang[num_s] + Text[counter1 + 1:]
                        break
        print(Text)

    def decode(shift, Text):
        for num_lang in languages:
            lang = num_lang
            for counter1 in range(len(Text)):
                for counter2 in range(len(lang)):
                    if Text[counter1] == lang[counter2]:
                        num_s = counter2 - shift + shift // len(lang) * len(lang)
                        Text = Text[0:counter1] + lang[num_s] + Text[counter1 + 1:]
                        break
        print(Text)


    languages = [string.ascii_lowercase, string.ascii_uppercase, 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя',
                 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ']
    while True:
        with open('Text.txt', 'r') as text:
            text = text.read()
        answer = input('\nWhat do you want to do? / Что вы хотите сделать?\n1)Encode / Закодировать\n2)Decode / '
                   'Раскодировать\n3)Show alphabet list / Показать список алфавитов\n4)Add language / Добавить язык\n'
                       '5)End program / Завершить программу\n')
        if answer == '1' or answer.lower() == 'encode' or answer.lower() == 'закодировать':
            k = 'k'
            while k.isdigit() != True:
                k = input('Enter shift (integer) / Введите сдвиг (целое число): ')
            k = int(k)
            encode(k, text)
        elif answer == '2' or answer.lower() == 'decode' or answer.lower() == 'раскодировать':
            k = 'k'
            while k.isdigit() != True:
                k = input('Enter shift (integer) / Введите сдвиг (целое число): ')
            k = int(k)
            decode(k, text)
        elif answer == '4' or answer.lower() == 'add language' or answer.lower() == 'добавить язык':
            answer2 = input('In the initial version of the program there are 2 languages: English and Russian. '
                            'Want to add something? /\nВ изначальной версии программы есть 2 языка: английский и '
                            'русский. Хотите что-то добавить?\n1)Yes / Да\n2)No / Нет\n')
            if answer2 == '1' or answer2.lower() == 'yes' or answer2.lower() == 'да':
                print('Enter alphabet / Введите алфавит:')
                new_alphabet = str(input().lower())
                if new_alphabet != new_alphabet.upper():
                    new_list = [new_alphabet, new_alphabet.upper()]
                else:
                    new_list = [new_alphabet]
                languages.extend(new_list)
        elif answer == '3' or answer.lower() == 'show alphabet list' or answer.lower() == 'показать список алфавитов':
            print(languages)
        elif answer == '5' or answer.lower() == 'end program' or answer.lower() == 'завершить программу':
            break
        else:
            print('Repeat input / Повторите ввод')
except FileNotFoundError:
    print('Ошибка! Файл не найден. Пожалуйста, создайте файл Text.txt в папке с программой.\nПеред запуском программы'
          ' убедитесь, что вы сохранили файл, иначе программа будет использовать последнюю сохранённую копию файла.')
