from tkinter import *
from PIL import *
import random
import os

class Game(object):
    def __init__(self,root):
        self.root=root
        self.canvas=Canvas(self.root,width=150,height=200)
        self.canvas.grid(row=0,column=0)

        self.highb=Button(root,text='HIGHER',command=self.onclickhighb)
        self.lowb=Button(root,text='LOWER',command=self.onclicklowb)
        self.highb.grid(row=1,column=0)
        self.lowb.grid(row=1,column=1)

        self.life=5
        self.score=0
        self.life_and_score=Label(root,text='Life: '+str(self.life)+' Score: '+str(self.score))
        self.life_and_score.grid(row=2,column=0)

        self.msglabel=Label(root,text='')
        self.msglabel.grid(row=3,column=0)

        self.value=''

        self.cards_in_deck={'sa':1,'s2':2,'s3':3,'s4':4,'s5':5,'s6':6,'s7':7,'s8':8,'s9':9,'s10':10,'sj':11,'sq':12,'sk':13,
        'ha':1,'h2':2,'h3':3,'h4':4,'h5':5,'h6':6,'h7':7,'h8':8,'h9':9,'h10':10,'hj':11,'hq':12,'hk':13,
        'ca':1,'c2':2,'c3':3,'c4':4,'c5':5,'c6':6,'c7':7,'c8':8,'c9':9,'c10':10,'cj':11,'cq':12,'ck':13 ,
        'da':1,'d2':2,'d3':3,'d4':4,'d5':5,'d6':6,'d7':7,'d8':8,'d9':9,'d10':10,'dj':11,'dq':12,'dk':13}
        self.cards_in_stack={}
        self.curr_card=random.choice(list(self.cards_in_deck.keys()))
        self.cards_in_stack.update({self.curr_card:self.cards_in_deck[self.curr_card]})
        self.cards_in_deck.pop(self.curr_card)
        self.rand_card=random.choice(list(self.cards_in_deck.keys()))
        self.img=PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+'\\Cards\\'+self.curr_card+".png")
        self.imgoncanvas=self.canvas.create_image(20,20,anchor=NW,image=self.img)

    def updatemsglabel(self,msg):
        self.msglabel['text']=msg

    def updatecard(self,card):
        global url
        url=PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+'\\Cards\\'+card+".png")
        self.canvas.itemconfig(self.imgoncanvas,image=url)

    def updatescoreandlife(self,score):
        self.life_and_score['text']='Life: '+str(self.life)+' Score: '+str(score)

    def onclickhighb(self):
        if self.ishigher():
            self.correct()
        else:
            self.wrong()

    def onclicklowb(self):
        if not self.ishigher():
            self.correct()
        else:
            self.wrong()

    def correct(self):
        self.updatemsglabel('You are correct!')
        self.score+=1
        if len(self.cards_in_deck)==0:
            self.end()
        self.initialize()
        self.updatecard(self.curr_card)
        self.updatescoreandlife(self.score)

    def wrong(self):
        self.updatemsglabel('You are wrong!')
        self.life-=1
        # self.score-=1
        if self.life==0:
            self.end()
        self.initialize()
        self.updatecard(self.curr_card)
        self.updatescoreandlife(self.score)

    def initialize(self):
        self.curr_card=self.rand_card
        self.cards_in_stack.update({self.curr_card:self.cards_in_deck[self.curr_card]})
        self.cards_in_deck.pop(self.curr_card)
        self.rand_card=random.choice(list(self.cards_in_deck.keys()))

    def ishigher(self):
        if self.cards_in_stack[self.curr_card]<=self.cards_in_deck[self.rand_card]:
            return True
        else:
            return False

    def end(self):
        self.highb['state']=DISABLED
        self.lowb['state']=DISABLED
        if self.life==0:
            self.updatemsglabel('Better luck next time! Your score was '+str(self.getscore()))# Display lose msg to frontend
        else:
            self.updatemsglabel('Congratulations, you won!')# Display win msg to frontend

    def getlife(self):
        return self.life

    def getscore(self):
        return len(self.cards_in_stack)

root=Tk()
obj=Game(root)
root.mainloop()  
