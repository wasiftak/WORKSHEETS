string = "Emma is a good developer. Emma is also a writer."
count_Emma = string.count("Emma")


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
new_list = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
