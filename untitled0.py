from tkinter import * 

root = Tk()

def window(main):
    main.title('Our Program')
    main.update_idletasks()
    width = 500
    height = 500 
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenwidth() // 2) - (height // 2)
    main.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    def main_content():
        hello = Label1(root, text="Hello from a label widget")
        hello.pack()
        
        
window(root)
main_content()
mainloop()