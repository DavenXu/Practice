def reverse(lst):
    result = []

    for element in lst :
        result.insert(0,element)
        
        print(element)
    return result

list1 = [2, 4, 6]

list2 = reverse(list1)
print(list2)