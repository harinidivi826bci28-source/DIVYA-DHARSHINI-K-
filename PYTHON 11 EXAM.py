list1=[1,2,3,4,4,5,6,7]
new_set1=(set(list1))
list2=[7,14,21,28,35,49]
new_set2=(set(list2))
new_set=new_set1.intersection(new_set2)
print(sorted(new_set))
