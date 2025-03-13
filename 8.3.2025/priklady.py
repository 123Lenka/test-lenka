numbers = [23, 4, -8, 16, 15, -42]

result = 0

for number in numbers:
  result = result + number

  
print(result)

  
les = [23, 4, -8, 16, 15, -42]

kosik = 0

for houba in les:
  kosik += houba

  
print(kosik)

coffee_list = [
    ["Espresso", 63],
    ["Americano", 95],
    ["Latte", 75],
    ["Cold Brew", 200],
    ["Cappuccino", 80]
]

for coffee in coffee_list:
    if coffee [1] < 90:
        print(coffee[0])


numbers = [23, 4, -8, 16, 15, -42]

numbers.append(31)

sude_kosik = []

for number in numbers:
   if number %2 ==0:
     
      sude_kosik.append(number)

print(sude_kosik)
print(len(sude_kosik))
print(sum(sude_kosik))
