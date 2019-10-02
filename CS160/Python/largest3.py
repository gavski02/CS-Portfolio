x = int(input('First Number: '));
y = int(input('Second Number: '));
z = int(input('Third Number: '));

if(x > y and x > z):
    print(x);

if(y > x and y > z):
    print(y);

if(z > x and z > y):
    print(z);
else:
    print("Values are all the same");
