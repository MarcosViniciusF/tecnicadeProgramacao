num1 = float(input("Digite a primeira nota: "))
while num1 != 0:
  if(num1 >= 0 and num1 <= 10):
      num2 = float(input("Digite a segunda nota: "))
      if(num2 >= 0 and num2 <= 10):
         media = (num1 + num2) / 2
         print("a media de {} e {} é de {}".format(num1, num2, media))
         break
  else:
     num1 = float(input("Digite a primeira nota: "))
