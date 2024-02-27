# Task 2. Stuttering Function
# Write a function stutter() that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
# Assume all input is in lower case and at least two characters long.
# Examples
#
# stutter("incredible") ➞ "in... in... incredible?"
# stutter("enthusiastic") ➞ "en... en... enthusiastic?"
# stutter("outstanding") ➞ "ou... ou... outstanding?"

def stutter(word):

    i = 0

    stutter_part = word[0:2]
    final_stutter = ""

    while i < 3:
        final_stutter += stutter_part + "... "
        i += 1
        if i == 2:
            final_stutter += word + "?"
            break

    print(final_stutter)
