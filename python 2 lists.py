
#LISTS
friend = ["punkoo","maddy","saggy","osho","harshu"]                    # working with lists in Python []
print(friend[0])                                                       # starts from 0
print(friend[-1])                                                      # last element is indexed -1
print(friend[1:])                                                      # grabs from 1 to last
print(friend[1:4])                                                     # grabs from 1 upto 4
friend[1]="mike"
print(friend)                                                          # replaces maddy (1st) with mike

lucky_numbers =[100,34,1,4,5,6,78,98,100]
friend.extend(lucky_numbers)
print(friend)
friend.append("tanks")                                                 # to append ONLY one more item at last
print(friend)
friend.insert(1,"kelly")                                               # to insert at any position
print(friend)
friend.remove("kelly")                                                 # to remove an item in the list
print(friend)
print(friend.clear())                                                  # to clear the list
friend = ["punkoo","maddy","saggy","osho","osho","harshu"]
friend.pop()                                                           # pops the last element out of the list
print(friend)
print(friend.index("osho"))                                            # gives the index of osho
print(friend.count("osho"))                                     # counts the number of times a string is in the list
friend.sort()
print(friend)                                                   # sorts the list
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()                                         # reverse the elements of the list
print(lucky_numbers)
friend_2 = friend.copy()                                        # copies the list
print(friend_2)
