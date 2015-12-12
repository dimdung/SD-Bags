user@samal-dimdung3:~/pylabs/sa$ ls
test.py
user@samal-dimdung3:~/pylabs/sa$ cat test.py 
import os


print ("-------------------List------------------")
mylist = ["Ship", "Boat", "plane"]


if "Ship" in mylist:
    print ("The Ship Found in the list")
else:
    print ("Ship Not found in the list")

print ("This is orginal my %s",mylist)

mylist.append("car")
print ("This is Append Mode", mylist)

mylist.pop()
print ("This is pop mode", mylist)

mylist.insert(1,"car")
print ("This is insert mode", mylist)	

mylist.reverse()
print ("This is Reverse mode", mylist)

#mylist.remove(mylist)
#print ("This Remove first of the list", mylist)

print ("-------------------Tuple ------------------")
my_tuple = ("ship", "boat")
print ("This is my Tuple: ", my_tuple)

my_new_tuple = ("plane", "jetski")
print ("Thi is my new Tuple", my_new_tuple)

my_really_new_tuple = my_tuple + my_new_tuple
print ("Thi is my really new Tuple: ", my_really_new_tuple)


print ("-------------------Ranges------------------")
my_range = list(range(0,22,2))
print ("This example of range: ", my_range)

my_new_range = list(range(0,24,4))
print ("This is new range example: ", my_new_range)
