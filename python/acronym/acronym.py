def abbreviate(words):
    acronym = list(
        (
            char
            for char in str(words).replace("'", '').title()
            if str(char).isupper()
        )
    )
    return ''.join(acronym)
