steps_total = int(input())
x = 0
y = 0

current_operation = "-"
current_var = "x"
steps_needed = 2
current_step = 0
for i in range(steps_total):
    if current_step < steps_needed // 2:
        current_var = "x"
    elif current_step == steps_needed:
        steps_needed += 2
        current_step = 0
        current_var = "x"
        if current_operation == "-":
            current_operation = "+"
        else:
            current_operation = "-"
    else:
        current_var = "y"

    if current_var == "x":
        if current_operation == "-":
            x -= 1
        else:
            x +=1
    else:
        if current_operation == "-":
            y -= 1
        else:
            y += 1
    current_step += 1

print(x, y)
