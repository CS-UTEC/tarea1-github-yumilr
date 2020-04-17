n=int(input('Ingrese número: '))
if n==0:
  print('El número no es admitido')
else:
  for i in range (2,n-1):
    if n/i:
      print('El número no es primo')
      break
    else:
      print('El número es primo')
      break
