def merge_sort(array:list[int], order:str = 'asc'):
   temp=array
   if len(array) > 1:
       temp=[]
       mid = len(array) // 2

       L = array[:mid]
       R = array[mid:]
       

       L=merge_sort(L, order)
       R=merge_sort(R, order)

       i = 0
       j = 0
       

       while i < len(L) and j < len(R):
           
           if order == 'asc':
               if L[i]<R[j]:
                   temp.append(L[i])
                   i +=1
               else:
                   temp.append(R[j])
                   j += 1

           elif order== 'dsc':
           
               if L[i] > R[j]:
                   temp.append(L[i])
                   i += 1
               else:
                   temp.append(R[j])
                   j += 1
           
           


       while i < len(L):
           temp.append(L[i])
           i+=1
       while j < len(R):
           
           temp.append(R[j])
           j+=1
       

   return temp

arr = [13, 4, 9, 5, 3, 1, 16, 12]
# arr = [12, 2, 4]

order = input("asc or dsc: ")
print(order)
temp = []
print(merge_sort(arr,order))