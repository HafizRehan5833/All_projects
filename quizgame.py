a=input("\t\t\tHello!Please enter your roll number:-")
score=0


list1=['1','2','3','4','5','6','7','8','9','10']
list2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]

condition=a in list1
if  condition:
  print("\t\t\t Your test is start:)") 

  print("Question # 1:- \t ⊖ is an angle in the 4th quadrant. if ⊖ increases, then sin⊖")
  print("a:increases\t\t\t\tb: decreases\nc:increases and then decreases\t\td: decreases and then increases")
  a=input("enter your answer: ")
  if a.lower()=="a":
   # print("Your answer is correct.")
    score +=1

  print("Question # 2:- Sum of complex number with its conjugate is")

  print("a:real\t\tb:complex\nc:imaginary\t\td: N.O.T")
  b=input("enter your answer: ")

  if b.lower()=="a":
    #print("Your answer is correct.")
    score +=1

    
  print("Question # 3:- The length of the radius of the circle x ² + y ² =a ² is")
  print("a:o\t\tb:a \nc:2a\t\t d:3a")  

  c=input("enter your answer: ")

  if c.lower()=="b":
    #print("Your answer is correct.")
    score +=1

  print("Question # 4:-Every natural number is-----")

  print("a:a prime number\t\tb:an irrational number\nc:an integer\t\td:an even number")
  d=input("enter your answer: ")
  if d.lower()=="a":
    #print("Your answer is correct.")
    score +=1

  print("Question # 5:-0.25 is ....................")
  print("a:an irrational number\t\tb:a natural number\nc:a prime number\t\td: a rational number")  

  e=input("enter your answer: ")
  if e.lower()=="d":
    #print("Your answer is correct.")
    score +=1


  print("Question # 6:- sum as well as the product of any two conjugate complex number is ..............number")

  print("a:a complex number\t\tb:imaginary\nc:real\t\td:N.O.T")

  f=input("enter your answer: ")
  if f.lower()=="a":
    #print("Your answer is correct.")
    score +=1

  print("Question # 7:-Every whole number is")
  print("a:a real number\t\tb:an irrational number\nc:a prime number\t\td:a negative integer")

  g=input("enter your answer: ")
  if g.lower()=="a":
    #print("Your answer is correct.")
    score +=1

  print("Question # 8:-In R, the multiplicative identity is")
  print("a:0\t\tb:1\nc:-1\t\td:none")

  h=input("enter your answer: ")
  if g.lower()=="b":
    #print("Your answer is correct.")
    score +=1


  print("Question # 9:-if cos ⊖ = 2/3 and cos ⊖ / tan ⊖ > 0 , then ⊖ is in the")

  print("a:the 1st quadrant\t\tb:the 3rd quadrant\nc:the 4th quadrant\t\td:1st & 3rd quadrant")  

  i=input("enter your answer: ")
  if i.lower()=="c":
    #print("Your answer is correct.")
    score +=1

  print("Question # 10:-The constant distance of all points of the circle from its center is called the")
  print("a:radius of the circle\t\tb:secant of the circle\nc:chord of the circle\t\td:diameter of the circle")

  j=input("enter your answer: ")
  if j.lower()=="a":
    #print("Your answer is correct.")
    score +=1


  print("Question # 11:-What is the area of rectangular room with a length of 5-3i and width of 2i")

  print("a:6+10i\t\tb:5-i\nc:10-i\t\td:N.O.T")


  k=input("enter your answer: ")
  if k.lower()=="a":
    #print("Your answer is correct.")
    score +=1
  print("Question # 12:-Conic sections or simply conics are the curves obtained by cutting a right circular cone by...")

  print("a:a line\t\tb:two line\nc:a plane\t\td: two planes")


  l=input("enter your answer: ")
  if l.lower()=="c":
    #print("Your answer is correct.")
    score +=1

  print("Question # 13:-the equation of the circle with center (h , k) and radius r is")
  print("a:(x + h) ² + (y + k ) ² = r ²\t\tb:(x + h) ² + (y - k ) ² = r ²\nc:(x - h) ² + (y + k ) ² = r ²\t\td: (x - h) ² + (y - k ) ² = r ²")  


  m=input("enter your answer: ")
  if m.lower()=="d":
    #print("Your answer is correct.")
    score +=1


  print("Question # 14:- 1.4142135... is ......................")

  print("a:a natural number\t\tb:a:a irrational number\nc:a prime number \t\td: a rational number")


  n=input("enter your answer: ")
  if n.lower()=="d":
    
    #print("Your answer is correct.")
    score +=1

  print("Question # 15:- The set R-{0} of rea numbers is closed w. r. t?l")

  print("a:Addition\t\tb:Multiplication\nc:Division\t\t d:A .O. T")

  o=input("enter your answer: ")
  if o.lower()=="d":
    #print("Your answer is correct.")
    score +=1



    
  print("\t\t\tYour",score,"answer is correct.")
  print("\t\t\tYou got",(score/len(list2))*100,("%marks."))
else:
    print("\t\t\tYour roll number is invalid.Please enter your valid roll number.")
    quit()





















#print("What is your name?")
#print("a:Rehan\t\tb:Habib\nc:Aleem\t\td:Junaid")

#b=input("Enter your answer::")
#if b.lower()=="a":
 #   print("Your answer is correct.")
##    score +=1
#else:
#    print("Incorrect!")    



#print("What is yur schol name:-")
#print("a:sandal\t\tb:allied\nc:universal\t\td:none of these")
#c=input("Enter your answer::")
#if c.lower()=="d":
  #  print("Your answer is correct.")
 #   score +=1
#else:
 #   print("Incorrect!")    

#print("What are you doing?")
#print("a:study\t\tb:work\nc:coding\t\td:both a & c")
#d=input("Enter your answer::")
#if d.lower()=="d":
  #  print("Your answer is correct.")
 #   score +=1
#else:
   # print("Incorrect!")    


#print("What is best friend name:-")
#print("a:Aleem\t\tb:Abdul\nc:Habib\t\td:both a & c  ")
#e=input("Enter your answer::")
#if e.lower()=="d":
 #   print("Your answer is correct.")
#    score +=1
#else:
 #   print("Incorrect!")    


#
#print("\t\t\t\tYour",score,"answer is correct.")

#print("\t\t\t\tYou got ",((score/4)*100),"%marks.")


