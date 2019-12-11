from helper import extractor

def read():
    filea = open(r"/Users/suryakakria/Downloads/SuryaOutputabc (11).txt", "r+")
    c = filea.read()
    ans = []
    ans.append(extractor(c,1))
    write_list_to_file1(ans, "Login.csv")

def write_list_to_file1(abc, filename):
    with open(filename, "w") as outfile:
        for entries in abc:
            for x in entries:
                outfile.write(x)
                outfile.write(",")
            outfile.write("\n")
    print("done")

read()
