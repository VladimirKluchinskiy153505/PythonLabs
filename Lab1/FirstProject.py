# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def calculation(a,b,operation):
    try:
        x=float(a)
        y=float(b)
        match operation:
            case "add":
                res=x+y
            case "sub":
                res=x-y
            case "mult":
                res=x*y
            case "div":
                res= x/y
    except ValueError as error:
        print('Imposible value')
    except ZeroDivisionError as error1:
        print('zero division')
    else:
        return res
def sort_list(list):
    new_list=[]
    for i in list:
        try:
            if int(i)%2==0:
                new_list.append(i)
        except ValueError as error:
            print('List contains not only numbers')
    return new_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('World')

    print("Enter two numbers")
    a=input()
    b=input();
    print("Enter Operation:add,sub,mult,div")
    operation=input()
    print(calculation(a,b,operation))

    input_string = input('Enter elements of a list separated by space\n')
    list=input_string.split()
    print('list: ',list)
    print('sorted_list: ',sort_list(list))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
