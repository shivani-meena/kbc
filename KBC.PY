question_list=[
              "how many continents are there?",
              "what is the capital of india?",
              "NG me konsa course padhaya jata hai?",
              "which is national flower of India?",
              "who is the president of india?"]
options_list=[
            ["1.Four","2.Nine","3.Seven","4.Eight",],
            ["1.Chandigarh","2.Bhopal","3.Chennai","4.Delhi"],
            ["1.Software Engineering" ,"2.Counseling","3.Tourism","4.Agriculture"],
            ["1.Rose","2.Lotus","3.sunflower","4.merygold"],
            ["1.Ramnath Kovind","2.Droupadi murmu","3.Nirmala Sitharaman","4.indira gandhi",]]

solution_list=[3,4,1,2,2]

lifeline=[["(1)Four","(3)Seven"],
         ["(2)Bhopal","(4)Delhi"],
         ["(1)Software Engineeering","(3)Tourism"],
         ["(2)Lotus","(3)Sunflower"],
         ["(2)Droupadi murmu","(4)indira gandhi"]]

print("Welcome to KBC")
print("your game starts now") 


i=0
money=0
c=1
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        k=options_list[i][j]
        print(k)
        j=j+1
    if c<3:
        user_input=input("do you using lifeline")
        if user_input=="yes":
            c=c+1
            print("5050",lifeline[i])
    else:
        print("you cant use lifeline,because you already use two ltfeline")
    b=int(input("choose correct answer : "))
    if b==solution_list[i]:
            money=money+10000
            print("your answer is correct")
            print("you win Rs./-",money)
    else:
        print("your answer is wrong")

    i=i+1



