def fiboSeries(input_num):
   if input_num <= 1:
       return input_num
   else:
       return(fiboSeries(input_num-1) + fiboSeries(input_num-2))

input_num = 10
print("Fibonacci Series")

for i in range(input_num):
  print(fiboSeries(i))
