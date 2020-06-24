
print ('Welcome!')

#You have to write a program that, when run, asks the user to input some text. It can be a phrase, a sentence, or multiple sentences. After it is entered, your program will let the user know if it is a palindrome or not. Use "is a palindrome" and "is not a palindrome" in your output in order for the tests to pass.

name = input ("Please enter your birthdate.")
print(birthdate)
if birthdate == birthdate[::-1]:
  print(birthdate, 'is a palindrome.')
else:
  print(birthdate, 'is not a palindrome.')


  
