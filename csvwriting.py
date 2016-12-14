# import csv
import csv

# create file
csvfile = open("csvfile.txt", "w")

# create csvwriter
csvwriter = csv.writer(csvfile, delimiter=",")

# write information
csvwriter.writerow(["n", "standard letter"])
for n in range(0,26):
    csvwriter.writerow([n+1, "abcdefghijklmnopqrstuvwxyz"[n]])

# close file
csvfile.close()