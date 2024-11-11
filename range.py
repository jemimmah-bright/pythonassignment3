# # the range function herates through sequences) the "for loops(its also part of the loops and a function)
# #it takes in parameters of start,stop
# # Examples
# name = "Birunji" 
# for items in name:    #for loops
#     print(items)
 

# marks = [70,40,10,20]
# for mark in marks:
#     print(marks)

# #When using a function
# def total_marks():
#     marks = [70,40,10,20]
#     sum = 0
#     for mark in marks:
#         sum+=marks
#         print(f"The total mark is: {sum}")
# total_marks()

# # RANGE AS A FUCTION
# #using a loop print all number from zero to six(0-6) Hint(use a range function)
# for number in range(7):
#     print(number)

# #print numbers between 0-10 0 and 10 inclusive
# for number in range(11): 
#     print(number)

# #print numbers between 1-20
# for number in range(1,21):
#     print (number)

# print the following range of even numbers 2-10

def even_numbers():
    for num in range(2,11):
        if num % 2==0:
            print(num)


def even_numbers():
    for number in range(2,11,1):
      print (number)
even_numbers()


