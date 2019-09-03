def shortestDistance(words, word1, word2):
    first_word_index = -1
    second_word_index = -1
    distance = float('inf')
    for i in range(len(words)):
        if words[i] == word1:
            first_word_index = i
        elif words[i] == word2:
            second_word_index = i
        if first_word_index >= 0 and second_word_index >= 0:
            distance = min(distance, abs(first_word_index - 
            second_word_index))
    return distance

words = ["practice", "makes", "perfect", "coding", "makes"]
# shortestDistance(words, 'coding', 'perfect')
shortestDistance(words, 'coding', 'practice')
shortestDistance(words, 'makes', 'coding')