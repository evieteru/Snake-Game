list_one = [1, 2, 3]
print(list_one)
list_two = ["a", "b", "c"]
list_three = [list_one, list_two]
list_three[1][0] = "d"
print(list_three)

list_three[0][0] = list_three[0][0] + 1 
print(list_three)

