print("what is your goal?")
goals = []
times = []
userinput = input()
timeinput = ""
while (timeinput.find(":") == -1):
    print("Please the time that you want reminding of: ",userinput," including :" )
    timeinput = input()
while userinput != "" and timeinput != "":
    goals.append(userinput)
    times.append(timeinput)
    print("Please give your next goal.")
    userinput = input()
    if userinput != "":
        while (timeinput.find(":") == -1):
            print("Please the time that you want reminding of: ",userinput," including :" )
            timeinput = input()
print(goals)
print(times)
