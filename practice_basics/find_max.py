user_list1 = []
i = 1
def enter_list(user_list):
   num = 0
   while(num != -1):
        num = int(input("enter your numbers(-1 to stop) : "))
        if (num != -1):
            user_list.append(num)
   return user_list

def findmax(user_list):
    max = user_list[0]
    for num in user_list:
        if (num > max ):
            max =  num
    return max





print("your list is : ", enter_list(user_list1))
print("the maximum number in your list is : ", findmax(user_list1))
