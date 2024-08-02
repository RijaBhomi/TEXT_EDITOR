from tkinter import*
from tkinter import filedialog
from tkinter import ttk
import os
from tkinter import messagebox
from tkinter import simpledialog

def openFile():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'r') as file:
            text= file.read()
            editor= Text(window)
            editor.insert('1.0', text)
            filename= os.path.basename(filepath)
            title= os.path.splitext(filename)[0]   #extracting title without etensions
            notebook.add(editor, text=title)
           

def saveFile():
    selected_tab = notebook.select()
    text_widget = notebook.nametowidget(selected_tab)
    content = text_widget.get('1.0', 'end-1c')

    filepath = filedialog.asksaveasfilename(defaultextension='.txt',
                                            filetypes=[("Text file", ".txt"),
                                                       ("HTML file", ".html"),
                                                       ("All files", ".*")])
    if filepath:
        with open(filepath, 'w') as file:
            file.write(content)




#Function to change the theme
def changeTheme(theme):
    selected_tab= notebook.select()
    text_widget= notebook.nametowidget(selected_tab)
    if theme=="Light":
        text_widget.config(bg="white", fg="black")
    elif theme== "Dark":
        text_widget.config(bg="#2b2a2a", fg="white")
    elif theme== "Read":
        text_widget.config(bg="#FBF0D9", fg="#5F4B32")
    

#implementing cut copy and paste functions
def cut():
    selected_tab= notebook.select()
    text_widget= notebook.nametowidget(selected_tab)

    text_widget.event_generate("<<Cut>>")

def copy():
    selected_tab = notebook.select()
    text_widget = notebook.nametowidget(selected_tab)
    text_widget.event_generate("<<Copy>>")

   

def paste():
    selected_tab = notebook.select()
    text_widget = notebook.nametowidget(selected_tab)
    text_widget.event_generate("<<Paste>>")

def wordCount():
    selected_tab= notebook.select()
    text_widget= notebook.nametowidget(selected_tab)
    content= text_widget.get('1.0', 'end-1c')

    #count words
    words= content.split()
    num_words= len(words)

    #count characters
    num_characters= len(content)

    #count lines
    num_lines= content.count('\n')+1 #count '/n' charcters to get numbers of lines

    #Display word count in a messagebox
    message= f"Word count: {num_words}\nCharacter count: {num_characters}\nLine count: {num_lines}"
    messagebox.showinfo("Word Count", message)

    

def main():
    global window
    window = Tk()
    window.title("Text Titan")
    window.iconbitmap("C:\\Users\\User\\Downloads\\editor logo.jpg")

    global notebook
    notebook = ttk.Notebook(window)
    notebook.pack(expand=True, fill='both')

     #create a default tab
    default_editor= Text(window)
    notebook.add(default_editor, text= "Untitled")

    

    #images for file menu
    openImage= PhotoImage(file="C:\\Users\\User\\Downloads\\open.png")
    openImage= openImage.subsample(25,25)
    saveImage= PhotoImage(file="C:\\Users\\User\\Downloads\\savee.png")
    saveImage= saveImage.subsample(100,100)
    exitImage= PhotoImage(file="C:\\Users\\User\\Downloads\\exitttt.png")
    exitImage= exitImage.subsample(20,20)

    #images for edit menu
    cutImage= PhotoImage(file='C:\\Users\\User\\Downloads\\copy.png')
    cutImage= cutImage.subsample(20,20)
    copyImage= PhotoImage(file='C:\\Users\\User\\Downloads\\cut.png')
    copyImage= copyImage.subsample(20,20)
    pasteImage= PhotoImage(file='C:\\Users\\User\\Downloads\\paste.png')
    pasteImage= pasteImage.subsample(20,20)

    #images for setting menu
    lightImage= PhotoImage(file='C:\\Users\\User\\Downloads\\sun.png')
    lightImage= lightImage.subsample(20,20)
    darkImage= PhotoImage(file='C:\\Users\\User\\Downloads\\dark.png')
    darkImage= darkImage.subsample(20,20)
    readImage= PhotoImage(file='C:\\Users\\User\\Downloads\\reading-mode.png')
    readImage= readImage.subsample(20,20)






    menubar = Menu(window)
    window.config(menu=menubar)

    fileMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Open", command=openFile,image= openImage,compound= 'left', accelerator="Ctrl+O" )
    fileMenu.add_command(label="Save", command=saveFile,image= saveImage,compound= 'left', accelerator="Ctrl+S")
    
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit, image= exitImage,compound= 'left' )

    #Bind keyword shortcuts
    window.bind_all("<Control-o>", lambda event: openFile())
    window.bind_all("<Control-s>", lambda event: saveFile())


    editMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Cut", command=cut, image= cutImage,compound= 'left', accelerator='Ctrl+X')
    editMenu.add_command(label="Copy", command=copy, image=copyImage,compound= 'left', accelerator='Ctrl+C' )
    editMenu.add_command(label="Paste", command=paste, image= pasteImage,compound= 'left', accelerator='Ctrl+V')

    window.bind_all("<Control-x>", lambda event: cut())
    window.bind_all("<Control-c>", lambda event: copy())
    window.bind_all("<Control-v>", lambda event: paste())



    #for choosing themes
    settingsMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Settings", menu=settingsMenu)
    themesMenu= Menu(settingsMenu, tearoff= 0)
    settingsMenu.add_cascade(label="Themes", menu=themesMenu)
    themesMenu.add_command(label="Light", command=lambda: changeTheme("Light"), image=lightImage, compound= 'left' )
    themesMenu.add_command(label="Dark", command= lambda:changeTheme("Dark"), image=darkImage, compound= 'left')
    themesMenu.add_command(label="Read", command= lambda:changeTheme("Read"), image=readImage, compound= 'left')


    #Menu to count words
    toolsMenu= Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Tools", menu= toolsMenu)
    toolsMenu.add_command(label="Word Count", command=wordCount)

    window.mainloop()

if __name__ == "__main__":
    main()