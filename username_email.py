import sys, random, re


user_file = open(sys.argv[1], 'r')
write_file = open(sys.argv[3], 'w')

users_array = []
user_email_array = []

for line in user_file:
    users_array.append(line)


if '@' in sys.argv[2]:
    for u in users_array:
        write_string = u.strip() + sys.argv[2] + "\n"
        print(write_string)
        write_file.write(write_string.lower())


else:
    email_file = open(sys.argv[2], 'r')

    email_array = []


    for line in email_file:
        email_array.append(line)

    for i, domain in enumerate(email_array):
        m = re.search("([@].+)", domain).group()
        write_string = users_array[i].strip() + m + "\n"
        print(write_string)
        write_file.write(write_string.lower())
