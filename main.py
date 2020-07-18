from time import*
from random import*
from tkinter import*
from audio import*
from GUI import*


#playernumbers

players=12
wolves=4
todaydie=[0]*12
minnum=0
maxnum=0
peace=0

#identities

wolfkill=0

win=0
witchnum=0
hunternum=0
idiotnum=0
seernum=0

dovote=1
policenum=0
police=0

wid=[["狼人","狼王","白狼王","惡靈騎士","狼美人"],[4,0,0,0,0]]
gid=[['魔術師','守衛','攝夢人','女巫','預言家','獵人','騎士','白痴','平民'],[0,0,0,1,1,1,0,1,4]]

#for GUI
wolves=[0]*12
YNres=[0]
poison=[0]
witchn=[0]
seern=[0]
huntern=[0]
idiotn=[0]
guni=[0]
voten=[0]
exp=[0]
expn=[0]
'''
def settings():
    global players
    print('請輸入遊戲人數')
    players=int(input())
    for i in range(5):
        print('請輸入%s數量' % (wid[0][i]))
        wid[1][i]=int(input())
    for i in range(9):
        print('請輸入%s數量' % (gid[0][i]))
        gid[1][i]=int(input())
'''
def wincheck():
    global win
    v=0
    w=0
    g=0
    for i in range(players):
        if player_data[1][i]!=0:
            continue
        if player_data[2][i]==0:
            v+=1
        elif player_data[2][i]>0 and player_data[2][i]%2==0:
            g+=1
        elif player_data[2][i]==1:
            w+=1
    if v==0 or g==0:
        play('gameover',blocking=True)
        play('wolfwin',blocking=True)
        ConfText(bg,"遊戲結束，狼人勝利!")
        win=1
    elif w==0:
        play('gameover',blocking=True)
        play('goodwin',blocking=True)
        ConfText(bg,"遊戲結束，好人勝利!")
        win=1
    else:
        return
'''
def guard(n):
    global guardnum, guard
    if n==1:
        print('請輸入守衛號碼')
        guardnum=int(input())
    print('今晚要守護誰?')
    p=int(input())
    r=guard
'''
def print_data(data):
    for i in range(4):
        for j in range(12):
            print(data[i][j],end=' ')
        print()
     
def werewolf(n):
    global wolfkill
    play('wolfopen')
    wfopen=Text(bg,'狼人現身請睜眼')
    if n==1:
        wolf=MultiSelection(bg,'請輸入狼人號碼',wolves,wid[1][0])
        for i in range(12):
            r=wolves[i]
            player_data[2][i]=r
        play('wolfcheck')
        wolcheck=Text(bg,'請確認彼此身分')
        
    sleep(1)
    kill=[0]
    play('wolfkill')
    killing=SingleSelection(bg,'狼人請殺人',kill)
    wolfkill=kill[0]
    todaydie[wolfkill-1]=1
    play('wolfclose',blocking=True)

def witch(n):
    global wolfkill, witchnum
    if gid[1][3]!=0:
        p=0
        ynpos=1
        play('witchopen')
        wiopen=Text(bg,'女巫請睜眼')
        if n==1:
            witchn=[0]
            witc=SingleSelection(bg,'請輸入女巫號碼',witchn)
            witchnum=witchn[0]
            player_data[2][witchnum-1]=2
        if player_data[1][witchnum-1]==0 and player_data[3][witchnum-1]%2==0:
            play('heal')
            heal=YNSelection(bg,"今天晚上 "+str(wolfkill)+" 被殺了，你要救他嗎？",YNres)
            if YNres[0]==1:
                todaydie[wolfkill-1]=0
                player_data[3][witchnum-1]+=1
                wolfkill=0
                ynpos=0
                    
        else:
            play('heal')
            sleep(5)
        if player_data[1][witchnum-1]==0 and player_data[3][witchnum-1]!=3 and ynpos==1:
            if player_data[3][witchnum-1]==0 or player_data[3][witchnum-1]%2==1:
                play('poison')
                dopos=YNSelection(bg,"你要使用毒藥嗎？",YNres)
                if YNres[0]==1:
                    poison=[0]
                    posions=SingleSelection(bg,"你要毒誰呢？",poison)
                    p=poison[0]
                    todaydie[p-1]=1
                    player_data[3][witchnum-1]+=2
            else:
                play('poison')
                sleep(5)
        else:
            play('poison')
            sleep(5)
        play('witchclose',blocking=True)
def seer(n):
    global seernum, wolfkill
    play('seeropen')
    sopen=Text(bg,'預言家請睜眼')
    if n==1:
        see=SingleSelection(bg,"請輸入預言家號碼",seern)
        seernum=seern[0]
        player_data[2][seernum-1]=4
    play('seercheck')
    if player_data[1][seernum-1]!=0:
        sleep(5)
    else:
        checkn=[0]
        checking=SingleSelection(bg,"選擇今晚要查驗的對象",checkn)
        check=checkn[0]
        if player_data[2][check-1]%2==1:
            t=Text(bg,"他是壞人")
        else:
            t=Text(bg,"他是好人")
    sleep(1)
    play('seerclose',blocking=True)
def hunter(n):
    global hunternum
    if n==1:
        sleep(1)
        play('hunteropen')
        hopen=Text(bg,'獵人請睜眼')
        hunters=SingleSelection(bg,"請輸入獵人號碼",huntern)
        hunternum=huntern[0]
        player_data[2][hunternum-1]=6
        sleep(1)
        play('hunterclose',blocking=True)

