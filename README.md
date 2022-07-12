# Tkinter Tutorial for Beginners

When I was getting started with Python I loved writing Tkinter GUIs. At
first they felt really complicated because the tutorial I was following
wasn't very good. Even the hello world example had a class with
inheritance, and I didn't know what was a class at the time.

This tutorial consists of minimal examples and explains common mistakes.
You don't need to have any experience in GUI programming to read this
tutorial, and you don't even need to know what is a GUI. All you need is
basic Python skills.

**If you need help**, you're not alone! Just let me know

## Which GUI toolkit?

GUI is short for Graphical User Interface. It means a program that we
can use without a command prompt or a terminal, like a web browser, a
file manager or an editor.

Tkinter is an easy way to write GUIs in Python. Unlike bigger GUI
toolkits like Qt and GTK+, tkinter comes with Python so many Python
users have it already. Tkinter works on Windows, Mac OSX and Linux, so
it's a good choice for writing cross-platform programs. For example, I
have written [Porcupine](https://github.com/Akuli/porcupine) using
tkinter.

Tkinter is not a good choice if you want to write programs mainly for
Linux users. Most Linux distributions don't come with tkinter and
tkinter applications look different than Qt and GTK+ applications on
Linux. On the other hand, many Linux distributions come with
[GTK+](https://python-gtk-3-tutorial.readthedocs.io/en/latest/), so I
recommend using that if you want to write programs for Linux users.

You can also use [PyQt](http://zetcode.com/gui/pyqt5/) if you want to
write cross-platform GUI programs. It doesn't come with Python and
installing it can be difficult, but PyQt programs look good on Windows,
Mac and Linux.

Tkinter is light, but it's also limited in some ways. For example, you
can't write a web browser in tkinter, but it's possible to write web
browsers in GTK+ and PyQt. Simpler things like text editors and music
players can be written in tkinter.

## List of contents
> Check out [docs] branch

<h1>Quick Revision</h1>

## Template
```python
# importing 
from tkinter import *

# GUI STARTS HERE
root = Tk()
.
.
# Gui Code Here
.
.
# GUI ENDS HERE
root.mainloop()
```
### BASIC STARTER TEMPLATE TKINTER 

```python
# importing 
from tkinter import *

 # GUI STARTS HERE
 root = Tk()

root.title("Jocefyneroot Personal - Calculator")
root.geometry("600x700")
root.minsize(400,400)
root.maxsize(500,610)

 # GUI ENDS HERE
 root.mainloop()
```

## Operator, Description and Code Example
----------------------
SL.NO.  | Name | Description | code
------------- | -------------|------------- | -------------
1 | Button | The Button widget is used to display buttons in your application.| [ReadMore](https://www.tutorialspoint.com/python/tk_button.htm)
2 |Canvas | The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.| [ReadMore](https://www.tutorialspoint.com/python/tk_canvas.htm)
3 |Checkbutton | The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.| [ReadMore](https://www.tutorialspoint.com/python/tk_checkbutton.ht)
4 |Entry | The Entry widget is used to display a single-line text field for accepting values from a user.| [ReadMore](https://www.tutorialspoint.com/python/tk_entry.htm)
5 |Frame | The Frame widget is used as a container widget to organize other widgets.| [ReadMore](https://www.tutorialspoint.com/python/tk_frame.htm)
6 |Label | The Label widget is used to provide a single-line caption for other widgets. It can also contain images.| [ReadMore](https://www.tutorialspoint.com/python/tk_label.htm)
7 |Listbox | The Listbox widget is used to provide a list of options to a user.| [ReadMore](https://www.tutorialspoint.com/python/tk_listbox.htm)
8 |Menubutton | The Menubutton widget is used to display menus in your application.| [ReadMore](https://www.tutorialspoint.com/python/tk_menubutton.htm)
9 |Menu | The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.| [ReadMore](https://www.tutorialspoint.com/python/tk_menu.htm)
10|Message | The Message widget is used to display multiline text fields for accepting values from a user.| [ReadMore](https://www.tutorialspoint.com/python/tk_message.htm)
11|Radiobutton | The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time.| [ReadMore](https://www.tutorialspoint.com/python/tk_radiobutton.ht)
12|Scale | The Scale widget is used to provide a slider widget.| [ReadMore](https://www.tutorialspoint.com/python/tk_scale.htm)
13|Scrollbar | The Scrollbar widget is used to add scrolling capability to various widgets, such as list boxes.| [ReadMore](https://www.tutorialspoint.com/python/tk_scrollbar.htm)
14|Text | The Text widget is used to display text in multiple lines.| [ReadMore](https://www.tutorialspoint.com/python/tk_text.htm)
15|Toplevel | The Toplevel widget is used to provide a separate window container.| [ReadMore](https://www.tutorialspoint.com/python/tk_toplevel.htm)
16|Spinbox | The Spinbox widget is a variant of the standard Tkinter Entry widget, which can be used to select from a fixed number of values.| [ReadMore](https://www.tutorialspoint.com/python/tk_spinbox.htm)
17|PanedWindow | A PanedWindow is a container widget that may contain any number of panes, arranged horizontally or vertically.| [ReadMore](https://www.tutorialspoint.com/python/tk_panedwindow.ht)
18|LabelFrame | A labelframe is a simple container widget. Its primary purpose is to act as a spacer or container for complex window layouts.| [ReadMore](https://www.tutorialspoint.com/python/tk_labelframe.htm)
19|tkMessageBox | This module is used to display message boxes in your applications.| [ReadMore](https://www.tutorialspoint.com/python/tk_messagebox.htm)


## Code Example Comming soon