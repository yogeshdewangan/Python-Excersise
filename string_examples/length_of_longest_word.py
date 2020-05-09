list = ["i", "love", "my", "india", "fsdfsdfsdssd"]

def longest_word(list):
    longest= len(list[0])

    for word in list:
        if longest < len(word):
            longest = len(word)

    print longest

longest_word(list)
