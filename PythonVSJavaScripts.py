Q1: An Array [A,B,C,D,E,F,G], filter the elements with odd index

Python:

thislist = ["A","B","C","D","E","F","G"]
for x in range(0,len(thislist)):
  if x%2 == 0:
    print(thislist[x])
  else:
    print("Eliminated")
    
JavaScript:
var thislist = ["A","B","C","D","E","F","G"];
for (var i =0; i <= thislist.length; i+=2) 
{console.log(thislist[i]+"");}
