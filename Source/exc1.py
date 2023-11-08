import random 

def main():
    total = 0
    num_list = [] 
    for x in range(0, 10):
        random_number = random.randint(0, 100)
        total += random_number
        num_list.append(random_number)
    
    print(num_list)
    print(f"The sum is {total}")    

if __name__ == "__main__":
    main()