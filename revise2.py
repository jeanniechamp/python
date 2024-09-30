quote = 'to be or not to be'
print(quote.find('be'))
print(quote.replace('be' , 'me'))


#boleean=rue or false
name = ('vaanya')
is_cool = False
is_cool = True
print(bool(0))
#0 is false. 1 is true


#birth_year = input('what year were you born in? ')
#age = 2024 - int(birth_year)
#print(f'your age is {age}')

#31
#username = input('user')
#password = input('secret')
#len = len(password)
#hidden_password = '*' *len

#print(f'{username}, your password, {hidden_password}, is {len} letters long')

##check code again


#32
#grocerylist = ['milk' , 'bread' , 'fruits'] 
#print(grocerylist = [2])

#33
#grocerylist = [
#               'milk' , 
#               'bread' ,
#                 'fruits',
#                   'potato'] 
#print(grocerylist)
#34 
matrix = [
[1,2,3],
[2,4,6],
[7,8,9]
]

print(matrix[0][1])

#43
dictionary = {
    123 : '123',
    True: 127

}
print(dictionary[123])
# you cant add list because it needs to be immutable in order to be in a dictionary, you can add or remove things in list

user = {
    123 : '123',
    True: 127
    #key : value

}
print(user.get('age' , 55))
print(123 in user.keys())
#get method prevents error from appearing in code+ modifies dict
