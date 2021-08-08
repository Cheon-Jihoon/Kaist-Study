file = open("average-latitude-longitude-countries.csv", "r")
lines = [i.strip() for i in file.readlines()]
del lines[0]
result1=[]
result2=[]
for line in lines:
    line = line.split(",")
    if len(line) == 5:
        print(line[0], line[1] + ","+ line[2])
    else:
        print(line[0], line[1])
print(len(lines))