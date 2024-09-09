#function for count vowels that take text as its parameter
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for character in text.lower():  # Convert to lowercase in the loop
        if (character in vowels):
            count += 1
    return count
result = count_vowels("nonzamo")
print(result)  

