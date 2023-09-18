# arr=[13, 5, 11, 7, 23, 15]

# 선택정렬
# for i in range(len(arr)):
#     idx=i
#     for j in range(i+1, len(arr)):
#         if arr[idx]> arr[j]:
#             idx=j
    
#     tmp=arr[i]
#     arr[i]=arr[idx]
#     arr[idx]=tmp

# print(arr)


# 버블정렬
# for i in range(len(arr)):
#     for j in range(i, len(arr)-1-i):
#         if arr[j]> arr[j+1]:
#             tmp=arr[j+1]
#             arr[j+1]=arr[j]
#             arr[j]=tmp

# print(arr)

# 삽입정렬
# for i in range(1, len(arr)):
#     tmp=arr[i]
#     for j in range(i-1, -1, -1):
#         if tmp < arr[j]:
#             arr[j+1]=arr[j]
#             arr[j]=tmp
#         else:
#             break
# print(arr)

# 이분검색
# arr=[12, 23, 32, 57, 65, 81, 87, 99]
# start=0
# end=len(arr)-1
# key=int(input())
# while True:
#     mid=(start+end)//2
#     if arr[mid]==key:
#         print(mid)
#         break
#     elif arr[mid]> key:
#         end=mid-1
        
#         print(arr[mid])
#     elif arr[mid] < key:
#         start= mid+1
#         print(arr[mid])

# 이진 트리 순회방법    
tree=[1,2,3,4,5,6,7]

# preoder (root, left, right)
def preoder(root):
    


