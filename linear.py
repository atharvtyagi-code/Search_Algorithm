#list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
total = int(input("How many numbers?"))
list=[]
for i in range(total):
    x = int(input("Enter your number: "))
    list.append(x)
    
n = int(input("Enter the number you want to find: "))
if n in list:
    index = 0
    for i in list:
        if i == n:
            print("Number found ",list[index])

        index = index+1

else:
    print("It's not in the list.")

#Time Complexity of the above Algorithm is O(n).