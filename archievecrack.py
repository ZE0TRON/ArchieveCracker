#Made By Ze0tron
import zipfile
import rarfile
from sys import argv
import string
def usage():
    print("Usage : \n archievefile -minl minumumlenght -maxl maximumlenght \
          \n -wl contains words lowercase \n -wu contains words uppercase \n -n containsnumbers \n -s contains special charachters \n -p path to passwordlist file \n -h help")
ishelp=0
minl=0
maxl=-1
if(argv[1]=="-h"):
    usage()
    ishelp=0
elif(argv[1].split(".")[1]=="zip"):
    myzip = zipfile.ZipFile(argv[1])
    filetype="zip"
elif(argv[1].split(".")[1]=="rar"):
    myrar=rarfile.RarFile(argv[1])
    filetype="rar"
i=2
hasfile=0
elems=[]

while(i<len(argv)):
    if(argv[i]=="-minl"):
        minl=int(argv[i+1])
        i+=2
    elif(argv[i]=="-maxl"):
        maxl=int(argv[i+1])
        i+=2
    elif(argv[i]=="-wl"):
        for elem in string.ascii_lowercase:
            elems.append(elem)
        i+=1
    elif(argv[i]=="-wu"):
        for elem in string.ascii_uppercase:
            elems.append(elem)
        i+=1
    elif(argv[i]=="-n"):
        for elem in ["0","1","2","3","4","5","6","7","8","9"]:
            elems.append(elem)
        i+=1
    elif(argv[i]=="-s"):
        for elem in string.punctuation:
            elems.append(elem)
        i+=1
    elif(argv[i]=="-p"):
        filename=argv[i+1]
        hasfile=1
        i+=2
    else():
        usage()
        break
found=0
if(filetype=="zip"):
    if(!ishelp and !hasfile):
        for i in range(minl,maxl+1):
            print("Trying length of : ",i)
            if(found):
                break
            length=i
            counters=[0 for _ in range(i)]
            current=i-1
            while counters[0]<len(elems)-1:
                pasw=""
                for j in range(i):
                    pasw+=elems[counters[j]]
                pointer=current
                while(not(counters[pointer]<len(elems)-1)):
                    pointer-=1
                counters[pointer]+=1
                for c in range(pointer+1,i):
                    counters[c]=0
                try:
                    myzip.extractall(pwd=pasw.encode())
                    print("Password found")
                    print(pasw)
                    found=1
                    break
                except:
                    pass
    elif(!ishelp):
        passfile=open(filename,"r")
        for pasw in passfile.readlines():
            pasw=pasw.rstrip()
            try:
                myzip.extractall(pwd=pasw.encode())
                print("Password found")
                print(pasw)
                found=1
                break
            except:
                pass

elif(filetype=="rar"):
    if(!ishelp and !hasfile):
        for i in range(minl,maxl+1):
            print("Trying length of : ",i)
            if(found):
                break
            length=i
            counters=[0 for _ in range(i)]
            current=i-1
            while counters[0]<len(elems)-1:
                pasw=""
                for j in range(i):
                    pasw+=elems[counters[j]]
                pointer=current
                while(not(counters[pointer]<len(elems)-1)):
                    pointer-=1
                counters[pointer]+=1
                for c in range(pointer+1,i):
                    counters[c]=0
                try:
                    myrar.extractall(pwd=pasw.encode())
                    print("Password found")
                    print(pasw)
                    found=1
                    break
                except:
                    pass
    elif(!ishelp):
        passfile=open(filename,"r")
        for pasw in passfile.readlines():
            pasw=pasw.rstrip()
            try:
                myrar.extractall(pwd=pasw.encode())
                print("Password found")
                print(pasw)
                found=1
                break
            except:
                pass
