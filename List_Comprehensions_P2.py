def square_evens(numbers:list)->list:
    result = []
    for x in numbers:  # Iterate through each number in the input list
        if x % 2 == 0: # Check if the number is even
            result.append(x * x)  # Compute the square of the even number & append it to the result list
    return result


arr = [1, 2, 3, 4, 5]
squares_of_evens = square_evens(arr)
print("Squares of even numbers:", squares_of_evens)
