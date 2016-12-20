file = open("donow.txt", "w")

for n in range(1,6):
    file.write("Hi, I'm line #{}.\n".format(n))