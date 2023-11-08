from datetime import date

today = f"Today's date: {date(2023,8,11)}"

# print(f"Today's date: {today}")

file = open("output.txt","w")
file.write(today)
file.close()


# file2 = open("output.txt","r")
# file2.read(today)
# file2.close()

# Checking if the data is
# written to file or not
# file1 = open('myfile.txt', 'r')
# print(file1.read())
# file1.close()