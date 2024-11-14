words = []
for i in range(10):
    word = input(f"Kindly enter a word {i + 1}: ")
    words.append(word)
    
while True:
    length = input("Please Enter a length/number: ")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("OoOoH NO!, your input is invalid. Try again a numeric value. ")
        
matching_words = [word for word in words if len(word) == length]

if matching_words:
    print("Here are the words with the specified length:", ', '.join(matching_words))
else:
    print("Oops sorry, there are no words was found with specified length.")
    