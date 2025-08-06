import re
#functions
#to find the average
def grade(a,b,c,d,e):
    av=(int(a)+int(b)+int(c)+int(d)+int(e))/5
    if av>75:
        return 'A'
    elif av>50:
        return 'B'
    elif av>25:
        return 'C'
    else:
        return 'Fail'

#to insert records
def store(fname,name,a,b,c,d,e):
    with open(fname,'a') as f:
        f.write("\n")
        f.writelines([name+",",a+",",b+",",c+",",d+",",e+",",grade(a,b,c,d,e)])

#to retrieve based on name
def retrieve(fname,name):
    with open(fname) as f:
        r=f.readlines()   #each record will be element of the list in form of comma sep. string
        for i in r: 
            if(name in i):
                result=[e for e in re.split(r'\s*,\s*',i) if e] #using regex we split the comma separated record
                return result
        
        
            

