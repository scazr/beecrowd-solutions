OUTPUTS = []

while True:
    entrada = input()
    entrada = entrada.split(" ")
    key = entrada[0]
    value = [*entrada[1]]
    newValue = []

    if entrada[0] == "0" and entrada[1] == "0": break
    
    for digit in value:
        if digit != key: newValue.append(digit)

    if newValue == []: newValue = 0;
    else: newValue = int("".join(newValue))
    OUTPUTS.append(newValue)
 
for _ in OUTPUTS: print(_)
