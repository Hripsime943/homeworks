def operate(a, b, operation):
   return operation(a,b)
result = operate(5,6,lambda x,y: x*y)
print (result)
