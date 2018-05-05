# Tuples - These can't be changed unlike arrays

tup1 = ('a','hello',12,90.4)
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d","e"
tup4 = ()
tup5 = (1,)
tup6 = (2)

print tup1[0]
print tup1[0:4]
print tup4
print tup5
print tup1 + tup3
#length of a tupple (Here tupple is an argument)
print len((1,2,3))
#Using a comma after first element
print (tup6)*4
print (tup5)*4
#Check if nth element exists in a tupple
print 5 in tup2
print 8 in tup2
#iteration
for x in (1,2,3):
    print x
    
tup = "qwerty",1,5,45,-9
print tup
#deleting a tupple
del tup
print tup
