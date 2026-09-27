def unique_words(list1, list2):
    result = []

    for word in list1:
        if word not in list2 and word not in result:
            result.append(word)

    for word in list2:
        if word not in list1 and word not in result:
            result.append(word)

    return result


words1 = ["кіт", "собака", "миша", "жирафа"]
words2 = ["собака", "миша", "папуга", "слон"]

result = unique_words(words1, words2)

print(result)