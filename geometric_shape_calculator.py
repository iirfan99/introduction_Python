def geometrity(sekil):
    #triangle
    if len(sekil) ==3:
        a =sekil[0]
        b =sekil[1]
        c =sekil[2]


        if (a+b) > c and (a +c) > b and (b +c) > a:
           if (a==b)  and (a==c) and (b==c):
                print("equilateral triangle")
           elif (a==b) and (a==c):
               print("isosceles triangle")


           else:
               print("isosceles triangle")


        else:
            print("entered values do not specify a triangle")


   #quadrilateral
    elif len(sekil)==4:
        a= sekil[0]
        b= sekil[1]
        c= sekil[2]
        d= sekil[3]
        if(a==b) and (a==c) and (a==d):
            print("square")

        elif (a==c) and (b==d):
             print("rectangle")
        else:
             print("normal tetragon")



    elif len(sekil) ==5:
        a =sekil[0]
        b =sekil[1]
        c =sekil[2]
        d = sekil[3]
        e = sekil[4]


        if (a+b) > c and (a +c) > b and (b +c) > a:
           if (a==b)  and (a==c)  and (a==d) and (a==e)and (b==c)and (b==d)and(b==e)and(c==d)and(c==e)and(d==b)and(d==c)and(d==e):
                print("regular pentagon")


    else:
        print("entered values do not belong to any shape ")





while(True):
    elemanNumber =int(input("Please enter yout eleman Number :"))

    if(elemanNumber ==3):
        a= int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometrity([a,b,c])


    elif(elemanNumber ==4):
       a = int(input("a:"))
       b = int(input("b:"))
       c = int(input("c:"))
       d = int(input("d:"))
       geometrity([a,b,c,d])

    elif (elemanNumber == 5):
       a = int(input("a:"))
       b = int(input("b:"))
       c = int(input("c:"))
       d = int(input("d:"))
       e = int(input("e:"))
       geometrity([a, b, c, d,e])


    else:
        print("Please try agin !!!")
