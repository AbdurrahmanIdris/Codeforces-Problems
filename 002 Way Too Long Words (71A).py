words = []
n = int(input())
num_words = n
while (num_words > 0):
    words.append(input())
    num_words -= 1

for word in words:
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)