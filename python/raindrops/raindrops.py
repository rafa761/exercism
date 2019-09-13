def raindrops(number):
    """

    :param number: number to be translated to raindrop
    :return: raindrop sound
    """
    factors = []
    sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    result = ''
    # calculate number factors
    for num in range(1, number + 1):
        if number % num == 0:
            factors.append(num)

    # Check if the number factors is in the sound dict, so return the input number
    if all(list(map(lambda x: x not in sounds.keys(), factors))):
        return str(number)

    # Iterate through sound dict searching for sound match
    for factor in factors:
        if factor in sounds.keys():
            result += sounds[factor]
    return result
