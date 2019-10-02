def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]


print("input the number: ");
number = int(input());
print("input the end base");
end = int(input());
print("converting ******************************");
print(toStr(number, end));
