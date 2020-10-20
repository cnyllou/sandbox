import sys, random

read_file = open(sys.argv[1], 'r')
write_file = open(sys.argv[2], 'w')

gadi = []
for line in read_file:
    stripped_line = line.strip()
    gadi.append(stripped_line)

read_file.close()

for g in gadi:
    rand_dienas = str(random.randrange(1,29)).zfill(2)
    rand_meness = str(random.randrange(1,13)).zfill(2)
    num = 100-int(g)+20
    if num >= 100:
        num = str(abs(num) % 100) + "0"



    pk_p2 =  str(random.randrange(1,100)).zfill(2) + str(random.randrange(1,100)).zfill(2) + str(random.randrange(1,10))
    pk_p1 = rand_dienas + rand_meness + str(num)

    write_file.write(pk_p1 + "-" + pk_p2 + "\n")

    #write_file.write(g + "\n")
