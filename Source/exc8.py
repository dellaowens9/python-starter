def short_straw(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num 
    print(smallest)
    
numbers = [34,15,88,2]
short_straw(numbers)

myList = [6,2,7,3,77,7,1]
short_straw(myList)