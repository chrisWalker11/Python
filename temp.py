cTemp = 0.0
fTemp = 0.0
temp = float(input("Enter temp: "))
option =(int(input("Enter 1 to convert from F to C or 2 to convert from C to F: "))
 if option == 1
    cTemp = (temp - 32) * (5.0 / 9.0)
    printf("the temp in C is {cTemp}" )
 elif option == 2
    fTemp = (temp * 9.0 / 5.0) + 32
    printf("The temp in F is {fTemp}")

 else
         Printf("incorret option of {option}")

