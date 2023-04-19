def words_sorting(*args):
    words = {word: sum(map(ord, word)) for word in args}
    result_str = []

    if sum(words.values()) % 2 != 0:
        result_str = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))
    else:  # if the sum of all values is even, sort the dictionary by keys in ascending order
        result_str = dict(sorted(words.items(), key=lambda x: x[0]))

    return "\n".join(result_str)
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
