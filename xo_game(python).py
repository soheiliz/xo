from tkinter import *
from random import *

def start():
    root1.destroy()

def lets_go(h):
    if h!=None:
        h.destroy()
    global root1
    global turn
    global table
    global dude
    root1 = Tk()
    root1.title("soheil's xo game")
    root1.geometry("600x600")
    turn = 1
    table = []
    dude = 0
    for i in range(3):
        exx = []
        for j in range(3):
            exx.append(0)
        table.append(exx)

    my_menu = Frame(root1,bg="light blue",width=600,height=600)
    my_menu.pack(side=TOP)

    play_pvp = Button(my_menu,text="play againts your friend",bd=3,padx=5,pady=5,font=("Arial",14),command=pvp,height=1,width=20)
    play_pvp.place(x=190,y=260)

    exit_butt = Button(my_menu,text="exit the game",bd=3,padx=5,pady=5,font=("Arial",14),command=exit,width=20,height=1)
    exit_butt.place(x=190,y=330)

    play_pvi = Button(my_menu,text="play againts an ai",bd=3,padx=5,pady=5,font=("Arial",14),command=againts_ai,width=20,height=1)
    play_pvi.place(x=190,y=190)

    root1.mainloop()

def pvp():
    start()
    global turn
    global root
    global xo_board
    root = Tk()
    root.title("its XO bitches!!")
    root.geometry("600x640")
    xo_board = Canvas(root,width=595,height=590,bg="#EAF998")
    xo_board.pack(side=TOP)
    again(root)
    for i in range(0,600,200):
        xo_board.create_line(i,0,i,600,width=3)
        xo_board.create_line(0,i,600,i,width=3)

    xo_board.bind('<Button-1>',its_time)
    root.mainloop()

def its_time(event):
    global turn
    global table
    x=event.x
    y=event.y
    x = int(x/200)
    y = int(y/200)
    if turn%2==0:
        extra = "X"
    else:
        extra = "O"
    a = x
    b = y
    x = x*200 + 2
    y = y*200 + 2
    if extra=="O":
        yo = Label(xo_board,text=f"{extra}",bg = "white",font=("Arial",110),padx=40,pady=14)
    elif extra=="X":
        yo = Label(xo_board,text=f"{extra}",bg = "white",font=("Arial",110),padx=48,pady=14)
    yo.place(x=x,y=y)
    adding(a,b,extra)
    turn +=1
    yoyo1 , yoyo2 = check(table)
    if yoyo1 != None:
        win_time(yoyo1 , yoyo2)

def adding(b,a,c):
    global turn
    global table
    if c=="O":
        c=5
    else:
        c=20
    table[a][b]=c
    print(table)
            
def check(table):
    if table[0][0]+table[0][1]+table[0][2]==15:
        return("O player 1","c1")
    if table[1][0]+table[1][1]+table[1][2]==15:
        return("O player 1","c2")
    if table[2][0]+table[2][1]+table[2][2]==15:
        return("O player 1","c3")
    if table[0][0]+table[0][1]+table[0][2]==60:
        return("X player 2","c1")
    if table[1][0]+table[1][1]+table[1][2]==60:
        return("X player 2","c2")
    if table[2][0]+table[2][1]+table[2][2]==60:
        return("X player 2","c3")
    if table[0][0]+table[1][1]+table[2][2]==15:
        return("O player 1","z1")
    if table[0][2]+table[1][1]+table[2][0]==15:
        return("O player 1","z2")
    if table[0][0]+table[1][1]+table[2][2]==60:
        return("X player 2","z1")
    if table[0][2]+table[1][1]+table[2][0]==60:
        return("X player 2","z2")
    if table[0][0]+table[1][0]+table[2][0]==15:
        return("O player 1","r1")
    if table[0][1]+table[1][1]+table[2][1]==15:
        return("O player 1","r2")        
    if table[0][2]+table[1][2]+table[2][2]==15:
        return("O player 1","r3")
    if table[0][0]+table[1][0]+table[2][0]==60:
        return("X player 2","r1")
    if table[0][1]+table[1][1]+table[2][1]==60:
        return("X player 2","r2")
    if table[0][2]+table[1][2]+table[2][2]==60:
        return("X player 2","r3")
    check_draw()
    return (None,None)

