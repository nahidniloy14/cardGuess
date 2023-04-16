def num_square(num):
    return num**2

#num_square(num=[1,2,3,4,5,6,7,8])
"""
Our compiler would not allow us to do this thing,
instead what we can do is to use the map function
"""
num=[1,2,3,4,5,6,7,8]
for item in map(num_square,num):
    print(item)


print("..........................")
for item in num:
    num=item**2
    print(num)

"""
map function will allow us to simplify the code
"""
# for item in map(num_square,num):
#     print(item)
"""
map function does not take the function name istead it takes this as a  parameter
that is why we used num_square istead of num_square()
"""
