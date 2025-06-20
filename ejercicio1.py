match operador:
    case"+":
      print("resultado",num_1+num_2)
    case"-":
      print("resultado",num_1-num_2)
    case"*":
      print("resultado",num_1*num_2)
    case"/":
      if num_2 != 0:
       print("resultado",num_1/num_2)
      else:
       print("resultado no valido")
    case _:
       print("resultado no valido")