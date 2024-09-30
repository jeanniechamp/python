#46--tuples : immutable list / cannot be modified
my_tuple = (1,2,3,4,5)
print(my_tuple [2])
x, y, z, *other = (1,2,3,4,5)
print (x)
#47 sets : unique lists 
my_set = {1,2,3,4,5,6,7}
you_set = {6,7,8,9}
print(my_set.difference(you_set))
print(my_set.discard(5))
print(my_set)
print(my_set.difference_update(you_set))
print(my_set)
#50 conditional logic : if/else
is_old = False
is_licensed = True
if is_old :
    print("You are old enough!")
elif is_licensed:
    print("You can drive!")
else :
    print("You arent of age!")
#53 ternanry operator
#condition_if_true if condition else condition cond
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to dm"
print(can_message)
# 55 logical operator
#<
#>
#==
#!= when two numbers do not equal
#and or not

#56 excercise
is_magician = True
is_expert = False
if is_magician and is_expert:
    print("you are an expert magician") 
if is_magician:
    print("you are yet to become an expert")
elif not is_magician:
    ("you need magical powers")

#58 loops 
#format 
for item in 'cat':
    for x in [1,2,3]:
        print (item, x)

#59 iterable - list,dictionary,tuple,string,set
#iterated -> 

