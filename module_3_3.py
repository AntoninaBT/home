def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c,)
    print(a, b)
    print(a, c)

print_params()
#print_params(a, b)
#print_params(b, c)
#print_params(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
values_list_2 = ["gggyyddx", 9898998]

print_params(*values_list_2, 42)

def print_params(*a):
    print(a)
values_list = [88, "row", True]
values_dict = {"F": 7, "ll": "move", "gy": True}
print_params(*values_list)
print_params(*values_dict)
def print_params(**a):
    print(a)
print_params(**values_dict)

