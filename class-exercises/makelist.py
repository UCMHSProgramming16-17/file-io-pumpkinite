# create new file to contain list
listfile = open("userlist.txt", "w")

# create 10 list entries
for n in range(0,10):
    # take user input and store in temporary variable
    entry = input("Item #{}: ".format(str(n+1)))
    # write entry to file
    listfile.write("{}. {}\n".format(str(n+1), entry))