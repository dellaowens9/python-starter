import re 

user_input = input("Enter a string: ")
len_word = len(user_input)
find_vowels = re.findall("[aeiou]", user_input)
vowel_count = len(find_vowels)
constant_count = int(len_word) - int(vowel_count)

print(f"Vowels: {vowel_count}")
print(f"Consonants: {constant_count}")



# re.findall('[aeiou]')

# vowels = ['a', 'e', 'i', 'o', 'u']