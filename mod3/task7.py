num_list = input().split()
print(True if len(num_list) != len(set(num_list)) else False)
