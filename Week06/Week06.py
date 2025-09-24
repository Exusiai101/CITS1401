# FIle processing
def emails():
    infilename = input("File name which has details of students")
    outfilename = input("File name of destination file with emails")
    outfile = open(outfilename, "w")
    infile = open(infilename, "r")
    for line in infile:
        # ID followed by 2 character of first name, followed by dot then last name
        ID, fname, lname = line.split(",")
        email_add = ID + fname[0:2] + "." + lname[:-1]+ "@student.uwa.edu.au\n"
        outfile = outfile.write(email_add)
