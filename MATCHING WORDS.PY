def match_words (words):
    counter = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0]  == word[-1]:
            counter += 1
            lst.append(word)
    print ("The words starting and ending with the same letter",lst)   
    return counter
count = match_words(["abc","uj",'kok','woow']) 
print ("The no. with matching end and start are",count)