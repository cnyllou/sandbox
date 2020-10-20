import sys, random

times = sys.argv[1]
write_file = open('svitrkod.txt', 'w')

for i in range(int(times)):
    write_file.write(str(random.randrange(111111111111,999999999999))+"\n")
