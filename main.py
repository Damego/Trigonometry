import tkinter as tk
from PIL import Image, ImageTk
import random

class Main(tk.Frame):
   def __init__(self):
      super().__init__()

      self.positiveNums = ['2Pi','Pi/6','Pi/4','Pi/3','Pi/2','2Pi/3','3Pi/4','5Pi/6','Pi','7Pi/6','5Pi/4','4Pi/3','3Pi/2','5Pi/3','7Pi/4','11Pi/6']
      self.negativeNums = ['-2Pi', '-11Pi/6', '-7Pi/4', '-5Pi/3', '-3Pi/2', '-4Pi/3', '-5Pi/4', '-7Pi/6', '-Pi', '-5Pi/6', '-3Pi/4', '-2Pi/3', '-Pi/2', '-Pi/3', '-Pi/4', '-Pi/6']
      self.coordsNums = ['1;0','√3/2;1/2','√2/2;√2/2','1/2;√3/2','0;1','-1/2;√3/2','-√2/2;√2/2','-√3/2;1/2','-1;0','-√3/2;-1/2','-√2/2;-√2/2','-1/2;-√3/2','0;-1','1/2;-√3/2','√2/2;-√2/2','√3/2;-1/2']

      img = Image.open("circle.png")
      render = ImageTk.PhotoImage(img)
      self.initil = tk.Label(root, image=render)
      self.initil.image = render
      self.mainMenu()
        
        


   def mainMenu(self):
      self.start1 = tk.Button(root,
                                 text="Положительные числа",
                                 width=20, height=2,
                                 bg = "#246de8", fg="white",
                                 font="Arial 16",
                                 command=lambda: self.application(1))
      self.start1.place(x = 150, y = 50)

      self.start2 = tk.Button(root,
                                 text="Отрицательные числа",
                                 width=20, height=2,
                                 bg = "#246de8", fg="white",
                                 font="Arial 16",
                                 command=lambda: self.application(2))
      self.start2.place(x = 150, y = 150)

      self.start3 = tk.Button(root,
                                 text="Координаты",
                                 width=10, height=2,
                                 bg = "#246de8", fg="white",
                                 font="Arial 16",
                                 command=lambda: self.application(3))
      self.start3.place(x = 200, y = 250)

      self.start4 = tk.Button(root,
                                 text="Все числа",
                                 width=10, height=2,
                                 bg = "#246de8", fg="white",
                                 font="Arial 16",
                                 command=lambda: self.application(4))
      self.start4.place(x = 200, y = 350)



   def createCircle(self):
      self.start1.place_forget()
      self.start2.place_forget()
      self.start3.place_forget()
      self.start4.place_forget()

      self.initil.pack()
      self.ex = tk.Label(root, text="", font="Arial 20")
      self.ex.place(x = 38, y = 440)


      self.btn1 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn1.place(x = 475, y = 200)

      self.btn2 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn2.place(x = 445, y = 95)

      self.btn3 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn3.place(x = 405, y = 50)

      self.btn4 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn4.place(x = 370, y = 25)

      self.btn5 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn5.place(x = 260, y = 3)

      self.btn6 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn6.place(x = 160, y = 25)

      self.btn7 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn7.place(x = 115, y = 55)

      self.btn8 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn8.place(x = 80, y = 97)

      self.btn9 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn9.place(x = 50, y = 200)

      self.btn10 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn10.place(x = 80, y = 305)

      self.btn11 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn11.place(x = 110, y = 350)

      self.btn12 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn12.place(x = 150, y = 395)

      self.btn13 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn13.place(x = 260, y = 420)

      self.btn14 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn14.place(x = 370, y = 395)

      self.btn15 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn15.place(x = 410, y = 345)

      self.btn16 = tk.Button(root,
                                 text="",
                                 width=2, height=1,
                                 bg = "white")
      self.btn16.place(x = 450, y = 295)

      self.play = tk.Button(root,
                                 text="Начать",
                                 width=10, height=1,
                                 bg = "#246de8", fg="white",
                                 font="Arial 16")
      self.play.place(x = 300, y = 440)

      self.btn_back = tk.Button(root, text = "<", font = "Arial 16", command = self.clickedBtnBack)
      self.btn_back.place(relx = 0.01, rely = 0.01)


   def application(self, typeList):
      self.createCircle()

      if typeList == 1:
         self.list = self.positiveNums
         self.play['command'] = lambda: self.newNum(1)
      elif typeList == 2:
         self.list = self.negativeNums
         self.play['command'] = lambda: self.newNum(2)
      elif typeList == 3:
         self.list = self.coordsNums
         self.play['command'] = lambda: self.newNum(3)
      elif typeList == 4:
         self.play['command'] = lambda: self.newNum(4)
         
         
      self.btn1['command'] = lambda: self.check(self.list[0])
      self.btn2['command'] = lambda: self.check(self.list[1])
      self.btn3['command'] = lambda: self.check(self.list[2])
      self.btn4['command'] = lambda: self.check(self.list[3])
      self.btn5['command'] = lambda: self.check(self.list[4])
      self.btn6['command'] = lambda: self.check(self.list[5])
      self.btn7['command'] = lambda: self.check(self.list[6])
      self.btn8['command'] = lambda: self.check(self.list[7])
      self.btn9['command'] = lambda: self.check(self.list[8])
      self.btn10['command'] = lambda: self.check(self.list[9])
      self.btn11['command'] = lambda: self.check(self.list[10])
      self.btn12['command'] = lambda: self.check(self.list[11])
      self.btn13['command'] = lambda: self.check(self.list[12])
      self.btn14['command'] = lambda: self.check(self.list[13])
      self.btn15['command'] = lambda: self.check(self.list[14])
      self.btn16['command'] = lambda: self.check(self.list[15])

   def check(self, pos):
      if pos == self.res:
         self.ex['fg'] = 'green'
      else:
         self.ex['fg'] = 'red'

   def newNum(self,typeList):
      if typeList == 4:
         all_nums = [self.positiveNums,self.negativeNums,self.coordsNums]
         self.preRes = random.choice(all_nums)
         self.res = random.choice(self.preRes)
         self.list = self.preRes
      else:
         self.res = random.choice(self.list)
      self.ex['text'] = self.res
      self.play['text'] = "Новое число"
      self.ex['fg'] = 'black'



   def clickedBtnBack(self):
      self.btn_back.place_forget()
      self.btn1.place_forget()
      self.btn2.place_forget()
      self.btn3.place_forget()
      self.btn4.place_forget()
      self.btn5.place_forget()
      self.btn6.place_forget()
      self.btn7.place_forget()
      self.btn8.place_forget()
      self.btn9.place_forget()
      self.btn10.place_forget()
      self.btn11.place_forget()
      self.btn12.place_forget()
      self.btn13.place_forget()
      self.btn14.place_forget()
      self.btn15.place_forget()
      self.btn16.place_forget()
      self.ex.place_forget()
      self.play.place_forget()
      self.initil.forget()

      self.start1.place(x = 150, y=50)
      self.start2.place(x = 150, y=150)
      self.start3.place(x = 200, y=250)
      self.start4.place(x = 200, y=350)




if __name__ == "__main__":
   root = tk.Tk()
   root.title("Тригонометрия")
   root.geometry("550x500+700+300")
   root.resizable(False, False)

   

   app = Main()

   root.mainloop()
