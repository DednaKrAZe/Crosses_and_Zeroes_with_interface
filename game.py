from tkinter import *

root=Tk()
root.geometry('400x400')
root.title('Крестики-нолики')
move=1
map=[[' ',' ',' '],
     [' ',' ',' '],
     [' ',' ',' ']]

numofcrwin=0
numofzrwin=0

scrhead1=Label(root,text='Крестики')
scrhead1.grid(row=0,column=0)
scrhead2=Label(root,text='Нолики')
scrhead2.grid(row=0,column=1)
scrnums1=Label(root,text=str(numofcrwin))
scrnums1.grid(row=1,column=0)
scrnums2=Label(root,text=str(numofzrwin))
scrnums2.grid(row=1,column=1)
txt=Label(root,text='')

def crosses_wins(map):
    if map[0][0]==map[1][1]==map[2][2]=='X' or map[0][2]==map[1][1]==map[2][0]=='X':
        return True
    for i in range (0,3):
        if map[i][0]==map[i][1]==map[i][2]=='X' or map[0][i]==map[1][i]==map[2][i]=='X':
            return True
    return False

def zeroes_wins(map):
    if map[0][0]==map[1][1]==map[2][2]=='O' or map[0][2]==map[1][1]==map[2][0]=='O':
        return True
    for i in range (0,3):
        if map[i][0]==map[i][1]==map[i][2]=='O' or map[0][i]==map[1][i]==map[2][i]=='O':
            return True
    return False

def resbut():
    btnrst.config(state=['normal'])
    btnrst.place(x=142,y=300)
    btn11.config(state=['disabled'])
    btn12.config(state=['disabled'])
    btn13.config(state=['disabled'])
    btn21.config(state=['disabled'])
    btn22.config(state=['disabled'])
    btn23.config(state=['disabled'])
    btn31.config(state=['disabled'])
    btn32.config(state=['disabled'])
    btn33.config(state=['disabled'])

def m11():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[0][0]==' ':
        if move%2==1:
            btn11.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[0][0]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        else:
            btn11.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[0][0]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1 

def m12():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[0][1]==' ':
        if move%2==1:
            btn12.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[0][1]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        if move%2==0:
            btn12.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[0][1]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1 

def m13():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[0][2]==' ':
        if move%2==1:
            btn13.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[0][2]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        if move%2==0:
            btn13.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[0][2]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1 

def m21():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[1][0]==' ':
        if move%2==1:
            btn21.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[1][0]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        if move%2==0:
            btn21.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[1][0]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1 

def m22():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[1][1]==' ':
        if move%2==1:
            btn22.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[1][1]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        if move%2==0:
            btn22.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[1][1]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1 

def m23():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[1][2]==' ':
        if move%2==1:
            btn23.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[1][2]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        if move%2==0:
            btn23.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[1][2]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1 

def m31():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[2][0]==' ':
        if move%2==1:
            btn31.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[2][0]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        if move%2==0:
            btn31.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[2][0]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1 

def m32():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[2][1]==' ':
        if move%2==1:
            btn32.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[2][1]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        if move%2==0:
            btn32.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[2][1]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1 

def m33():
    global map
    global move
    global numofcrwin
    global numofzrwin
    if map[2][2]==' ':
        if move%2==1:
            btn33.config(text='X',bg='blue',fg='red',state=["disabled"])
            map[2][2]='X'
            if crosses_wins(map):
                numofcrwin+=1
                scrnums1.config(text=str(numofcrwin))
                txt.config(text='Крестики победили')
                txt.place(x=140,y=60)
                return resbut()
        if move%2==0:
            btn33.config(text='O',bg='red',fg='blue',state=["disabled"])
            map[2][2]='O'
            if zeroes_wins(map):
                numofzrwin+=1
                scrnums2.config(text=str(numofzrwin))
                txt.config(text='Нолики победили')
                txt.place(x=145,y=60)
                return resbut()
        if move==9:
            txt.config(text='Ничья')
            txt.place(x=180,y=60)
            return resbut()
        else:
            move+=1

btn11=Button(root,text=' ',width=4,height=2,bg='grey',command=m11)
btn12=Button(root,text=' ',width=4,height=2,bg='grey',command=m12)
btn13=Button(root,text=' ',width=4,height=2,bg='grey',command=m13)
btn21=Button(root,text=' ',width=4,height=2,bg='grey',command=m21)
btn22=Button(root,text=' ',width=4,height=2,bg='grey',command=m22)
btn23=Button(root,text=' ',width=4,height=2,bg='grey',command=m23)
btn31=Button(root,text=' ',width=4,height=2,bg='grey',command=m31)
btn32=Button(root,text=' ',width=4,height=2,bg='grey',command=m32)
btn33=Button(root,text=' ',width=4,height=2,bg='grey',command=m33)

def game():
    global btnstrt
    btnstrt.destroy()
    btn11.place(x=140,y=110)
    btn12.place(x=180,y=110)
    btn13.place(x=220,y=110)
    btn21.place(x=140,y=153)
    btn22.place(x=180,y=153)
    btn23.place(x=220,y=153)
    btn31.place(x=140,y=196)
    btn32.place(x=180,y=196)
    btn33.place(x=220,y=196)

def restart():
    global map
    global move
    txt.config(text=' ')
    txt.place_forget()
    btnrst.config(state=['disabled'])
    btnrst.place_forget()
    move=1
    for i in range (0,3):
        for j in range (0,3):
            map[i][j]=' '
    btn11.config(text=' ',bg='grey',state=["normal"])
    btn12.config(text=' ',bg='grey',state=["normal"])
    btn13.config(text=' ',bg='grey',state=["normal"])
    btn21.config(text=' ',bg='grey',state=["normal"])
    btn22.config(text=' ',bg='grey',state=["normal"])
    btn23.config(text=' ',bg='grey',state=["normal"])
    btn31.config(text=' ',bg='grey',state=["normal"])
    btn32.config(text=' ',bg='grey',state=["normal"])
    btn33.config(text=' ',bg='grey',state=["normal"])

btnstrt=Button(root,text='Старт', width=10,height=2,bg='grey',command=game)
btnrst=Button(root,text='Новая игра',width=15,height=2,bg='grey',fg='black',state=['disabled'],command=restart)

def main_menu():
    btnstrt.place(x=160,y=160)

main_menu()

root.mainloop()