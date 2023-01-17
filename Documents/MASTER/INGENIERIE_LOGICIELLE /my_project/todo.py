"""The sys module provides functions and variables to interact with the Python interpreter"""
import sys #import sys library
import os.path #import os.path library

ADN_LIST=("A","C","G","T") #creating a list of existing nucleotides

def adn_read(fastafile):
    """ function that takes effect on fasta files and
    retrieve the characters are not nucletoides in sequence"""
    #In case file ends with ".fa", ".faa" or ".fasta"
    if fastafile.endswith((".faa",".fa",".fasta")):
        #print the FASTA file and it's name is in the format correct
        print("FASTA file " + str(fastafile) + " format correct")
        #open the file in reading mode as file
        with open(fastafile,"r", encoding="utf-8") as file:
            #returns a list containing each line in the file as a list item.
            lines = file.readlines()
            #initiate the line counter
            line_counter = 0
            #initiate emply variable which will contain the header of sequence
            header = ""
            #for each line in "lines" variable
            for line in lines:
                #synchronize the counter (add one)
                line_counter += 1
                #if the first character of the line is ">"
                if line[0] == ">":
                    #remove last special characters (like "\n")
                    header = line.strip()
                #otherwise
                else:
                    line = line.strip()
                    # turn all characters of the line into capital letters
                    line = line.upper()
                    #initiate the column counter
                    column_counter = 0
                    # for each character in line
                    for char in line:
                        #synchronize the column counter (add one)
                        column_counter += 1
                        #if character isn't in the list (isn't A,C,G or T)
                        if char not in ADN_LIST:
                            #create a variable which contains the character followed
                            #by the line,column,sequence, and file name of the character
                            error= (char  + " It's not a nucl in line " + str(line_counter)
                            + " and column "+ str(column_counter)
                            + " for sequence " + header[1:]
                            + " in file" + str(fastafile) + "\n")
                            #create and open an empty file
                            with open("error_file.faa","a",encoding="utf-8") as error_file:
                            #insert content error variable in this file
                                error_file.write(error)
    else:
        #indicate to user to use correct file format
        print("Please use faa/fa file format")
#for each argument given by user
for arg in sys.argv[1:]:
    #to check whether the specified path exists or not
    #Returns Boolean value
    #in the case where the answer is False
    if os.path.exists(arg) is False:
        #print the fact that the file doesn't exists
        print("The file" + str(arg)+ "does not exist")
    else:
        #run the function
        adn_read(arg)
