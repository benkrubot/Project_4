#This will create 10 boxes with integers 1-10 randomly displayed. When the user presses the button, it will call
#the get_smallest_val function and find the smallest number, then change the background of that box, and remove
#the value from the list. The user will have to press the button 10 times, after which all of the numbers have
#been found and then if pressed again the program will break.

from tkinter import *
import random

root = Tk()
root.geometry("500x400")
numbers = []
data_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Creating and randomly populating boxes
for x in range(10):
    j = Text(root, height = 2, width = 30)
    j.place(x = 125, y = 10 + (x * 30))
    j.insert(END, data_set.pop(random.randint(0,len(data_set)-1)))
    numbers.append(j)
#print(numbers) #test

def get_smallest_val():
    #This will find the smallest number in the data set that is being displayed,
    #it will change the color, then remove it from the data set
    global numbers
    global val
    small_num = None
    placeholder = None

    #Iterating through numbers, using get method to get the value for the specified key
    for value in numbers:
        integer = int(value.get("1.0", END).strip())
        print(integer) #test
        if small_num:
            if integer < placeholder:
                small_num = value
                placeholder = integer
        else:
            small_num = value
            placeholder = integer

    #print(numbers) test
    #This will update the display by changing the smallest number background and then
    #removing from the list
    small_num.configure(background = "red")
    numbers.remove(small_num)
    cur_label.configure(text = "Current Lowest Value: {}".format(placeholder))

#Creating button and label
val_but = Button(root, text = "Find the smallest number", command = get_smallest_val)
val_but.place(x = 170, y = 325)
cur_label = Label(root, text = "")
cur_label.place(x = 176, y = 355)

root.mainloop()