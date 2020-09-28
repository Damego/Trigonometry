import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class Main(ttk.Frame):
   def __init__(self):
      super().__init__()

      self.positiveNums = ['2Pi','Pi/6','Pi/4','Pi/3','Pi/2','2Pi/3','3Pi/4','5Pi/6','Pi','7Pi/6','5Pi/4','4Pi/3','3Pi/2','5Pi/3','7Pi/4','11Pi/6']
      self.negativeNums = ['-2Pi', '-11Pi/6', '-7Pi/4', '-5Pi/3', '-3Pi/2', '-4Pi/3', '-5Pi/4', '-7Pi/6', '-Pi', '-5Pi/6', '-3Pi/4', '-2Pi/3', '-Pi/2', '-Pi/3', '-Pi/4', '-Pi/6']
      self.coordsNums = ['1;0','√3/2;1/2','√2/2;√2/2','1/2;√3/2','0;1','-1/2;√3/2','-√2/2;√2/2','-√3/2;1/2','-1;0','-√3/2;-1/2','-√2/2;-√2/2','-1/2;-√3/2','0;-1','1/2;-√3/2','√2/2;-√2/2','√3/2;-1/2']

      img = Image.open("circle.png")
      render = ImageTk.PhotoImage(img)
      self.initil = tk.Label(root, image=render)
      self.initil.image = render

      self.startMenu()
        

   def startMenu(self):
      self.startFreeModeBtn = tk.Button(root,
                                 text="Работа с кругом",
                                 width=20, height=2,
                                 bg = "#246de8", fg="white",
                                 font="Arial 16",
                                 command=self.mainMenu)
      self.startFreeModeBtn.place(x = 150, y = 50)

      self.startExamModeBtn = tk.Button(root,
                                 text="Работа без круга",
                                 width=20, height=2,
                                 bg = "#246de8", fg="white",
                                 font="Arial 16",
                                 command=self.SecondStartMenu)
      self.startExamModeBtn.place(x = 150, y = 150)


   def forgetStartMenu(self):
      self.startFreeModeBtn.place_forget()
      self.startExamModeBtn.place_forget()


   def mainMenu(self):
      self.forgetStartMenu()
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
      self.currentExercise = tk.Label(root, text="", font="Arial 20")
      self.currentExercise.place(x = 150, y = 450)

      self.allExercisesLabel = tk.Label(root, text="Всего примеров: ", font="Arial 8")
      self.allExercisesLabel.place(x = 38, y = 440)

      self.successExercisesLabel = tk.Label(root, text="Правильных: ", font="Arial 8")
      self.successExercisesLabel.place(x = 38, y = 460)

      self.wrongExercisesLabel = tk.Label(root, text="Ошибок: ", font="Arial 8")
      self.wrongExercisesLabel.place(x = 38, y = 480)


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

      self.newNumButton = tk.Button(root,
                                 text="Начать",
                                 width=10, height=1,
                                 bg = "#246de8", fg="white",
                                 font="Arial 16")
      self.newNumButton.place(x = 300, y = 440)

      self.btn_back = tk.Button(root, text = "<", font = "Arial 16", command = self.pressedButtonBack)
      self.btn_back.place(relx = 0.01, rely = 0.01)


   def application(self, typeList):
      self.quantityExercises = 0
      self.successQuantityExercises = 0
      self.wrongQuantityExercises = 0
      self.addSuccesfulExercice = 0
      self.createCircle()

      if typeList == 1:
         self.list = self.positiveNums
         self.newNumButton['command'] = lambda: self.newNum(1)
      elif typeList == 2:
         self.list = self.negativeNums
         self.newNumButton['command'] = lambda: self.newNum(2)
      elif typeList == 3:
         self.list = self.coordsNums
         self.newNumButton['command'] = lambda: self.newNum(3)
      elif typeList == 4:
         self.newNumButton['command'] = lambda: self.newNum(4)
         
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


   def check(self, position):
      if position == self.result:
         self.currentExercise['fg'] = 'green'
         self.addSuccesfulExercice = 1
      else:
         self.currentExercise['fg'] = 'red'
         self.wrongQuantityExercises += 1
         self.wrongExercisesLabel['text'] = f"Ошибок: {self.wrongQuantityExercises}"


   def newNum(self,typeList):
      if typeList == 4:
         all_nums = [self.positiveNums,self.negativeNums,self.coordsNums]
         self.preResult = random.choice(all_nums)
         self.result = random.choice(self.preResult)
         self.list = self.preResult
      else:
         self.result = random.choice(self.list)
      self.currentExercise['text'] = self.result
      self.newNumButton['text'] = "Новое число"
      self.currentExercise['fg'] = 'black'
      self.quantityExercises += 1
      self.allExercisesLabel['text'] = f"Всего примеров: {self.quantityExercises}"

      if self.addSuccesfulExercice == 1:
         self.successQuantityExercises += 1
         self.successExercisesLabel['text'] = f"Правильных: {self.successQuantityExercises}"


   def pressedButtonBack(self):
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
      self.currentExercise.place_forget()
      self.newNumButton.place_forget()
      self.initil.forget()
      self.allExercisesLabel.place_forget()
      self.successExercisesLabel.place_forget()
      self.wrongExercisesLabel.place_forget()

      self.quantityExercises = 0
      self.successQuantityExercises = 0
      self.wrongQuantityExercises = 0
      self.addSuccesfulExercice = 0

      self.startMenu()


   # Second Menu
   def SecondStartMenu(self):
      self.forgetStartMenu()
      style = ttk.Style(root)
      style.configure("TButton", width = 18,padding = 15,font = "Arial 26")
      self.StartButton_1_2 = ttk.Button(root, text = "Координата - число", style = "TButton", command =lambda:  self.preSecondMenu(1))
      self.StartButton_1_2.place(x = 85, y = 150)
      self.StartButton_2_1 = ttk.Button(root, text = "Число - координата", style = "TButton", command =lambda:  self.preSecondMenu(2))
      self.StartButton_2_1.place(x = 85, y = 250)

   def preSecondMenu(self, gameType):
      self.StartButton_1_2.place_forget()
      self.StartButton_2_1.place_forget()
      self.StartButton = ttk.Button(root, text = "Начать", style = "TButton", command =lambda:  self.SecondMenu(gameType))
      self.StartButton.place(x = 85, y = 150)


   def SecondMenu(self, gameType):
      self.StartButton.place_forget()
      style = ttk.Style(root)
      style.configure("TButton", width = 12, font = "Arial 12")
      style.configure("TCombobox", font = "Arial 12")

      self.combobox = ttk.Combobox(root, width=15, height = 20, font = "Arial 12", style = "TCombobox")
      

      self.checkButton = ttk.Button(root, text = "Проверить", command =lambda: self.check2(gameType))
      self.checkButton.place(x = 300, y = 100)

      self.JustLabel = ttk.Label(root, text = "", font = "Arial 12")
      self.JustLabel.place(x = 10, y = 100)

      self.allExercisesLabel = ttk.Label(root, text = "Всего примеров:", font = "Arial 12")
      self.allExercisesLabel.place(x = 10, y = 250)
      self.quantityExercises = 0

      self.successExercisesLabel = ttk.Label(root, text = "Правильных:", font = "Arial 12")
      self.successExercisesLabel.place(x = 10, y = 275)
      self.successQuantityExercises = 0

      self.wrongExercisesLabel = ttk.Label(root, text = "Неправильных:", font = "Arial 12")
      self.wrongExercisesLabel.place(x = 10, y = 300)
      self.wrongQuantityExercises = 0

      self.buttonBack = tk.Button(root, text = "<", font = "Arial 16", command = self.pressedBackButtonSecondMenu)
      self.buttonBack.place(relx = 0.01, rely = 0.01)
      self.newNum2(gameType)


   def newNum2(self, gameType):
      self.answerID = random.randint(0,15)
      
      if gameType == 1:
         self.combobox['values'] = self.positiveNums
         self.combobox.place(x = 100, y = 100)
         self.list = self.coordsNums
         self.question = self.list[self.answerID]
         self.compAnswer = self.positiveNums[self.answerID]
         self.JustLabel['text'] = self.question
      elif gameType == 2:
         self.combobox['values'] = self.coordsNums
         self.combobox.place(x = 100, y = 100)
         self.list = self.positiveNums 
         self.question = self.list[self.answerID]
         self.compAnswer = self.coordsNums[self.answerID]
         self.JustLabel['text'] = self.question
      

   def check2(self, gameType):
      self.userAnswer = self.combobox.get()
      if self.compAnswer == self.userAnswer:
         self.successQuantityExercises += 1
         self.quantityExercises += 1
         self.allExercisesLabel['text'] = f"Всего примеров: {self.quantityExercises}"
         self.successExercisesLabel['text'] = f"Правильных: {self.successQuantityExercises}"
         self.newNum2(gameType)
      else:
         self.wrongQuantityExercises += 1
         self.quantityExercises += 1
         self.allExercisesLabel['text'] = f"Всего примеров: {self.quantityExercises}"
         self.wrongExercisesLabel['text'] = f"Неправильных: {self.wrongQuantityExercises}"
         self.newNum2(gameType)


   def pressedBackButtonSecondMenu(self):
      self.buttonBack.place_forget()
      self.JustLabel.place_forget()
      self.successExercisesLabel.place_forget()
      self.allExercisesLabel.place_forget()
      self.wrongExercisesLabel.place_forget()
      self.combobox.place_forget()
      self.checkButton.place_forget()
      self.startMenu()



if __name__ == "__main__":
   root = tk.Tk()
   root.title("Тригонометрия")
   root.geometry("550x500+700+300")
   root.resizable(False, False)
   app = Main()
   root.mainloop()
