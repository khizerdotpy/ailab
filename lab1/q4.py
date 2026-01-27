while True:
    print("\n1. Add two numbers ")
    print("2. Subtract two numbers")
    print("3. Exit")
    choice=int(input("Enter your choice: "))

    match choice:
      case 1:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        sum=a+b
        print(f"Result: {sum}")
      case 2:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))  
        diff=a-b
        print(f"Result: {diff}")
      case 3:
        print("Exit Confirmed.")
        break
      case _:
        print("Enter a valid choice.")


