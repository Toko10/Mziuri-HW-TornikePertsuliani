# with open("Mziuri67.txt", "w") as file:
#     file.write("toko magari biwia")


# with open("Mziuri67.txt", "r") as file:
#     content = file.read()
#     print(content)
#     symbol_count = len(content)
#     print("simboloebis raodenoba ", symbol_count)


# with open("Mziuri67.txt", "a+") as file:
#     file.write("\ntoko ufro magari gaxda")


# file1 = open("Mziuri67.txt", "r")
# content = file1.read()
# file1.close()
# copy_file = open("copy.txt", "w")
# copy_file.write(content)
# copy_file.close()


# with open("Mziuri67.txt", "r") as f1, open("copy.txt", "r") as f2:
#     c1 = f1.read()
#     c2 = f2.read()
# with open("copy2.txt", "w") as f3:
#     f3.write(c1)
#     f3.write("\n")
#     f3.write(c2)


# with open("Mziuri67.txt", "r") as file:
#     text = file.read()
# print(text.upper())


# with open("nomeri7is file", "w") as file:
#     while True:
#         line = raw_input("random text(0 to end): ")
#         if line == "0":
#             break
#         file.write(line + "\n")


with open("Mziuri67.txt", "r") as file1:
    lines = file1.readlines()
with open("output.txt", "w") as file2:
    one_line = " ".join(line.strip() for line in lines)
    file2.write(one_line)
