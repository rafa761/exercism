def return_sentence(sentence):
    tamanho = len(sentence)
    if tamanho == 1:
        return sentence[0]

    phrase = ''
    for index, p in enumerate(sentence):
        if index == 0:
            phrase += p
        elif index < tamanho-1:
            phrase += f', {p}'
        else:
            phrase += f', and {p}'

    return phrase


def recite(start_verse=1, end_verse=1):

    day_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
                'eleventh', 'twelfth']

    things_list = ['a Partridge in a Pear Tree.', 'two Turtle Doves', 'three French Hens', 'four Calling Birds',
                   'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking',
                   'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']

    # Cria um dicionario contendo os dias como chave e os presentes como valores
    gave_list = []
    for index, day in enumerate(day_list, start=1):
        # Reverte a lista de presentes
        reverse_things_list = things_list[:index]
        reverse_things_list = reverse_things_list[::-1]

        # Cria um dicionario com as chaves e dados necessarios
        gave_dict = {
            'index': index,
            'day': day,
            'sentence': reverse_things_list
        }

        # Armazena os dicionarios em uma lista
        gave_list.append(gave_dict)

    return_lyric = []
    for item in gave_list[start_verse-1:end_verse]:
        return_lyric.append(f"On the {item['day']} day of Christmas my true love gave to me: "
                            f"{ return_sentence(item['sentence'])}")

    return return_lyric
