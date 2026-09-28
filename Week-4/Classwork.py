#  Write a Python program using a while loop to print the numbers 1
# through 10.

# count = 1
# while(count < 11):
#   print(count)
#   count = count + 1

# 2. Write a program that uses a while loop to print all even numbers
# from 2 to 20.

# count2 = 1
# while(count2 < 21):
#   if(count2 % 2 == 0):
#     print(count2)
#   count2 = count2 + 1


# 3. Write a program that asks the user for a starting number and counts
# down to 0.

# count3 = int(input("give me a number to count down"))
# while(count3 > 0 ):
#   print(count3)
#   count3 = count3 - 1

# 4. Write a Python program to print a table of consecutive even
# numbers from 2 to 30 and their square values.
# A sample output of this is as follows:
# 2 4
# 4 16
# 6 36
# …
# 28 784
# 30 900

# for i in range(2,31):  
#   print(i * i)


# 5. Keep asking the user to enter a password until they enter the
# correct password.

# usinput = ""
# password = "password"
# while(usinput != password):
#   usinput = input("Enter your password")



# 6. Choose a secret number between 1 and 100. Keep asking the user
# to guess until they get it correct. Tell them whether their guess is
# too high or too low.

# secret = "51"
# usinput = ""
# while(usinput != secret):
#   int(input("enter a number 1-100"))
#   if(usinput<51):
#     print("too high")
#   else:
#     print("too low")


# 7. Write a Python program that keeps asking the user to enter a word.
# The program should continue asking until the user enters "stop".
# When the user enters "stop", print "Program ended."
# Example
# Enter a word: apple
# Enter a word: banana
# Enter a word: computer
# Enter a word: stop
# Program ended.



# 8. Ask the user for a positive integer n. Use a while loop to calculate
# the sum of all numbers from 1 to n

# count8 = input("give me a number?")
# sum8 = 0
# counter8 = 0
# while(counter8 < count8 ):
#   sum8 = sum8 + counter8 
#   counter8 = counter8 + 1
# print(sum8)

# 9. Keep asking the user to enter numbers. Add them together until the
# user enters 0. Then display the total.

# count9 = int(input("give me a number?"))
# sum9 = 0

# while(count9 != 0 ):
#   sum9 = sum9 + count9 
#   count9 = int(input("give me a number?"))
#   print(sum9)


# 10. Keep asking the user for numbers until they enter 0. Count
# # how many numbers were positive and how many were negative.
# posNum = 0
# negNum = 0
# count10 = int(input("give me a number?"))

# while(count10 != 0 ):
#   if(count10 > 0):
#     posNum = posNum + 1
#   else:
#     negNum = negNum + 1
    
#   count10 = int(input("give me a number? Enter 0 to stop"))

# print(posNum, "positive numbers")
# print(negNum, "negative numbers")


# 11. Write a Python program to read the grades of 6 students,
# calculate their average, and print it out.

# numStudents = 6
# numStudentsCount = 6
# sumGrade = 0
# avgGrade = 0
# while(numStudentsCount > 0):
#   grade = int(input("Grade for student?"))
#   sumGrade = sumGrade + grade
#   numStudentsCount = numStudentsCount - 1

# avgGrade = sumGrade / numStudents
# print(avgGrade, " is the average between", numStudents, "students")


# sumgrade =0
# for i in range(0,6):
#   sumgrade = sumgrade + int(input("grade?"))

# print(sumgrade/6, " is the average between 6 students")

# 12. Write a Python program that prompts the user to enter
# integers (0 to stop). The program should find and print the largest
# positive even number of them. If the user did not enter any positive
# even number, the program should print 0.



# biggestPosNum = 0
# numInp = int(input("give me a number?"))

# while(numInp != 0):
#   if(numInp > 0):
#     if(biggestPosNum < numInp and numInp%2 == 0):
#       biggestPosNum = numInp
#       numInp = int(input("give me a number?"))
#     else:
#       numInp = 0

# print(biggestPosNum, "was the largest postive even number")


# 13. In mathematics, the factorial of a positive integer n, denoted
# by n!, is the product of all positive integers less than or equal to n.
# For example:
# 0! = 1
# 1! = 1
# 2! = 1 * 2
# 5! = 1 * 2 * 3 * 4 *5 = 120
# Write a Python code that reads a positive number n from the user,
# then calculates n! and displays the result in the output window. If
# the user enters a negative number, the program should not do any
# calculation and should display a message that says: “Positive value
# # is expected”.

# sum = 1
# numFact = int(input("give a num"))

# for i in range(1,numFact + 1):
#   sum = sum * i
# print(sum)

# 14. Write a Python program using a for loop to print the numbers
# from 1 to 10.



# 15. Ask the user to enter a word. Use a for loop to print that word
# 5 times.


# 16. Use a for loop to print all even numbers from 2 to 20.


# 17. Ask the user for a number n. Use a for loop to find the sum of
# all numbers from 1 to n.



# 18. Ask the user to enter a word. Use a for loop to check each
# letter. Count how many times the letter "a" appears.
# Example:
# Enter a word: banana
# # The letter a appears 3 times.
# count = 0
# word = input("enter a word")
# for i in word:
#   if(i == "a"):
#     count+=1
# print(count)


# 19. Write python program that displays the following:
# 0000
# 1111
# 2222
# 3333

# for i in range(4):
#   for j in range(4):
#     print(i, end="")
#   print()
    
    

# 20. Write python program that displays the following:
# ****
# ****
# ****
# ****


# for i in range(4):
#   for i in range(4):
#     print("*", end ="")
#   print()
    




# 21. Write python program that displays the following:
# 0
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5

# for i in range(7):
#   if(i == 2):
#     continue
#   else:
#     for j in range(i):
#       print(j, end="")
#   print()
   


# 22. Write python program that displays the following:
# *
# **
# ***
# ****
# *****

# for i in range(6):
#   for j in range(i):
#     print("*", end="")
#   print()
   

