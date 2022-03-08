def parse(link):
    total=  0.0
    fobWords = ["wallet", "Wallet", "div"]
    refundCount = 0
    with open(link,"r") as file:
        lines = file.readlines()
        for count in range(len(lines)):
            if "refunded" in lines[count]:
                refundCount = 6
            if refundCount>0:
                refundCount-=1
                if "£" in lines[count]:
                    refLine = ((lines[count].strip("							£")).strip("Â£")).split(
                        "					")
                    total -= float(refLine[0])

            elif "£" in lines[count] and not any(elem in lines[count] for elem in fobWords):
                curLine = ((lines[count].strip("							£")).strip("Â£")).split(
                    "					")
                total += float(curLine[0])

        return(total)

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "RUN"
        self.hi_there["command"] = self.run
        self.hi_there.pack(side="top")

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def run(self):
        inp = self.entry.get()
        label = tk.Label(root, text=("£",parse(inp)))
        label.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()

