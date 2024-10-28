'''
Password validator is a program that validates passwords to match specific rules. For example, the minimum length of the password must be eight characters long and it should have at least one uppercase letter in it. 

In this example, a valid password is the one that conforms to the following rules:
 - Minimum length is 5;
 - Maximum length is 10;
 - Should contain at least one number;
 - Should contain at least one special character (such as &, +, @, $, #, %, etc.);
 - Should not contain spaces.
'''
from string import punctuation
def Validator(x):
         
         n = (i for i in range(0,11))
         if ( (" " not in x) and ( len(x) >= 5 and len(x) <= 10)):
             for k in n:
                 if (str(k) in x):
                     for i in punctuation:
                         if i in x:
                            return True
         return False

p = input('Password to check: ')
print(f"{p} is a valid password : {Validator(p)}")