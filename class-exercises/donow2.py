import csv

file = open("csvdonow.csv", "w")

writer = csv.writer(file, delimiter=",")

for n in range(5,10):
    writer.writerow([n, (n + 50) % 4, n*8])
    
file.close()