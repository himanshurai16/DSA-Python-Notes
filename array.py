"""Array is a collection of elements stored at contiguous memory locations,
used to hold multiple values of the same data type."""
import array
val = array.array('i',[1,2,3,4,5,6])
for i in range(0,6):
    print(val[i], end=" ")


print('/n')
for x in val:
    print(x, end= " ")

print('/n')
print(val.typecode)

val.reverse()
for i in range(0,len(val)):
       print(val[i], end=" ")


val.insert(1,50) #for insert as a position
val.append(100) # for insert at a last
copyarray = array.array(val.typecode,(x for x in val))
for i in range(0,len(val)):
       print(copyarray[i], end=" ")

copyarray = array.array(val.typecode,(x for x in val))
copyarray.pop(3) #for delete any index element
copyarray.remove(5) # for delete any specific element
    #index
a = val[::-1]
for i in range(0,len(a)):
       print(a[i], end=" ")
       # for search the element index
i = val.index(5)
print(i)

