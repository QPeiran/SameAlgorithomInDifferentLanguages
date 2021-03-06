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


Q2(1): REC_(k) = Sum[1:k]
Python:
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
#    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)  

JS:
function rec(k)
{
  for (var i = 1,j = 0; i <= k ; i++)
  {
    j += i;
    console.log(j);
  }
}

rec(6);

Q2(2): k!
JS Loop:
function factor(k) 
{
  var result = 1;
  for ( k; k > 1; k--) 
  {
    result *= k;
  }
  return result;
};
console.log(factor(6));

JS Recursion:  
function factorial(k) 
{
  if (k <= 0) 
  { 
    return 1;
  } 
  else 
  {
    return (k * factorial(k - 1));
  }
};
console.log(factorial(6));  

python:
  
def factorial(k):
  if k <= 0:
    return 1
  else:
    return k*factorial(k-1)
  
print(factorial(6))
    
   
    
