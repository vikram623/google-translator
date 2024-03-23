from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
# Here Translator Part
def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_sor.get()
    d=comb_dest.get()
    masg=sor_txt.get(1.0,END)
    textget=change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)
    

# Graphics Part
root =Tk()  #create object
root.title("Translator")
root.geometry("500x700")
root.config(bg="green")

lab_txt=Label(root,text="Translator",font=("Time New Roman",20,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

# making frame
frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="black",bg="green")
lab_txt.place(x=100,y=100,height=20,width=300)

# create source txt
sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=200,width=480)


# create combobox
#  frist creat list
list_text=list(LANGUAGES.values())
 
#  1st combo_box
comb_sor=ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=350,height=40,width=150)
comb_sor.set("english")
button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=350,height=40,width=150)

# 2nd combo_box destination
comb_dest=ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=350,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root,text="Desitnation Text",font=("Time New Roman",20,"bold"),fg="black",bg="green")
lab_txt.place(x=100,y=420,height=20,width=300)

dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=470,height=200,width=480)

root.mainloop()