#!usr/bin/env python
import random
import sys
import subprocess

def main():

    f = open('input.txt', 'w')
    f.write("{\n")
    f.write('"message": "'+ sys.argv[2]+'",\n')
    f.write('"recipients": [')
    
    phone_total = int(sys.argv[1])

    for x in range(phone_total):
        if x == phone_total - 1:
            f.write('"'+str(random.randint(1000000000, 9999999999)) +'"]\n')
        else:
            f.write('"'+str(random.randint(1000000000, 9999999999)) +'",')

    f.write('}')



if __name__ == "__main__":
    main()
