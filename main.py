import pandas as pa

data={
    "name":["mitsi","viarrah","jessica","miko","jack","raf","cade","sam"],
    "class":[9,10,12,7,8,6,22,14],
    "age":[15,16,18,14,16,12,28,20],
    "favsub":["english","biology","herbiology","social","physics","computer science","economics","history"]
}

myd=pa.DataFrame(data)

#print(myd)

#print(myd["name"])

myd2=pa.DataFrame(data,index=["st1","st2","st3","st4","st5","st6","st7","st8"])
#print(myd2["name"])

myd["math mark"]=[98,96,70,85,80,97,95,90]
print(myd)

#print(myd.sort_values("age"))

print(myd.info())