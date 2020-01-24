with open("data.txt", "r") as f:
    thing = f.read()

with open("data.txt", "a") as f:
    f.write(thing)
    f.write(thing)

print(thing)