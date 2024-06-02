def quickSort(array, low, high):
   if low < high:
       pivot = array[low]
       i = low
       j = high
       # print("before while:", i,j, pivot)

       while (i < j):
           x = True
           y = True
           while x:
               if array[i]<=pivot:
                   if i >=0 and i <len(array)-1:
                       i+=1
                   else:
                       x=False
               else:
                   x=False
           print("first while done")

           while y:

               if (array[j] > pivot):
                   # print("loop 2:")
                   # print(j, array[j],pivot)
                   if i >= 0 and i < len(array) - 1:
                       j -= 1
                   else:
                       y=False
               else:
                   y = False

           if (i < j):
               (array[i], array[j]) = (array[j], array[i])
               # print(array, i , j)
       # print("while done")
       (array[low], array[j]) = (array[j], array[low])
       # print(array, low, j)


       quickSort(array, low, j-1)
       # print("left side:")
       # print(array, j+1, high)
       quickSort(array, j + 1, high)
   return array


arr = [810, 1000, 2110, 44, 39, 960]
size = len(arr)-1
print(quickSort(arr, 0, size))