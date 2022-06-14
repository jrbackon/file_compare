
# open the two files as variables and read contents into a list.

file1 = input("Enter the path of the first file to compare: ")
file1_list = []

file2 = input("Enter the path of the second file to compare: ")
file2_list = []

with open(file1, 'r') as f:
    file1_list = f.readlines()
    for index in range(len(file1_list)):
        file1_list[index] = file1_list[index].strip("\n")

with open(file2, 'r') as g:
    file2_list = g.readlines()
    for index in range(len(file2_list)):
        file2_list[index] = file2_list[index].strip("\n")
    

# compare both lists and write matching entries into a new list.
matching_list = []
for item in file1_list:
    if item in file2_list:
        matching_list.append(item)

# output the matching list to a new file.
with open("/Users/jbackon/Desktop/compared_file.txt", 'w') as h:
    for item in matching_list:
        h.write(item)
        h.write("\n")
