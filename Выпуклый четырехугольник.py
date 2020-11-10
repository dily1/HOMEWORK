import math;
xa = int(input("Введите координату х первой точки: "));
ya= int(input("Введите координату у первой точки: "));
xb = int(input("Введите координату х второй точки: "));
yb= int(input("Введите координату у второй точки: "));
xc = int(input("Введите координату х третьей точки: "));
yc= int(input("Введите координату у третьей точки: "));
xd = int(input("Введите координату х четвертой точки: "));
yd = int(input("Введите координату у четвертой точки: "));

a = math.sqrt((xa - xb)**2 + (ya -yb)**2);
bc = math.sqrt((xb - xc)**2 + (yb -yc)**2);
c =  math.sqrt((xa - xc)**2 + (ya -yc)**2);
d =  math.sqrt((xa - xd)**2 + (ya -yd)**2);
bd = math.sqrt((xb - xd)**2 + (yb -yd)**2);

p1 = a+bc+c;
p1 = p1/2;
S1 = math.sqrt(p1*(p1-a)*(p1-bc)*(p1-c));

p2 = a+bd+d;
p2 = p2/2;
S2 = math.sqrt(p2*(p2-a)*(p2-bd)*(p2-d));
S = S1+S2;
S=S//1;
print (S);
