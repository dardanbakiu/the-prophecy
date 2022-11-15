
from number_parser import parse_ordinal
import numbers

def isNumber(word):
    return isinstance(word, numbers.Number)

def isMoreThen21(word):
    return word > 20

def numberToPercentage(num):
    if(num > 1):
        return 1 - ((num - 1) * 0.05)
    return 1

def formatNumber(num):
    return format(num, '.8f') + '%'

def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    result = round(result * 100, 8)
    return formatNumber(result)

def calculateSentence(sentence):
    percentages = []
    words = sentence.split(" ")
    for word in words:
        word_to_number = parse_ordinal(word)
        if(isNumber(word_to_number)):
            if(isMoreThen21(word_to_number)):
                return formatNumber(0)
            else:
                percentages.append(numberToPercentage(word_to_number))
    return multiplyList(percentages)
                

input_file = open("input.txt", "r")
senteces = input_file.read().split(".")

file_to_delete = open("output.txt",'w') #clear output file
output_file = open("output.txt", "a")

index = 1
for sentece in senteces:
    print(f"Case #{index}: {calculateSentence(sentece)}")
    output_file.write(f"Case #{index}: {calculateSentence(sentece)}\n")
    index += 1

output_file.close()