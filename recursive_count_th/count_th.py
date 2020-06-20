'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    count = 0

    selected_word = word
    # base case required for recursion to know when to stop
    if len(word) < 2:
        return 0
    # check for occurance in string match "th"
    elif word[0] + word[1] == "th":
        count += 1
        selected_word = word[2:]

    elif word[1] == "t":
        selected_word = word[1:]

    else:
        selected_word = word[2:]

    return count + count_th(selected_word)
