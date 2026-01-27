unum=int(input("Enter how many students: "))

def record(unum):
  udict = {}

  for i in range(unum):
    key=input("Enter student name: ")
    value=int(input("Enter student marks: "))

    udict[key]=value


  print("Student Records: ")

  for key, value in udict.items():
    print(f"{key} : {value}")
    


record(unum)
