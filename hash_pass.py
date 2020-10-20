import sys

from werkzeug.security import check_password_hash, generate_password_hash

read_file = open(sys.argv[1], 'r')
write_file = open(sys.argv[2], 'w')

hashed_passwords = []
for line in read_file:
    stripped_line = line.strip()
    hashed_passwords.append(generate_password_hash(stripped_line))

read_file.close()

for passw in hashed_passwords:
    write_file.write(passw + "\n")
