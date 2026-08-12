arr=[6,8,3,4,9]
n=len(arr)
for i in range(n):

        
        si = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[si]:
                si = j  
                
        
        arr[i], arr[si] = arr[si], arr[i]

print("Sorted array:", arr)





