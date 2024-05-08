def fizzbuzz(int):
    counter = 0
    fizz = 3
    buzz = 5
    while counter <100:
        if (counter%fizz) == 0 and (counter%buzz) == 0:
            print("fizz", "buzz")
        elif (counter%fizz) == 0:
            print("fizz")
        elif(counter%buzz) == 0:
            print("buzz")
        else:
            print(counter)
        counter += 1


counter = 0
game = fizzbuzz(counter)           