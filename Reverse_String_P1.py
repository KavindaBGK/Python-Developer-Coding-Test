def reverse_string(s: str) -> str:
    length = len(s) # measure length of the string
    s = list(s) # first it convert to a list

    for i in range(length // 2):
        temp = s[i] #i th element pass to temp value
        s[i] = s[length - 1 - i] #swap position i with the character at position length - 1 - i
        s[length - 1 - i] = temp #Place the character originally at position i to position length - 1 - i

    return (''.join(s))


str_input = input("Enter a string: ") # First get input from user
reversed_str = reverse_string(str_input)
print(f"Reversed string: {reversed_str}")


#Insted of that we can use "return (input_string[::-1]) and get swap output at once"