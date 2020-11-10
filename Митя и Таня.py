X = float(input("Введите возраст Тани  "));
Y = float (input("Введите возраст Мишы  "));
srvoz = (X+Y)/2;
print("Средний возраст Тани и Мишы равен  ",srvoz);
if X>srvoz:
    otlT = X - srvoz;
else:
    otlT = srvoz - X;
if Y>srvoz:
    otlM = Y - srvoz;
else:
    otlM = srvoz - Y;

#otlM = srvoz-Y;
print("Отличие возраста Тани от среднего возраста " ,otlT,"\n Отличие возраста Мишы от среднего возраста",otlM);
