# Define the variables and assign them from user input
def check_fermat(a,b,c,n):
    print ('There are no positive integers a, b, and c such that (a*n)(b*n)=(c*n)for any values of n>2')
a = int(input('Enter a number for a'))
b = int(input('Enter a number for b'))
c =  int(input('Enter a number for c'))
n =  int(input('Enter a number for n'))
# check to see if it is true , then the equation is wrong
if(a*n) + (b*n)==(c**n):
   print('Holy smokes,fermat was wrong!')
# if it is false then the equation holds up
else: 
    print('No,that does not work')
#Assign the integer values from the user to the equation a, b, c, n
check_fermat('a','b','c', 'n')
#Define the variables and assign them from user input

def check_fermat(a,b,c,n):
    print('There are no positive integers a,b,and c such that (a*n)(b*n)=(c*n) for any values of n>2')
a =  int(input('Enter a number for a'))
b =  int(input('Enter a number for b'))
c =  int(input('Enter a number for c'))
n =  int(input('Enter a number for n'))

#check to see if it is true then the equation is wrong 

if (a*n)+(b*n)==(c**n):
    print('Holy smokes,fermat was wrong!')

#if it is false then the equation holds up

else: 
    print('No, that does not work')
