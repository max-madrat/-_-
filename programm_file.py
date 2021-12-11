data = []
with open("data.txt") as f:
    for line in f:
        for x in line.split():
            data.append(float(x))
print(data)

dsagfdafaesgasdf
def min_number(list_of_data):
    try:
        low = list_of_data[0]
        for i in range(len(list_of_data)):
            if low >= list_of_data[i]:
                low = list_of_data[i]
        return low
    except OverflowError:
        return "Слишком большие данные"


def max_number(list_of_data):
    try:
        high = list_of_data[0]
        for i in range(len(list_of_data)):
            if high <= list_of_data[i]:
                high = list_of_data[i]
        return high
    except OverflowError:
        return "Слишком большие данные"


def multiplication(list_of_data):
    try:
        mult = 1
        for i in range(len(list_of_data)):
            mult = mult * list_of_data[i]
        return mult
    except OverflowError:
        return "Слишком большие данные"


def total_sum(list_of_data):
    try:
        amount = 0
        for i in range(len(list_of_data)):
            amount = amount + list_of_data[i]
        return amount
    except OverflowError:
        return "Слишком большие данные"


def average(list_of_data):
    try:
        amount = 0
        for i in range(len(list_of_data)):
            amount = amount + list_of_data[i]
        average_num = amount / len(list_of_data)
        return average_num
    except OverflowError:
        return "Слишком большие данные"


print(min_number(data))
print(max_number(data))
print(multiplication(data))
print(total_sum(data))
print(average(data))
