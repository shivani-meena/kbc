question_list=[
              "how many continents are there?",
              "what is the capital of india?",
              "NG me konsa course padhaya jata hai?",
              "which is national flower of India?",
              "who is the president of india?"]
options_list=[
            ["Four","Nine","Seven","Eight",],
            ["Chandigarh","Bhopal","Chennai","Delhi"],
            ["Software Engineering" ,"Counseling","Tourism","Agriculture"],
            ["Rose","Lotus","sunflower","merygold"],
            ["Ramnath Kovind","Droupadi murmu","Nirmala Sitharaman","indira gandhi",]]

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



