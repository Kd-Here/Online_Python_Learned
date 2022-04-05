#Union to add all elements but remove the same element
#intersection will give only the seame vlaue
#symmetric_difference_update() will keeo the element that are not present in both

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
see=set1.union(set2)
print(see)


see=set1.intersection(set2) #Does not print anything bcoz of no element is same
print(see)

see=set1.symmetric_difference(set2)
print(see)


