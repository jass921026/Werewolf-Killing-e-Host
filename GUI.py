from tkinter import *
from math import *
from time import *
from functools import partial
myFont=('新細明體')
global player_count
def init(players=12):
    global player_count
    player_count=players
    return Background()
class Background(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Werewolf Killing e-Host")
        self.geometry("800x600")
        self.configure(background="white")
        self.frame=Frame(self)
        self.frame.pack()
        self.Title=Label(self.frame,text="狼人殺電腦主持人",font=(myFont,30),width="20",height="1")
        self.SubTitle=Label(self.frame,text="by 12715張均豪、12717陳品羲",font=(myFont,20),width="30",height="1")
        self.Title.pack()
        self.SubTitle.pack()
class SingleSelection:
    def __init__(self,stage,text,result,can_quit=0):
        self.stage=stage
        self.frame=Frame(self.stage,bg="pink",width=800,height=500)
        self.Text=Label(self.frame,text=text,font=(myFont,20),width="25",height="1")
        self.Text.place(x=220,y=50)
        self.Buttons = list()
        self.res=result
        self.res[0]=0
        self.go=0
        self.cqt=can_quit
        for i in range(player_count):
            self.Buttons.append(Button(self.frame,text=(str)(i+1),font=(myFont,30),bg="lightgrey",command=partial(self.select,i+1)))
            self.Buttons[i].place(x=380+300*cos(pi/(player_count-1)*i),y=100+300*sin(pi/(player_count-1)*i))
        self.Confirm=Button(self.frame,text="確認",font=(myFont,30),command=partial(self.conf))
        self.Confirm.place(x=330,y=150)
        self.run()
    def run(self):
        self.frame.place(x=0,y=100)
        while(self.go==0):
            self.stage.update()
    def select(self,i):
        if(self.res[0]!=0):
            self.Buttons[self.res[0]-1]['bg']="lightgrey"
        self.Buttons[i-1]['bg']="grey"
        self.res[0]=i
    def conf(self):
        if(self.res[0]!=0 or self.cqt==1):
            self.frame.place_forget()
            self.go=1
        
class MultiSelection:
    def __init__(self,stage,text,res,cnt):
        self.stage=stage
        self.frame=Frame(self.stage,bg="lightblue",width=800,height=500)
        self.Text=Label(self.frame,text=text,font=(myFont,20),width="25",height="1")
        self.Text.place(x=220,y=50)
        self.Buttons = list()
        self.res=res
        self.cnt=cnt
        self.go=0
        for i in range(player_count):
            self.Buttons.append(Button(self.frame,text=(str)(i+1),font=(myFont,30),bg="lightgrey",command=partial(self.select,i+1)))
            self.Buttons[i].place(x=380+300*cos(pi/(player_count-1)*i),y=100+300*sin(pi/(player_count-1)*i))
        self.Confirm=Button(self.frame,text="確認",font=(myFont,30),command=partial(self.conf))
        self.Confirm.place(x=330,y=150)
        self.run()
    def run(self):
        self.frame.place(x=0,y=100)
        while(self.go==0):
            self.stage.update()
    def select(self,i):
        if(self.res[i-1]):
            self.Buttons[i-1]['bg']="lightgrey"
            self.res[i-1]=0
        else:
            self.Buttons[i-1]['bg']="grey"
            self.res[i-1]=1
    def conf(self):
        current_cnt=0
        for i in range(player_count):
            if(self.res[i]):
                current_cnt+=1
        if(self.cnt==current_cnt):
            self.frame.place_forget()
            self.go=1

class YNSelection:
    def __init__(self,stage,text,res):
        self.stage=stage
        self.frame=Frame(self.stage,bg="yellow",width=800,height=500)
        self.Text=Label(self.frame,text=text,font=(myFont,20),width="30",height="1")
        self.Text.place(x=200,y=50)
        self.res=res
        self.res[0]=-1
        self.go=0
        self.YB=Button(self.frame,text="是",font=(myFont,30),bg="lightgrey",command=partial(self.select,1))
        self.NB=Button(self.frame,text="否",font=(myFont,30),bg="lightgrey",command=partial(self.select,0))
        self.YB.place(x=200,y=200)
        self.NB.place(x=500,y=200)
        self.Confirm=Button(self.frame,text="確認",font=(myFont,30),command=partial(self.conf))
        self.Confirm.place(x=330,y=350)
        self.run()
    def run(self):
        self.frame.place(x=0,y=100)
        while(self.go==0):
            self.stage.update()
    def select(self,i):
        if(i==1):
            self.YB["bg"]="grey"
            self.NB["bg"]="lightgrey"
            self.res[0]=1
        else:
            self.NB["bg"]="grey"
            self.YB["bg"]="lightgrey"
            self.res[0]=0
    def conf(self):
        if(self.res[0]!=-1):
            self.frame.place_forget()
            self.go=1
class Text:
    def __init__(self,stage,text,sec=5):
        self.stage=stage
        self.frame=Frame(self.stage,bg="lightgrey",width=800,height=500)
        self.Text=Label(self.frame,text=text,font=(myFont,30),width="25",height="1")
        self.Text.place(x=150,y=50)
        self.run()
        sleep(sec)
        self.conf()
    def run(self):
        self.frame.place(x=0,y=100)
        self.stage.update()
    def conf(self):
        self.frame.place_forget()
        self.stage.update()
class ConfText:
    def __init__(self,stage,text):
        self.stage=stage
        self.frame=Frame(self.stage,bg="lightgrey",width=800,height=500)
        self.Text=Label(self.frame,text=text,font=(myFont,30),width="25",height="1")
        self.Text.place(x=150,y=50)
        self.Confirm=Button(self.frame,text="確認",font=(myFont,30),command=partial(self.conf))
        self.go=0
        self.Confirm.place(x=330,y=350)
        self.run()
    def run(self):
        self.frame.place(x=0,y=100)
        while(self.go==0):
            self.stage.update()
    def conf(self):
        self.frame.place_forget()
        self.go=1


class Talk:
    def __init__(self,stage,num,res):
        self.stage=stage
        self.frame=Frame(self.stage,bg="green",width=800,height=500)
        self.Text=Label(self.frame,text=str(num)+'號玩家請發言',font=(myFont,20),width="25",height="1")
        self.Text.place(x=220,y=50)
        self.res=res
        self.res[0]=-1
        self.go=0
        self.YB=Button(self.frame,text="過",font=(myFont,30),bg="lightgrey",command=partial(self.select,1))
        self.NB=Button(self.frame,text="自爆",font=(myFont,30),bg="lightgrey",command=partial(self.select,0))
        self.YB.place(x=200,y=200)
        self.NB.place(x=500,y=200)
        self.Confirm=Button(self.frame,text="確認",font=(myFont,30),command=partial(self.conf))
        self.Confirm.place(x=330,y=350)
        self.run()
    def run(self):
        self.frame.place(x=0,y=100)
        while(self.go==0):
            self.stage.update()
    def select(self,i):
        if(i==1):
            self.YB["bg"]="grey"
            self.NB["bg"]="lightgrey"
            self.res[0]=1
        else:
            self.NB["bg"]="grey"
            self.YB["bg"]="lightgrey"
            self.res[0]=0
    def conf(self):
        if(self.res[0]!=-1):
            self.frame.place_forget()
            self.go=1
    

class TextInput:
    def __init__(self,stage,text,res):
        self.stage=stage
        self.frame=Frame(self.stage,bg="red",width=800,height=500)
        self.Text=Label(self.frame,text=text,font=(myFont,20),width="40",height="1")
        self.Text.place(x=150,y=50)
        self.res=res
        self.res[0]=0
        self.var=StringVar()
        self.go=0
        self.InputBar=Entry(self.frame,font=(myFont,28),textvariable=self.var)
        self.InputBar.place(x=220,y=200)
        self.Confirm=Button(self.frame,text="確認",font=(myFont,30),command=partial(self.conf))
        self.Confirm.place(x=330,y=350)
        self.run()
    def run(self):
        self.frame.place(x=0,y=100)
        while(self.go==0):
            self.stage.update()
    def conf(self):
        self.res[0]=self.var.get()
        self.frame.place_forget()
        self.go=1

if(__name__=='__main__'):
    bg=init(12)
    myid=[0]
    TextInput(bg,text="12號啟動腳色技能，請問你要帶走的玩家是?",res=myid)
    t=Talk(bg,5,myid)
    myEnter=SingleSelection(bg,"test",myid)
    print(myid[0])
    wolf_arr=list()
    for i in range(player_count):
        wolf_arr.append(0)
    myMultiEnter=MultiSelection(bg,text="請輸入狼人的編號(應選四位)",res=wolf_arr,cnt=4)
    for i in range(player_count):
        if(wolf_arr[i]):
            print(i+1,end=' ')
    print()
    myYN=[0]
    myYNEnter=YNSelection(bg,text="TA被殺了，你要救嗎?",res=myYN)
    print(myYN[0])
