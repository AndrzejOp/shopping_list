from tkinter import *


def done():
    food = []
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    print("You have ordered: ")
    for i in food:
        print(i + ", ")


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia', 50),
                  width=15,
                  selectmode=MULTIPLE,
                  )
listbox.pack()
listbox.insert(1, "watermelon")
listbox.insert(2, "chicken nuggets")
listbox.insert(3, "cool-aid")

entry_box = Entry(window)
entry_box.pack()

done_button = Button(text='Done', command=done)
done_button.pack()

add_button = Button(text='Add own item', command=add)
add_button.pack()

delete_button = Button(text='Delete item', command=delete)
delete_button.pack()

listbox.config(height=listbox.size())
window.mainloop()
