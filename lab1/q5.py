lnum=int(input("Enter how many marks you want to input: "))

def average(lnum):
  marksl= []
  sum=0
  for i in range(lnum):
    mk=int(input("Enter marks: "))
    marksl.append(mk)


  #for i in range(lnum):
    

  for i in range(lnum):
    sum=sum+marksl[i]
  
  avg=sum/lnum
  print(f"Marks: {marksl}")
  print(f"Average Marks: {avg}")



average(lnum)