def where():
    if table[0][0]+table[0][1]+table[0][2]==40:
        if table[0][0]==0:
            return(0,0)
        elif table[0][1]==0:
            return(0,1)
        elif table[0][2]==0:
            return(0,2)
    if table[1][0]+table[1][1]+table[1][2]==40:
        if table[1][0]==0:
            return(1,0)
        elif table[1][1]==0:
            return(1,1)
        elif table[1][2]==0:
            return(1,2)
    if table[2][0]+table[2][1]+table[2][2]==40:
        if table[2][0]==0:
            return(2,0)
        elif table[2][1]==0:
            return(2,1)
        elif table[2][2]==0:
            return(2,2)
    if table[0][0]+table[1][1]+table[2][2]==40:
        if table[0][0]==0:
            return(0,0)
        elif table[2][2]==0:
            return(2,2)
    if table[0][2]+table[1][1]+table[2][0]==40:
        if table[0][2]==0:
            return(0,2)
        elif table[2][0]==0:
            return(2,0)
    if table[0][0]+table[1][0]+table[2][0]==40:
        if table[0][0]==0:
            return(0,0)
        elif table[1][0]==0:
            return(1,0)
        elif table[2][0]==0:
            return(2,0)
    if table[0][1]+table[1][1]+table[2][1]==40:
        if table[0][1]==0:
            return(0,1)
        elif table[1][1]==0:
            return(1,1)
        elif table[2][1]==0:
            return(2,1)
    if table[0][2]+table[1][2]+table[2][2]==40:
        if table[0][2]==0:
            return(0,2)
        elif table[1][2]==0:
            return(1,2)
        elif table[2][2]==0:
            return(2,2)
    return(None,None)

def nothing(event):
        pass

def ai_print(y,x):
    adding(x,y,"O")
    x = x*200 + 2
    y = y*200 + 2
    yo = Label(xo_board,text=f"O",bg = "white",font=("Arial",110),padx=40,pady=14)
    yo.place(x=x,y=y)
    yoyo1 , yoyo2 = check(table)
    if yoyo1 != None:
        win_time(yoyo1 , yoyo2)
    
def where_win():
    if table[0][0]+table[0][1]+table[0][2]==10:
        if table[0][0]==0:
            return(0,0)
        elif table[0][1]==0:
            return(0,1)
        elif table[0][2]==0:
            return(0,2)
    if table[1][0]+table[1][1]+table[1][2]==10:
        if table[1][0]==0:
            return(1,0)
        elif table[1][1]==0:
            return(1,1)
        elif table[1][2]==0:
            return(1,2)
    if table[2][0]+table[2][1]+table[2][2]==10:
        if table[2][0]==0:
            return(2,0)
        elif table[2][1]==0:
            return(2,1)
        elif table[2][2]==0:
            return(2,2)
    if table[0][0]+table[1][1]+table[2][2]==10:
        if table[0][0]==0:
            return(0,0)
        elif table[2][2]==0:
            return(2,2)
    if table[0][2]+table[1][1]+table[2][0]==10:
        if table[0][2]==0:
            return(0,2)
        elif table[2][0]==0:
            return (2,0)
    if table[0][0]+table[1][0]+table[2][0]==10:
        if table[0][0]==0:
            return(0,0)
        elif table[1][0]==0:
            return(1,0)
        elif table[2][0]==0:
            return(2,0)
    if table[0][1]+table[1][1]+table[2][1]==10:
        if table[0][1]==0:
            return(0,1)
        elif table[1][1]==0:
            return(1,1)
        elif table[2][1]==0:
            return(2,1)
    if table[0][2]+table[1][2]+table[2][2]==10:
        if table[0][2]==0:
            return(0,2)
        elif table[1][2]==0:
            return(1,2)
        elif table[2][2]==0:
            return(2,2)
    return(None,None)

def where_play():
    if table[0][0]+table[0][1]+table[0][2]==5:
        if table[0][0]==5:
            rand = [1,2]
        elif table[0][1]==5:
            rand = [0,2]
        elif table[0][2]==5:
            rand = [0,1]
        return 0,choice(rand)
    if table[1][0]+table[1][1]+table[1][2]==5:
        if table[1][0]==5:
            rand = [1,2]
        elif table[1][1]==5:
            rand = [0,2]
        elif table[1][2]==5:
            rand = [0,1]
        return 1,choice(rand)
    if table[2][0]+table[2][1]+table[2][2]==5:
        if table[2][0]==5:
            rand = [1,2]
        elif table[2][1]==5:
            rand = [0,2]
        elif table[2][2]==5:
            rand = [0,1]
        return 2,choice(rand)
    if table[0][0]+table[1][1]+table[2][2]==5:
        rand = [0,2]
        a = choice(rand)
        return a,a
    if table[0][2]+table[1][1]+table[2][0]==5:
        rand = [0,2]
        a = choice(rand)
        if a==0:
            return 0,2
        elif a==2:
            return 2,0
    if table[0][0]+table[1][0]+table[2][0]==5:
        if table[0][0]==5:
            rand = [1,2]
        elif table[1][0]==5:
            rand = [0,2]
        elif table[2][0]==5:
            rand = [0,1]
        return choice(rand),0
    if table[0][1]+table[1][1]+table[2][1]==5:
        if table[0][1]==5:
            rand = [1,2]
        elif table[1][1]==5:
            rand = [0,2]
        elif table[2][1]==5:
            rand = [0,1]
        return choice(rand),1
    if table[0][2]+table[1][2]+table[2][2]==5:
        if table[0][2]==5:
            rand = [1,2]
        elif table[1][2]==5:
            rand = [0,2]
        elif table[2][2]==5:
            rand = [0,1]
        return choice(rand),2
    return None,None

