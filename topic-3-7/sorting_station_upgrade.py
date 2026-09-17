label = input()

shape = label[0:4]
color = label[4:7]
size = int(label[7:10])
mass = int(label[10:14])
condition = label[14]

if condition == "D" or size > 50 or mass > 2000:
    destination = "INSPECT"
else:
    if shape == "BALL":
        if color == "RED" and size > 10:
            destination = "B"
        else:
            destination = "A"
    else:
        if shape == "CUBE":
            if (color == "BLU" or color == "GRN") and size <= 10:
                destination = "C"
            else:
                destination = "D"
        else:
            destination = "E"
if shape == "CUBE" and size > 60 and mass > 2500:
    destination = "INSPECT"
else:
    destination = "D"
if condition == "D":
    destination = "INSPECT"
if destination == "INSPECT":
    destination = "HOLD"
else:
    if shape == "CONE" or mass > 1000:
        destination = "CRATE"
    else:
        if shape == "BALL":
            destination = "PADDED"
        else:
            destination = "BOX"

print(destination)
