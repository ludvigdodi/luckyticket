print("\nЩасливий квиток!!!\n")
ticket_num = input("Введіть шестизначне число: ")
ticket_num_list = list(ticket_num)

try:
    list_of_numbers = [int(n) for n in ticket_num_list]
    def sum_of_digits(list_of_numbers):
        if len(list_of_numbers) == 6:
            a = (list_of_numbers[0]+list_of_numbers[1]+list_of_numbers[2])
            b = (list_of_numbers[3]+list_of_numbers[4]+list_of_numbers[5])
            print("Вітаю! Квиток щасливий!!!" if a == b else "Нажаль квиток не щасливий!!!")
        else:
            print("Ви ввели не шестизначне число!!!")

    sum_of_digits(list_of_numbers)
except:
    print("Ви ввели не число!!!")
