h = "Hello Good morning I am here to help you Wht do you think about it"
print(h[::-1]) #reverse the string 0 ir the start of the sentence and - from backward it counts and prints backward

print(h[0:])
print(h[3:])
print(h[::-8])


word = h.split()
print(word[1]) #splitting words from a strings

y = "apple, mango, orange"
print(y.index(','))  #It helps to count
print(y[0:y.index(',')]) #print the indexes as per the requirement and 0th index means first and 1st index means 2nd word
