# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2

lower_name = name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t+r+u+e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l+o+v+e

score_str = str(true)+str(love)
score = int(score_str)

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score<50 and score>40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
