total = int(input("How many numbers?"))
list=[]
for i in range(total):
    x = int(input("Enter your number: "))
    list.append(x)
    
list.sort()
print(list)
n = int(input("Enter the number you want to find: "))

search = False
start = 0
end = len(list)-1

while start <= end:
    mid = (start+end)//2
    if list[mid] == n:
        print("Found at index no. ",mid)
        search = True
        break

    elif list[mid] > n:
        end = mid - 1

    else:
        end = mid + 1

if search == False:
    print("Value not found!")

#Time Complexity of the above Algorithm is O(log(n)).