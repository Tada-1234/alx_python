def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        greater = 0
        for k in a_dictionary:
            temp = a_dictionary.get(k)
            if temp > greater:
                greater = temp
        for k, v in a_dictionary.items():
            if v == greater:
                return k
