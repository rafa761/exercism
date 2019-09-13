def hey(phrase=str):
    bob_answers = {'question': 'Sure.',
                   'yell': 'Whoa, chill out!',
                   'yell question': "Calm down, I know what I'm doing!",
                   'empty': 'Fine. Be that way!',
                   'any': 'Whatever.'
                   }

    phrase = phrase.strip()

    if phrase == '':
        return bob_answers['empty']

    elif phrase.endswith('?'):
        if phrase.isupper():
            return bob_answers['yell question']
        elif phrase:
            return bob_answers['question']

    elif phrase.isupper():
        return bob_answers['yell']

    else:
        return bob_answers['any']
