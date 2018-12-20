import string

en_low = string.ascii_lowercase
en_up = string.ascii_uppercase
rus_low = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
rus_up = rus_low.upper()
counter1 = 0
counter2 = 0

try:
    with open('Text.txt', 'r') as text:
        text = text.read()
    while True:
        answer = input('\nWhat do you want to do? / Что вы хотите сделать?\n1)Encode / Закодировать\n2)Decode / '
                   'Раскодировать\n3)End program / Завершить программу\n')
        if answer == '1' or answer.lower() == 'encode' or answer.lower() == 'закодировать':
            k = 'k'
            while k.isdigit() != True:
                k = input('Enter shift (integer) / Введите сдвиг (целое число): ')
            k = int(k)
            for counter1 in range(len(text)):
                for counter2 in range(len(en_low)):
                    if text[counter1] == en_low[counter2]:
                        num_s_en = counter2 + k - ((counter2 + k) // len(en_low)) * len(en_low)
                        text = text[0:counter1] + en_low[num_s_en] + text[counter1 + 1:]
                        break
                for counter2 in range(len(en_up)):
                    if text[counter1] == en_up[counter2]:
                        num_s_en = counter2 + k - ((counter2 + k) // len(en_up)) * len(en_up)
                        text = text[0:counter1] + en_up[num_s_en] + text[counter1 + 1:]
                        break
                for counter2 in range(len(rus_low)):
                    if text[counter1] == rus_low[counter2]:
                        num_s_rus = counter2 + k - ((counter2 + k) // len(rus_low)) * len(rus_low)
                        text = text[0:counter1] + rus_low[num_s_rus] + text[counter1 + 1:]
                        break
                for counter2 in range(len(rus_up)):
                    if text[counter1] == rus_up[counter2]:
                        num_s_rus = counter2 + k - ((counter2 + k) // len(rus_up)) * len(rus_up)
                        text = text[:counter1] + rus_up[num_s_rus] + text[counter1 + 1:]
                        break
            print(text)
        elif answer == '2' or answer.lower() == 'decode' or answer.lower() == 'раскодировать':
            k = 'k'
            while k.isdigit() != True:
                k = input('Enter shift (integer) / Введите сдвиг (целое число): ')
            k = int(k)
            for counter1 in range(len(text)):
                for counter2 in range(len(en_low)):
                    if text[counter1] == en_low[counter2]:
                        num_s_en = counter2 - k + k // len(en_low) * len(en_low)
                        text = text[0:counter1] + en_low[num_s_en] + text[counter1 + 1:]
                        break
                for counter2 in range(len(en_up)):
                    if text[counter1] == en_up[counter2]:
                        num_s_en = counter2 - k + k // len(en_up) * len(en_up)
                        text = text[0:counter1] + en_up[num_s_en] + text[counter1 + 1:]
                        break
                for counter2 in range(len(rus_low)):
                    if text[counter1] == rus_low[counter2]:
                        num_s_rus = counter2 - k + k // len(rus_up) * len(rus_up)
                        text = text[0:counter1] + rus_low[num_s_rus] + text[counter1 + 1:]
                        break
                for counter2 in range(len(rus_up)):
                    if text[counter1] == rus_up[counter2]:
                        num_s_rus = counter2 - k + k // len(rus_up) * len(rus_up)
                        text = text[0:counter1] + rus_up[num_s_rus] + text[counter1 + 1:]
                        break
            print(text)
        elif answer == '3' or answer.lower() == 'end program' or answer.lower() == 'завершить программу':
            break
except FileNotFoundError:
    print('Ошибка! Файл не найден. Пожалуйста, создайте файл Text.txt в папке с программой.\nПеред запуском программы'
          ' убедитесь, что вы сохранили файл, иначе программа будет использовать последнюю сохранённую копию файла.')
