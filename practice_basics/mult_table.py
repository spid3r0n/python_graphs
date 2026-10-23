n = int(input("enter the number "))

table = []

for i  in range(1,11) :
    print(f"{n} x {i} = {n*i}")
    table.append(n*i)
 
print("from table : ",table)
