import sys

project_file = open(sys.argv[1], 'r')
employ_file = open(sys.argv[2], 'r')
write_file = open(sys.argv[3], 'w')

projects = []
employees = []
output = []

difference = 0
checksum = 0

for p in project_file:
    projects.append(p.strip())

for id, e in enumerate(employ_file):
    emp = []
    emp.append(id+1)
    emp.append(int(e.strip()))
    employees.append(emp)



employees = sorted(employees, key=lambda x: x[1])
print(employees)

for id, count in employees:

    count = int(count) + difference
    print("starting count - ", count)
    proj_count = 0
    if difference < 0:
        proj_count += 1
    projects_for_office = []
    projects_for_office.append(id)

    while count > 0:

        if count > 5:

            print("6 or more:" + str(count), end="\n")
            count -= 6
            proj_count += 1
        else:
            print("Less than 6:" + str(count), end="\n")
            count -= 5
            proj_count += 1

    difference = count
    checksum += proj_count
    projects_for_office.append(proj_count)
    print("Difference is" + str(difference))
    print("Projects for office: {} = {}".format(employees[1], proj_count))
    print("\n\n")
    output.append(projects_for_office)

print("Total projects - " + str(checksum-1))
print(output)

for x, y in output:
    write_file.write(str(y) + "\n")
