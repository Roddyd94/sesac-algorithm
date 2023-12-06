from collections import defaultdict

my_dict1 = defaultdict(int)
my_dict2 = defaultdict(str)
my_dict3 = defaultdict(list)
my_dict4 = defaultdict(set)

print(my_dict1)
print(my_dict2)
print(my_dict3)
print(my_dict4)

my_dict1["my_key"] += 1
print(my_dict1)
print(my_dict1)
