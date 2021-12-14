import codecs
import re

def compress(filename):
    f = codecs.open(filename,"r","utf-8").read()
    buffer= ""
    output=""
    i=0
    while(i<len(f)):
        character= f[i]
        if buffer+character in output:
            buffer+=character
            i+=1
        else:
            if len(buffer)> (len(str(len(buffer)))+len(str(output.find(buffer)))+3):
                output += "("+str(output.find(buffer))+","+ str(len(buffer))+")"
            else:
                output += buffer+character
                i+=1
            buffer=""
    print("Done")
    file = codecs.open("compressed.txt", "w","utf-8")
    file.write(output)
    file.close()

def decompress(filename):
    f = codecs.open(filename,"r","utf-8").read()
    output=f
    regex = re.findall("(\([0-9]+,[0-9]+\))", output)  
    for sub in regex:
        temp = sub.replace("(","").replace(")","")
        index = int(temp.split(",")[0])
        length = int(temp.split(",")[1])
        output=output.replace(sub,f[index:(index+length)])
    file = codecs.open("decompressed.txt", "w","utf-8")
    file.write(output)
    file.close() 

compress("files\\informatyczny.txt")
decompress("compressed.txt")
