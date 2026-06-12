num_list= [20,50,66,80,10,5]
userInput= int(input("Enter a search number: "))
# for i in range(len(num_list)):

#     if userInput == num_list[i]:
#         print(f"The number in found in the list position {i+1}.")
#         break 

# else: 
#     print("The number is not in the list.")
condition = False
index = 0
for i in range(len(num_list)):

    if userInput == num_list[i]:
        condition = True
        index= i
        break 

    else: 
        condition = False

if condition == True:
    print(f"The number is found in the list, position {index+1}")
else:
    print("The number is not in the range.")