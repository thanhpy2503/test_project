from os import read
from tkinter import *
import source
import time
from importlib import reload
reload(source) # dùng hàm này để load module source

# toạ cửa sổ cho game đ
window = Tk()
window.title("game")
window.resizable(height=FALSE,width=FALSE)
window.minsize(width=800,height=500)
# vẽ các hình lên cửa sổ
c = Canvas(window,bg="white",height=500,width=800)
# tạo đường dẫn đến các hình ảnh
img = PhotoImage(file="image\\image_bg1.png")
img2 = PhotoImage(file="image\\image_bg2.png")
img3 = PhotoImage(file="image\\image_bg3.png")

Label(window,image=img).place(x=0,y=0,relheight=1,relwidth=1)#trang đầu tiên
c.pack()



lst = window.place_slaves()# danh sách chứa các vật thể trên màn hình

def choose_1():#trang đầu tiên
    Label(window,image=img2).place(x=0,y=0,relheight=1,relwidth=1)
    Button(window,text="attack",width=20,font=("algerian"),justify=CENTER,activebackground="red",command=play).place(x=100,y=400)
    Button(window,text="rule",width=20,font=("algerian"),justify=CENTER,activebackground="green",command=rule_play).place(x=500,y=400)
    c.pack()

def rule_play():# đọc cách chơi ở hàm này
    rule = open("data\\rule.txt",mode='r',encoding='UTF-8')# tệp chưa quy tắc
    doc = rule.read()
    
    Label(window,text=doc,font=("aria",18),justify=LEFT).place(x=0,y=0,relheight=1,relwidth=1)
    Button(window,text="back",font=("algerian"),width=20,justify=CENTER,activeforeground="blue",command=choose_1).place(x=450,y=400)
    c.pack()
def play():# quyết định chơi hay thôi     
    Label(window,image=img3,justify=RIGHT).place(x=0,y=0,relheight=1,relwidth=1)
    Button(window,text="readly",font=("algerian"),width=20,justify=CENTER,activeforeground="red",command=handle2).place(x=500,y=450)
    Button(window,text="cancel",font=("algerian"),width=20,justify=CENTER,activeforeground="blue",command=choose_1).place(x=95,y=450)
    c.pack()
def handle2():# hàm xử lí khi chơi
    lst = window.place_slaves()# danh sách chứa các vật thể trên màn hình
    for i in lst:
        i.destroy()
    source.main()

def sumary_end():# hiện lên máu các người chơi sau một vòng đấu
    sumary_end = open("data\\sumary.txt",mode='r',encoding='UTF-8')
    doc2 = sumary_end.read()
    Label(window,text=doc2,font=("algerian",60),fg="black",justify=LEFT).place(x=0,y=0,relheight=1,relwidth=1)
    c.pack()


 
Button(window,text="ok",fg="blue",font=("algerian"),justify=CENTER,width=20,activebackground="red",activeforeground="black",command=choose_1).place(x=310,y=400)
window.mainloop()

 
    
    

    