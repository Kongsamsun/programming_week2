def number_sum(enter_list):
    list_length = len(enter_list)
    if list_length == 0:
        return 0
    word = enter_list[list_length - 1]
    enter_list.remove(word)
    return int(word) + number_sum(enter_list)

while True:
    try:
        enter_num = input("Enter integers seperated by spaces ==> ")
        split_list = enter_num.split()
        if enter_num == 'done':
            print("Program terminated. Goodbye!!")
            break
        elif len(split_list) <= 1:
            identify = int(split_list[0]) #작성한 한 개의 텍스트가 숫자인지 확인하는 코드
            print("Must enter more than one integer")
            continue
        else:
            result_sum = number_sum(split_list)
            print("The sum of the input integers is ==> ", result_sum)
    except:
        print("Must enter integers seperated by spaces")
        continue