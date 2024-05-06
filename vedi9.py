questions = [["which language was used to create fb?","python","none","french","javascript","d"],
             ["india prime minister name?","modi","rahul","nehru","none","a"],
             ["surat kesa city he","smart","clean","green","all of these","b"],
             ["apdi company kevi che?","good","v.good","bad","none","c"]]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0

for i in range(0,len(questions)):
  question = questions[i]
  print(f"Questions for Rs.{levels[i]} is {questions [i][0]}")
  print(f"a.{questions [i][1]}  b.{questions [i][2]}")
  print(f"c.{questions [i][3]}  d.{questions [i][4]}")

  reply = str(input("enter your answer"))
  if(reply == questions [i][5]):
    print(f"correct answer, you have win Rs.{levels [i]}")
  else:
    print("wrong answer!")
    break;
    



          

 




