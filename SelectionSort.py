def selection_sort(array:list[int], order:str = 'asc')-> list[int]:
     for i in range(n):
         index = i
         minimum = array[i]
         for j in range(i+1,n):
             if order == 'asc':
                 if array[j]< minimum:
                     minimum = array[j]
                     index = j
                     array[i], array[index] = array[index], array[i]
             elif order == 'dsc':
                 if array[j] > minimum:
                     minimum = array[j]
                     index = j
                     array[i], array[index] = array[index], array[i]
     return array

arr = [13, 4, 9, 5, 3, 16, 12]
arr = [2,1,50,35,100,69,4,10]
n = len(arr)
order = input("asc or dsc: ")
print(selection_sort(arr,order))