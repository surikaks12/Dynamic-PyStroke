from helper import extractor
import os

def reader():
    filea = open(r"/Users/suryakakria/Downloads/Registration (12).txt", "r+")
    c = filea.read()
    z = c.split("\nxxxxxx\n")
    i = 0
    ans = []
    while i < len(z):
        ans.append(extractor(z[i], i))
        i = i + 1
    #ans = extractor(z[0], 0)
    write_list_to_file(ans, "tester1.csv")

def write_list_to_file(abc, filename):
    with open(filename, "w") as outfile:
        for entries in abc:
            for x in entries:
                outfile.write(x)
                outfile.write(",")
            outfile.write("\n")
    print("done")
# def write_list_to_file(guest_list, filename):
#     """Write the list to csv file."""
#
#     with open(filename, "w") as outfile:
#         for entries in guest_list:
#             outfile.write(entries)
#             outfile.write(", ")
#     print("done")

reader()
