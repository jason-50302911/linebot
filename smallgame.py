import random 
import copy

def userinput(message, answer):
    rightinput = False
    
    if message.isdigit() == True:
        if len(message) == len(answer):
            rightinput = True

    return rightinput

def decsidethedigits(message):
    rightinput = False
    
    if message.isdigit() is True:
        if int(message) <= 5:
            rightinput = True

    return rightinput

def generatoranswer(message):
    message = int(message)
    computeranswer = []

    for digit in range (1, message + 1):
        if digit == 1:
            number = random.randint(1, 9)
            computeranswer.append(number)
        else:
            number = random.randint(0, 9)
            computeranswer.append(number)
    
    return computeranswer

def playgame(message, answer):
    length = len(answer)
    tempuser = copy.deepcopy(message)
    tempanswer = copy.deepcopy(answer)
    tempuser = list(tempuser)
    count = 0
    answerB = 0
    answerA = 0
    for checking in tempuser:
        if tempanswer[count] is int(checking):
            answerA += 1
            tempuser[count] = -1
            tempanswer[count] = -1
        count += 1
    for matched in tempuser:   
        for countnumber in tempanswer:
            if int(matched) is countnumber and int(matched) != -1:
                answerB += 1
                tempanswer[tempanswer.index(countnumber)] = -1
                tempuser[tempuser.index(matched)] = -1

    if answerA == length:
        return None
    else:
        lista = [answerA, answerB]
        return lista
        
        
def telling_rule():
    rule = 'you'
    return rule
        
# def telling_rule():
#     rule = "此遊戲是猜電腦出的一個數字，範圍為一到五位數，利用幾A幾B去告訴你的答案的對錯\n\
#         A是告訴你有幾個數字在對的位置上且數字是正確的\n\
#         B是告訴你有幾個數字是對的但數字位置是不對的\n\
#         請開始輸入你想要猜得位數"
    
#     return rule


# message = input("number:")
# right = False 
# aright = False

# while right is False:
#     if decsidethedigits(message) is True:
#         computeranswer = generatoranswer(message)
#         print(computeranswer)
#         right = True
#     else:
#         message = input ("number:")
          
# useranswer = input("youranswer")
# while aright is False:
#     if userinput(useranswer, computeranswer) is True:
#         lastanswer = playgame(useranswer, computeranswer)
#         if lastanswer is None:
#             print("Great")
#             aright = True
#         else:
#             print("{}A{}B".format(lastanswer[0], lastanswer[1]))
#             useranswer = input("youranswer")
#     else:
#         useranswer = input("youranswer")
        
        
        
        
        
        
# for i in range(1, 10):
#     message = input("number")
#     answer = [1, 2, 3]
#     lastanswer = playgame(message, answer)
#     if lastanswer is None:
#         print("Great")
#         aright = True
#     else:
#         print("{}A{}B".format(lastanswer[0], lastanswer[1]))
