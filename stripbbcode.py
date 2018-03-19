"""
This is just a script to convert ascii art
This varient merely strips all bbcode
Tyler Hart
luna@mail.rit.edu
2017-09-19
"""

import sys

def main():
    if (len(sys.argv)<3):
        print("Usage: bbcode2bash [infile] [outfile]")
    else:
        bbcode2bash(sys.argv[1], sys.argv[2])

def bbcode2bash(infilename, outfilename):
    infile=''
    of = open(outfilename, 'w')
    with open(infilename, 'r') as f:
        infile=f.read()
    hexCode=""
    tripValue=False
    tripBB=False
    tripNoRead=False
    for i in range(len(infile)):
        #handles bb close statements
        #print(tripValue,tripBB,tripNoRead)
        if(tripNoRead):
            if(infile[i]=="]"):
                tripNoRead=False
                tripBB=False
        #handles bb open brackets
        elif(infile[i]=="["):
            tripBB=True
            #checks if close statement
            if(infile[i+1]=="/"):
                tripNoRead=True
        #handles bb content
        elif tripBB==True:
            if(infile[i]=="]"):
                tripBB=False
                if tripValue==True:
                    tripValue=False
                    hexCode=""
            elif(tripValue==True):
                hexCode+=infile[i]
            elif(infile[i]=="=" and infile[i-5:i]=="color"):
                tripValue=True
        #regular character
        else:
            of.write(infile[i])


main()
