def get_number(number):
    if number > 0:
        return number
    else: 
        return ' negative number'
prev_list =[-1,10,-20,2,-90,60,45,20]
new_list = [get_number(number)for number in prev_list]
print(new_list)