def againts_ai():
    start()
    global round1
    round1 = 0
    def player0(event):
        global table
        x=event.x
        y=event.y
        x = int(x/200)
        y = int(y/200)
        a = x
        b = y
        x = x*200 + 2
        y = y*200 + 2
        yo = Label(xo_board,text="X",bg = "white",font=("Arial",110),padx=48,pady=14)
        yo.place(x=x,y=y)
        adding(a,b,"X")
        ai0()
        yoyo1 , yoyo2 = check(table)
        if yoyo1 != None:
            win_time(yoyo1 , yoyo2)

    def ai0():
        global round1
        if round1==0:
            if table[1][1]==20:
                a = int(choice(["0","2"]))
                b = int(choice(["0","2"]))                
                ai_print(a,b)
            else:
                table[1][1]=5
                ai_print(1,1)
        else:
            doy2 , dox1 = where()
            doy4 , dox3 = where_win()
            if dox3!= None:
                ai_print(doy4,dox3)
            elif doy2!=None:
                ai_print(doy2,dox1)
            else:
                doy6 , dox5 = where_play()
                if dox5!=None:
                    ai_print(doy6,dox5)
                else:
                    hell = False
                    for i in range(3):
                        for j in range(3):
                            if table[i][j]==0:
                                ai_print(i,j)
                                hell = True
                                break
                        if hell==True:
                            break
        round1 += 1

    def first_player():
        global dude
        dude = 1
        root.destroy()
        global xo_board
        root2=Tk()
        root2.title("its XO bitches!!")
        root2.geometry("600x640")

        xo_board = Canvas(root2,width=595,height=590,bg="#A3E4D7")
        xo_board.pack(side=TOP)
        again(root2)
        for i in range(0,600,200):
            xo_board.create_line(i,0,i,600,width=3)
            xo_board.create_line(0,i,600,i,width=3)
        
        xo_board.bind('<Button-1>',player0)
        root2.mainloop()
        
    def second_player():
        global dude
        dude = 2
        root.destroy()
        global xo_board
        root2=Tk()
        root2.title("its XO bitches!!")
        root2.geometry("600x640")
        xo_board = Canvas(root2,width=595,height=590,bg="#A3E4D7")
        xo_board.pack(side=TOP)
        again(root2)
        for i in range(0,600,200):
            xo_board.create_line(i,0,i,600,width=3)
            xo_board.create_line(0,i,600,i,width=3)
        x = choice([0,2])
        y = choice([0,2])
        ai_print(x,y)
        xo_board.bind('<Button-1>',player1)
        root2.mainloop()

    def player1(event):
        global table
        x=event.x
        y=event.y
        x = int(x/200)
        y = int(y/200)
        a = x
        b = y
        x = x*200 + 2
        y = y*200 + 2
        yo = Label(xo_board,text="X",bg = "white",font=("Arial",110),padx=48,pady=14)
        yo.place(x=x,y=y)
        adding(a,b,"X")
        ai1()
        yoyo1 , yoyo2 = check(table)
        if yoyo1 != None:
            win_time(yoyo1 , yoyo2)
    
    def ai1():
        global round1
        if round1==0:
            if table[0][0]==20:
                if table[2][2]==5:
                    extra0 = choice([0,2])
                    if extra0==0:
                        extra1 = 2
                    else:
                        extra1=0
                    ai_print(extra0,extra1)
                else:
                    ai_print(2,2)
            elif table[0][2]==20:
                if table[2][0]==5:
                    extra0 = choice([0,2])
                    ai_print(extra0,extra0)
                elif table[0][0]==5:
                    ai_print(2,0)
                elif table[2][2]==5:
                    ai_print(2,0)
                else:
                    ai_print(2,0)
            elif table[2][2]==20:
                if table[0][0]==5:
                    extra0 = choice([0,2])
                    if extra0==0:
                        extra1 = 2
                    else:
                        extra1=0
                    ai_print(extra0,extra1)
                else:
                    ai_print(0,0)
            elif table[2][0]==20:
                if table[0][2]==5:
                    extra0 = choice([0,2])
                    if extra0==0:
                        extra1 = 2
                    else:
                        extra1=0
                    ai_print(extra0,extra1)
                else:
                    ai_print(0,2)
            elif table[1][1]==0:
                ai_print(1,1)
            else:
                if table[0][0]==5 and table[2][2]==0:
                    ai_print(2,2)
                elif table[0][2]==5 and table[2][0]==0:
                    ai_print(2,0)
                elif table[2][0]==5 and table[0][2]==0:
                    ai_print(0,2)
                elif table[2][2]==5 and table[0][0]==0:
                    ai_print(0,0)
        elif round1==1:
            dodoy1 , dodox0 = where_win()
            dodoy3 , dodox2 = where()
            if dodox0!=None:
                ai_print(dodoy1,dodox0)
            elif dodox2!=None:
                ai_print(dodoy3,dodox2)
            else:#fix
                if table[0][0]==0 and table[0][1]==0 and table[0][2]==5:
                    ai_print(0,0)
                elif table[0][0]==0 and table[1][0]==0 and table[2][0]==5:
                    ai_print(0,0)
                elif table[0][2]==0 and table[0][1]==0 and table[0][0]==5:
                    ai_print(0,2)
                elif table[0][2]==0 and table[1][2]==0 and table[2][2]==5:
                    ai_print(0,2)
                elif table[2][0]==0 and table[2][1]==0 and table[2][2]==5:
                    ai_print(2,0)
                elif table[2][0]==0 and table[1][0]==0 and table[0][0]==5:
                    ai_print(2,0)
                elif table[2][2]==0 and table[1][2]==0 and table[0][2]==5:
                    ai_print(2,2)
                elif table[2][2]==0 and table[2][1]==0 and table[2][0]==5:
                    ai_print(2,2)
        else:
                dodoy1 , dodox0 = where()
                dodoy3 , dodox2 = where_win()
                if dodox2!=None:
                    ai_print(dodoy3,dodox2)
                elif dodox0!=None:
                    ai_print(dodoy1,dodox0)
                else:
                    if dodox2!=None:
                        ai_print(dodoy3,dodox2)
                    else:
                        dodox5 , dodox6 = where_play()
                        if dodox2!= None:
                            ai_print(dodox5,dodox6)
                        else:
                            hell = False
                            for i in range(3):
                                for j in range(3):
                                    if table[i][j]==0:
                                        ai_print(i,j)
                                        hell = True
                                        break
                                if hell==True:
                                    break
        round1 += 1

    root = Tk()
    root.title("its XO bitches!!")
    root.geometry("280x150")

    screen0 = Frame(root,bg="#DBCFFF",width=100,height=200)
    screen0.pack()
    yo0 = Label(screen0,text="do you wanna go first?",font=("Arial",20),bg="#DBCFFF")
    yo0.pack()
    yo1 = Button(screen0,text="yes",bd=3,width=10,font=("Arial",20),command=first_player)
    yo1.pack()
    yo2 = Button(screen0,text="no ",bd=3,width=10,font=("Arial",20),command=second_player)
    yo2.pack()

    root.mainloop()

