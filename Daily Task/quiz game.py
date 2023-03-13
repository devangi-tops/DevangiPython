#Quiz game using dictionary

name=input("Enter your name:")

print('Hello',name)

score=0
Q1="Q1.What is last date of january in 2023?"
Q2="Q2.What is the capital of India?"

answer={Q1:'31',Q2:'delhi'}
print(type(answer))

for i in answer:
    print(i)
    ans=input("Enter your answer:")
    if ans==answer[i]:
        print("True")
        score=score+10
        print("your score is:",score)
    else:
     print("False")
     score=score-5
     print("Your score is:",score)
print("Your Total score is:",score)
