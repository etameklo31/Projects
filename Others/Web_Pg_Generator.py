import tkinter as tk
from tkinter import simpledialog
import webbrowser


def generate():
    f = open('demo.html', 'w')
    f.write('<html>'
                '<body>'
                    '<h1>'
                        '{}'
                    '</h1>'
                '</body>'
            '</html>'.format(Input))
    f.close()

    new = 2
    url = 'demo.html'

    webbrowser.open(url, new = new)

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
Input = simpledialog.askstring(title="Web Gen", prompt="Input:")

# check it out
print(Input)
    
generate()


