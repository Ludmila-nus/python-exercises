#--- usuario debe ingresar una contraseña (segura 1 vocal minuscula, 2 simbolos * y #)
contraseña = input('Ingrese una contraseña, asegurese de que contenga: \n 1 vocal minuscula\
     \n 2 simbolos especiales diferentes * y # \n:')

#--- comprobamos si tiene 8 caracteres, contiene una vocal en minuscula y dos simbolos * o # 
if len(contraseña) < 8:
      print('La contraseña debe tener al menos 8 caracteres')
else:
      minuscula = False
      for minus in contraseña:
         if minus.islower() == True:
            minuscula = True
         if not minuscula:
            print('usted debe ingresar una minuscula')
      caracter1 = False 
      for carac in contraseña:    
          if '*' in contraseña:
            caracter1 = True
          if not caracter1:
             print('Usted debe ingresar un "*"') 
             caracter2 = False
      for carac in contraseña:    
          if '#' in contraseña:
            caracter1 = True
          if not caracter1:
             print('Usted debe ingresar un "#"') 
             caracter2 = False