def huntershot():
    global hunternum
    play(str(hunternum),blocking=True)
    play('huntershot')
    TextInput(bg,"啟動角色技能，請問你要帶走的玩家是？",guni)
    gun=int(guni[0])
    if gun==0:
        return
    else:
        todaydie[gun-1]=1
        play(str(gun),blocking=True)
        play('eliminate')
        Text(bg,str(gun)+" 號玩家被槍殺")
        wincheck()
def idiot(n):
    global idiotnum
    if gid[1][7]!=0:
        if n==1:
            sleep(1)
            play('idiotopen')
            iopen=Text(bg,'白痴請睜眼')
            idiots=SingleSelection(bg,"請輸入白痴號碼",idiotn)
            idiotnum=idiotn[0]
            player_data[2][idiotnum-1]=8
            sleep(1)
            play('idiotclose',blocking=True)
'''
def police_elec():
    print('開始競選警長')
    print('候選人請舉手')
    s=0
    while True:
        e=int(input())
        if e==0:
            break
        else:
            elec.append(e)
            s+=1
    start=randint(0,s-1)
    for i in range(0,s):
        num=i+start
        if num>=s:
            num%=s
        print(str(elec[num])+'號玩家請發言')
        play(str(elec[num]))
        if int(input())==1:
            continue
'''      
    
    


def bright(n):
    global wolfkill, poison, hunternum, players, peace,minnum,maxnum
    play('bright')
    Text(bg,'天亮請睜眼')
    play('lastnight')
    Text(bg,'昨天晚上',sec=2)
    dnum=0
    for i in range(players):
        if todaydie[i]!=0:
            if dnum==0:
                minnum=i+1
            play(str(i+1))
            Text(bg,str(i+1)+' 號 ',sec=2)
            maxnum=i+1
            dnum+=1
        else:
            continue
    if dnum==0:
        peace=1
        play('peacenight')
        Text(bg,"是平安夜")
    else:
        peace=0
        play('killed')
        Text(bg,"被殺死")
    if wolfkill==hunternum:
        huntershot()
    for i in range(players):
        if todaydie[i]!=0:
            player_data[1][i]=1
            if n==1:
                play(str(i+1))
                play('lastword')
                ConfText(bg,str(i+1)+'號請發表遺言')
        todaydie[i]=0
    return
def speaking(n):
    global wolfkill, poison, dovote, players,minnum,maxnum
    dovote=1
    if peace:
        i=randint(1,players)
        while player_data[1][i-1]==1:
            i=randint(1,players)
    else:
        if n%2==1: 
            i=maxnum+1
        else:
            i=minnum-1
    if n%2==1:
        for j in range(i,i+players):
            if j>players:
                num=j%players
            else:
                num=j
            if player_data[1][num-1]==1:
                continue
            else:
                play(str(num),blocking=True)
                play('speak')
                talking=Talk(bg,num,exp)
                if exp[0]==1:
                    continue
                else:
                    explode=SingleSelection(bg,'自爆，請輸入號碼',expn)
                    e=expn[0]
                    player_data[1][e-1]=1
                    dovote=0
                    exp[0]=0
                    return
    else:
        for j in range(i+players,i,-1):
            if j>players:
                num=j%players
            else:
                num=j
            if player_data[1][num-1]==1:
                continue
            else:
                play(str(num),blocking=True)
                play('speak')
                talking=Talk(bg,num,exp)
                if exp[0]==1:
                    continue
                else:
                    explode=SingleSelection(bg,'自爆，請輸入號碼',expn)
                    e=expn[0]
                    player_data[1][e-1]=1
                    dovote=0
                    exp[0]=0
                    return

def vote():
    global hunternum, idiotnum, win, dovote,voten
    if dovote==1:
        play('voting')
        votin=TextInput(bg,"輸入被處決的玩家的號碼",voten)
        vote=int(voten[0])
        if vote==0:
            Text(bg,"本輪無玩家被處決")
            return
        else:
            play(str(vote),blocking=True)
            play('eliminate')
            Text(bg,"本輪處決 "+str(vote)+" 號玩家")
            player_data[1][vote-1]=1
            wincheck()
            if win!=0:
                return
            if vote==hunternum:
                huntershot()
                if win!=0:
                    return
            elif vote==idiotnum:
                play(str(vote),blocking=True)
                play('isidiot')
                Text(bg,str(vote)+" 號玩家是白痴，請翻牌")
                player_data[1][idiotnum-1]=2
            play('lastword')
            ConfText(bg,'請發表遺言')
            return
    



bg=init(players)

player_data=[[0]*players for i in range(4)]
for j in range(players):
    player_data[0][j]=j+1

#night


nn=1
while True:
    wolfkill=0
    poison=0
    play('dark')
    DarkText=Text(bg,text="天黑請閉眼")
    werewolf(nn)
    if nn>1:
        wincheck()
        if win!=0:
            break
    sleep(1)
    witch(nn)
    if nn>1:
        wincheck()
        if win!=0:
            break
    sleep(1)
    seer(nn)
    hunter(nn)
    idiot(nn)
    sleep(1)
    bright(nn)
    speaking(nn)
    vote()
    if win!=0:
        break
    nn+=1
