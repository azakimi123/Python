file = input("Enter the input file name: ")

counter = {}

with open(file) as f:
    word_list = f.read().split()
    
    for word in sorted(word_list):
        counter.update({word:0})

    for x in counter.keys():
        for word in word_list:
            if word == x:
                counter[word] += 1


print(counter)