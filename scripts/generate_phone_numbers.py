#!usr/bin/env python
import random
import sys
import subprocess

def main():
    file_string = "input_" + sys.argv[1] + "_phone_numbers.txt"
    
    f = open(file_string, 'w')
    f.write("{\n")
    f.write('"message": "'+ sys.argv[2]+'",\n')
    f.write('"recipients": [')
    

    try:
        phone_total = int(sys.argv[1])
        if phone_total < 1:
            print "Please provide a number that is greater than 0"
    except ValueError:
        print "Please input a positive integer!"
        
    for x in range(phone_total):
        if x == phone_total - 1:
            f.write('"'+str(random.randint(1000000000, 9999999999)) +'"]\n')
        else:
            f.write('"'+str(random.randint(1000000000, 9999999999)) +'",')

    f.write('}')



if __name__ == "__main__":
    main()
