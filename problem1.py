import sys
name=input("What is your name?")
name = name.title().strip()
print("Hello " + name + ", how are you today?")

mood = input()
cleaned_mood = ""
""" 
Cleans a mood response by removing spaces and punctuation and converting it to lowercase.
>>> clean_mood("GOOD!!!")
'good'
>>> clean_mood("   GoOd   ")
'good'
>>> clean_mood("BaD!!")
'bad'
>>> clean_mood("amazing!")
'amazing'
"""

for i in mood.strip().lower():
    if i.isalpha():
        cleaned_mood = cleaned_mood + i


if cleaned_mood =="good":
    print("I'm so glad!")
elif cleaned_mood =="bad":
    print("I'm so sorry!")
else:
    print(mood + ", huh?")

with open("welcome_letter.txt", "w") as file:
    file.write("It was so great to meet you today, " + name + "!")