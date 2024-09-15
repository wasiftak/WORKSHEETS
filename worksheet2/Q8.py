exam_st_date = (11, 12, 2014)
print(f"The exams will start from {exam_st_date[0]}-{exam_st_date[1]}-{exam_st_date[2]}")


numbers = [10, 15, 20, 25, 30, 35, 40]  # Example list
divisible_by_5 = [num for num in numbers if num % 5 == 0]


def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return not is_even(num)


