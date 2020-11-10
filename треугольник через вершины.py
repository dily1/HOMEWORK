import math;
xa = int(input("Введите координату х первой точки: "));
ya= int(input("Введите координату у первой точки: "));
xb = int(input("Введите координату х второй точки: "));
yb= int(input("Введите координату у второй точки: "));
xc = int(input("Введите координату х третьей точки: "));
yc= int(input("Введите координату у третьей точки: "));

a = math.sqrt((xa - xb)**2 + (ya -yb)**2);
b = math.sqrt((xb - xc)**2 + (yb -yc)**2);
c =  math.sqrt((xa - xc)**2 + (ya -yc)**2);
p = a+b+c;
p = p/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c));
p = p//1;
S = S//1

#print (a,b,c,p,S);
print ("периметр треугольника =",p,"\n Площадь треугольника =",S);

