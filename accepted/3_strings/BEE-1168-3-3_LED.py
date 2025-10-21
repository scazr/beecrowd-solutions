leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for n in range(int(input())):
    led_count = 0
    for v in input(): led_count += leds[int(v)]
    print(led_count, 'leds')