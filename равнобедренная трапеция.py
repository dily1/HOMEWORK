import math;
Osn_verh = int(input("Введите верхнее основание" ));
Osn_niz = int(input('Введите нижнее основание '));
Ygol = int(input('Введите угол при большем основании'));

Ygol = math.radians(Ygol);
tang= math.tan(Ygol);
a =Osn_niz**2;
b =Osn_verh**2;
c = a-b;
e = 1/2*c
d = tang*e;
d = d//1
print ("Площадь трапеции =" ,d);
