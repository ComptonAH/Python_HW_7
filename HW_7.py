# sentence = "para-ra-ram ram-pam-papam pa-ra-pa-da" 
# p_l = sentence.split()
# int_p_l = list()
# for phrase in p_l:
#     char_counter = phrase.count('a')
#     int_p_l.append(char_counter)
# for i, char in enumerate(int_p_l):
#     if TypeError(i+1):
#         break
#     if int_p_l[i] != int_p_l[i+1]:
#         print('Пам парам')
#         break
# print('Парам пам-пам')
# Second solution w/o first 'if':
# if int_p_l[i] != int_p_l[i+1]:
#     print('Пам парам')
#     break



# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
def operation(symbol):
    if symbol == '*':
        return '*'
    elif symbol == '+':
        return '+'
    
def print_operation_table(operation, row_number, column_number, num_rows=6, num_columns=6):
    if operation == '*':
        array_2D = [[i*a for i in range(1,num_rows+1)] for a in range(1,num_columns+1)]
        for each_row in array_2D:
            print(*each_row)
        print(f'The result is {array_2D[column_number-1][row_number-1]}')
    elif operation == '+':
        array_2D = [[i for i in range(1,num_columns+1)] for a in range(1,num_rows+1)]
        i = 1
        for row in array_2D[1:]:
            row[0] = row[i] 
            for i_r, r_e in enumerate(row[1:]):
                row[i_r+1] = row[0] + array_2D[0][i_r+1]
            i += 1
        for each_row in array_2D:
            print(*each_row)
        print(f'The result is {array_2D[column_number-1][row_number-1]}')



symbol = input("Enter the operation's symbol: ")
row_number = int(input("Enter the row's number: "))
column_number = int(input("Enter the columnm number: "))

print_operation_table(symbol, row_number, column_number)