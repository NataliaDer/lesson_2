#def fizz_buzz(n):   если используем инпут
   # if(n%3==0):
       # print("Fizz")
   # if(n%5==0):
       # print("Buzz")
   # if (n%3==0) and (n%5==0):
       # print("FizzBuzz")
#n=int(input())
#fizz_buzz(n)

#если задаем диапазон\не функция
#for x in range (1, 100):
    
#if(x %3==0):
        #print("Fizz")
      #if(x %5==0):
        #print("Buzz")
      #if (x %3==0) and (x %5==0):
        #print("FizzBuzz")
      #else:
        #print(x) 

def fuzz_buzz(n):
   for i in range(0,n):
      if i %3==0:
        print("Fizz")
      if i %5==0:
        print("Buzz")
      if i %3==0 and i %5==0:
        print("FizzBuzz")
      else:
        print(i) 
n=int(input())
fuzz_buzz(n)
    