def exit():
    quit()

def win_time(a,b):
    xo_board.bind('<Button-1>',nothing)
    if a=="X player 2":
        a = "hey x guy you win!!"
        yo = Label(xo_board,text=f"{a}",bg = "white",font=("Arial",55))
        yo.place(x=0,y=250)
    elif a=="O player 1":
        if dude == 1:
            a = "GAME OVER :D"
            yo = Label(xo_board,text=f"{a}",bg = "white",font=("Arial",55),width=14)
            yo.place(x=0,y=250)
        elif dude == 2:
            a = "GAME OVER :D"
            yo = Label(xo_board,text=f"{a}",bg = "white",font=("Arial",55),width=14)
            yo.place(x=0,y=250)
        else:
            a = "hey o guy you win!!"
            yo = Label(xo_board,text=f"{a}",bg = "white",font=("Arial",55))
            yo.place(x=0,y=250)

def check_draw():
    hoho = True
    hoho1 = False
    for i in table:
        for j in i:
            if j==0:
                hoho = False
                break
        if hoho == False:
            hoho1 = True
            break
    if hoho1 == False:
        xo_board.bind('<Button-1>',nothing)
        yo = Label(xo_board,text="TIE GAME",bg = "white",font=("Arial",55),width=14)
        yo.place(x=0,y=250)

def again(ro):
    yo7 = Button(ro,text="lets play again.",command=lambda: lets_go(ro),bd=3,font=("Arial",14),padx=5,pady=5,width=20,height=1)
    yo7.pack()

lets_go(None)