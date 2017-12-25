# import the library
from appJar import gui
# create a GUI variable called app
app = gui()


def bla(haha):
        # print(btnName)
        # print("bla")
        app.setTextAreaState("max_text", "normal")
        app.setTextArea("max_text", "Hallo \n\n Mehrzeilig!! \n", end=True, callFunction=True)
        app.setTextAreaState("max_text", "disabled")



app.addTextArea("max_text")


# add & configure widgets - widgets get a name, to help referencing them later
app.addButton("Welcome to appJar", bla )    
app.addButtonBg("Welcome to appJar", "red")





# start the GUI
app.go()
