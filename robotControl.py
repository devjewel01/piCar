import cv2  
from tkinter import *  
from PIL import Image, ImageTk
import RPi.GPIO as pin   
from motor import Forward, Backward, Stop, Left, Right

pin.setwarnings(False)
pin.setmode(pin.BOARD)

msg =''  #message variable

#width, height = 800, 500  #setting widht and height

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)

root = Tk()
root.title("RPI Robot Control Panel")

#main label for showing the feed
imagel = Label(root)
imagel.pack()

# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
# org 
org = (30, 20) 
# fontScale 
fontScale = 0.7
# Blue color in BGR 
color = (255, 255, 255)  
# Line thickness of 2 px 
thickness = 2


notif = ''

#load background and button images
for_img = 'image/f.gif'
left_img = 'image/l.gif'
right_img = 'image/r.gif'
back_img = 'image/b.gif'
quit_img = 'image/close.gif'

msg = ''



def forward():
    """forward motion"""
    print("Going Forward Baby.")
    global msg
    msg = 'Going Forward'
    Forward()
    notlabel.config(text=" man keya liya hain")
    notif = 'shamne jai vai'
    return

def backward():
    """backward motion"""
    print("Going back! Watch OUT!!") 
    global msg
    msg = 'Going BACKWARD' 
    Backward()
    notlabel.config(text=" pichhe dekh madar toast")
    return


def left():
    """go left"""
    print("Going left Baby.")
    global msg
    msg = 'Going LEFT'
    Left()
    notlabel.config(text=" dili to bam haat voira")
    notif = 'baaye jai vai'
    return

def right():
    """go right"""
    global msg
    msg = 'Going RIGHT'
    print("Going right man.")
    Right()
    notlabel.config(text=" daye dekh")  
    notif = 'dane jai vai'
    return

def msg_default():
    global msg
    msg = ''
  
def notification():
    global notif   
    return notif

def check_faces(f):  
    faces = face_cascade.detectMultiScale(f, scaleFactor = 1.5, minNeighbors = 5)
    for(x, y, w, h) in faces:
        print('Face found\n')
        roi_f = f[y: y+h, x: x+w] 
        
        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(f, (x,y), (end_cord_x, end_cord_y), color, stroke)
        
        return f
    

def get_frame():
    print("chhobi lagbo vai.")
    ret, frame = cap.read()
    return frame

def update():
    """update frames."""
    global msg
    print("dak porse vai")
    frame = get_frame()  
    cv2.putText(frame, msg, org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    

    try:
        cv2.image = check_faces(frame)
    except:
        pass


    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)

    imagel.imgtk = imgtk
    imagel.configure(image=imgtk)      
    msg_default() 
    pins_default()
    
    imagel.after(15, update)


#read the image for tk
im_f = PhotoImage(file= for_img)
im_l = PhotoImage(file= left_img)
im_r = PhotoImage(file= right_img)
im_b = PhotoImage(file= back_img)

im_quit = PhotoImage(file=quit_img)


#buttons
for_but = Button(root,text="<< Left",repeatdelay=15,repeatinterval=10, command=forward)
for_but.config(image=im_f, fg='gray', border=0, borderwidth=0, bg='black')
for_but.place(x=540, y=250)

left_but = Button(root,repeatdelay=15,repeatinterval=10, command=left)
left_but.config(image=im_l,border=0,borderwidth=0, bg='black' )
left_but.place(x=500, y=300)

right_but = Button(root,repeatdelay=15,repeatinterval=10, command=right)
right_but.config(image=im_r,border=0,borderwidth=0, bg='black')
right_but.place(x=580, y=300)

back_but = Button(root, repeatdelay=15, repeatinterval=10, command=backward)
back_but.config(image=im_b, border=0,borderwidth=0, bg='black')
back_but.place(x=540, y = 350)

quit_but = Button(root, text='Quit', command=root.destroy)
quit_but.config(image = im_quit, bg='red')
quit_but.place(x=0, y=0)

msg = ''
msg_default()

update()

root.resizable(0, 0)

root.mainloop()
pin.cleanup()

