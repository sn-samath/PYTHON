try:
    a=int(input())
    b=int(input())
    c=input()
    print(d)



except ValueError as z:
    print("ValueError",z)


except TypeError as w:
    print("TypeError",w)


except Exception:
    print ("something worng")


finally:
    print("done")
