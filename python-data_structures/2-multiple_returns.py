def multiple_returns(sentence):
    if sentence is None:
        first = None
        length = len(sentence)
    else:
        length = len(sentence)
        first = sentence[0]
    
    return length, first
