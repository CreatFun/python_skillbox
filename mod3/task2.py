number = int(input())
codes_list = [bin(number)[2:],oct(number)[2:], hex(number)[2:]]
print(codes_list[0] + ", " + codes_list[1] + ", " + codes_list[2])
