import re 
text = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."

# word = 'Python'
#word_count = sum(1 for _ in text.split(word) if _ != '') + 1

# print(f"The word '{word}' appears {word_count} times in the text.")

# text = text.split(" ")
# count = 0

# for x in text:
#     if x == "Python":
#         count += 1
# print(count)

text = text.split(" ")
count = 0
for x in text:
    if re.match(x, "Python"):
        count += 1
print(count)


