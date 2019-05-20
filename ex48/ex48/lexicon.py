def scan(stuff):

    words = stuff.split()

    directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
    verbs = ('go', 'stop', 'kill', 'eat')
    stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
    nouns = ('door', 'bear', 'princess', 'cabinet')

    result = []

    for word in words:
        try:
            word = int(word)
            result.append(('number', word))
        except ValueError:
            if word.lower() in directions:
                result.append(('direction', word))
            elif word.lower() in verbs:
                result.append(('verb', word))
            elif word.lower() in stop_words:
                result.append(('stop', word))
            elif word.lower() in nouns:
                result.append(('noun', word))
            else:
                result.append(('error', word))
    return result
