import sys, random

write_file = open(sys.argv[1], 'w')

for i in range(int(sys.argv[2])):
    write_file.write("Bite 2" + str(random.randrange(1000000,9999999))+ "\n")
