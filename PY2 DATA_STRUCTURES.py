
# Lists, tuples, dictionaries, sets are non primitive data structures. A list can store multiple elements of multiple datatypes unlike array. Lists are accessed just like 
strings i.e. L[::]
#LISTS are mutable sequences of any type data stored within square brackets []


list=string.split(' ')                                                 # to convert a string into a list
string=' '.join(list)                                                  # to convert list back into string
reverse = s[::-1]   or s.reverse                                       # to reverse a list
final_list=[word.title() for word in words]                            # to change list items and start them with upper case.

friend = ["punkoo","maddy","osho","saggy","osho","harshu",1 ]          # working with lists in Python []
help(friend)
print(friend[0])                                                       # starts from 0
print(friend[-1])                                                      # last element is indexed -1
print(friend[1:])                                                      # grabs from 1 to last
print(friend[1:6:2])                                                   # grabs from 1 upto 6 and every 2nd element
print(friend[::-1])                                                    # reverses the list
friend[1]="mike"
print(friend)                                                          # replaces maddy (1st) with mike

lucky_numbers =[100,34,1,4,5,6,78,98,100]
friend.extend(lucky_numbers)                                           # to extend the list
print(friend)
friend.append("tanks")                                                 # to append ONLY one more item at last
print(friend)
friend.insert(1,"kelly")                                               # to insert at any position
print(friend)
friend.remove("kelly")                                                 # to remove an item in the list by element
print(friend)
del friend[:3]                                                         # deletes 1st 3 elements by value
print(friend)
print(friend.clear())                                                  # to clear the list
friend = ["punkoo","maddy","saggy","osho","osho","harshu"]
friend.pop()                                                           # pops the last element out of the list
print(friend)
friend.pop(1)                                                          # removes 1st element
print(friend.index("osho"))                                            # gives the index of osho
print(friend.count("osho"))                                     # counts the number of times a string is in the list
friend.sort()
print(friend)                                                   # sorts the list in alphabetical order
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()                                         # reverse the elements of the list
print(lucky_numbers)
friend_2 = friend.copy()                                        # copies the list i.e. points to the same variable
print(friend_2)
friend_3=friend[:]                                              # cloning a list i.e. creates a new variable
print(friend_3)

# TUPLES are immutable ordered sequences of any type of data stored within round brackets ()

coordinates =(4,5)                                    # creating a tuple
print(coordinates[0])                                 # 1st index position
print(len(coordinates))                               # length of a tuple
print(4 in coordinates)                               # search in tuple
tuple_nested= ("op",("Rty",1,2),5,6)                  # nested tuples
print(tuple_nested[1][1])
coordinates_many=[(1,2),(7,4),(8,10)]                 # List of tuples

#DICTIONARIES USE {} CURLY BRACKETS AND ARE MUTABLE DATA SEQUENCES MATCHED WITH IMMUTABLE KEYS.
dictionary={"key1":12,"key2":"delhi","key3":(1,4,6)}        #{} used to define dictionary
print(dictionary)
print(dictionary["key1"])
dictionary["key4"]="string"                                 # inserting element to dictionary
print(dictionary)
del(dictionary["key1"])                                     # delete a key
print("key1" in dictionary)                                 # to check whether a key is in dictionary
print(dictionary.keys())                                    # to check all the keys in the dictionary
print(dictionary.values())                                  # to check all values in the dictionary
max(dictionary.values())


#Sets are a type of unordered unique data collections defined under curly brackets where no duplicates are present
set_1={123,"john",12.5,"john",False}
print(set_1)
print(friend)
print(set(friend))
print(type(set(friend)))                                    # type casting of list to set
set_1.add(True)
print(set_1)                                                # adding an element to set
set_1.remove(False)                                         # to remove an element from set
print(set_1)
print("john" in set_1)                                      # to check whether an item is in set

# mathematical operations like union by s1.union(s2), intersection by & can be applied to sets.
