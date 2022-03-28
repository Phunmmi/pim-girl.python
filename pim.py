
# from re import A, X


# def add_numbers():
#     print(6+5)

#print(5)
#add_numbers()

# def add_numbers():
#     print(3+3)
# add_numbers()

# import math
# print (math.sqrt(100))

# print(len("this is a boy"))


# a = lambda x : 5*x +4
# b = lambda x : 6*x +3
# c= a(b(5))
# print(c)

# PI = 3.142
# A = lambda r : (3.142 * (r**2))
#print (A(10))
#x=20
#def test_func():
  #  global X
 #   x=5
#test_func()
#print(x)

# def add_num(x,y):
#      print(x+y)
# add_num(3,2)


# def show_employee(name,salary=9000):
#     print("name:",name, "salary:",salary)
# show_employee("Ben", 12000)
# show_employee("jessa")

# dollar= int(input ('please enter the dollar amount') )
# d= 10
# naira= dollar * 550
# print(f'{d} is equivalent to {naira}')

# def print_twice(bruce,alex):
#     print(bruce)
#     print(alex)
# print_twice('bruce')
# print_twice(alex="a")

# def minus(a,b=3):
#     print(a-b)
# minus(8,5)
# minus(5,8)
# minus(b=8, a=5)
# minus(a=5,b=8)


# arr = [1,2,3,4,5,6]
# mapped=map(lambda y:y**2, arr)
# print(list(mapped))

# b = [1,2,3,5,6]
# c = (sum(b)/len(b))
# print (c)
# range = (max (b) - min (b))
# print (range)

# user = input('please input your numbers')
# num= user.split(",")
# print(num)
# n =list (map(int,num))
# print(n)

# scores = input ('please input the score of the students')
# num = scores.split(",")
# print(num)

# n=list (map(int,num))
# print(n)

# average= (sum(n)/len(n))
# print(average)

# range = (max (n) - min (n))
# print (range)

# standard_deviation = (sum(map(lambda x : (x-average)**2, n))/len(n))
# print(standard_deviation)

# variance= (standard_deviation)**2
# print(variance)



# age= input('please input your age')
# print (age)
# birth_year = 2022 - int(age)
# print (birth_year)

# def add_num(a,b):
#     return(a+b)
#     print(a+b)
    

# x = add_num (4,6)
# print(x)

# def factorial(n):
#      if n == 1:
#        return 1

#      return n * factorial(n-1)
# print(factorial(5))

#def slugify(word):
 #   return word.replace(" ","-").lower()

#print(slugify('how do you cook'))

#def username(a,b):
 #   c = a[:2]
  #  d = b[-2:]
   # e = c+d
    #return(e)

#print (username("adaeze","usman"))

#def first_last(first,last):
 #   a = first[:2]
  #  b = last[-2:]
   # return a+b

#print (first_last('Adaoni', 'usman'))

#str = 'HEEEEyyyyyy'
#print (str.swapcase())

#numeric = lamba string : string.isnumeric()
#change_case = lamda string: 

#a = input("Enter filename here>")
#b = a.split('.')
#print (b[1])

#num = [2,3,5,6,8]
#mapped = map(lambda y:y**3,num)
#mapped = map(lambda y:y**2,num)
#print(list(mapped))

#h = 1
#while h <=10:
 #   if h == 10:
  #     print("Boom")
   # else:
    #  print(h)
    #h+=1

i = 1
while True:
    print(f'keep playing {i}')
    c =input ('do you want to keep playinh \n>')
    i +=1
    if c=='y':
        continue 
    else:
        break