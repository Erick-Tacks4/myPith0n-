while True:
    firstWord = str(input('Enter the First Word: '))
    secondWord = str(input('Enter the second word: '))

    matchedLength = len(firstWord)


    if len(firstWord) == len(secondWord):
        print('Yes, the word ', firstWord, ' has the same letter count as the word ', secondWord, ' and the length is; ', matchedLength)

    elif len(firstWord) != len(secondWord):
        print('The word ', firstWord, ' and ', secondWord, ' do not have the same word count or check the spelling and try again.')
        
    else:
        print('Did not understand what you entered. ')