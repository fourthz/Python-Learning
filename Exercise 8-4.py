
# Exercise 8-4

# This will read through a file, create a list of unique words, then alphabetize them.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)

except:
    print("A file named", fname, "cannot be opened.")
    quit()

unique_words = []

for line in fhand:

    line_words = line.split()
    
    for i in range(len(line_words)) :

        if line_words[i] not in unique_words :
            unique_words.append(line_words[i])
    
unique_words.sort()
print(unique_words)
