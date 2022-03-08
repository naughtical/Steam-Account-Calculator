import tkinter as tk


def parse(link):
    total = 0.0
    fobWords = ["wallet", "Wallet", "div"]
    refundCount = 0

    # read in file and append to lines
    with open(link, "r") as file:
        lines = file.readlines()

        # for every line, check if refunded, else check if its got a price
        for count in range(len(lines)):
            if "refunded" in lines[count]:
                refundCount = 6

            elif refundCount > 0:
                # count down till after a price, then take away the price from the total
                refundCount -= 1
                if "£" in lines[count]:
                    refLine = ((lines[count].strip("							£")).strip("Â£")).split(
                        "					")
                    total -= float(refLine[0])

            elif "£" in lines[count] and not any(elem in lines[count] for elem in fobWords):
                # strip the non price bits away, then split into an array and add price to total
                curLine = ((lines[count].strip("							£")).strip("Â£")).split(
                    "					")
                total += float(curLine[0])

        return (total)


# Tkinter setup
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
        # get the link, and add a label to the gui
        inp = self.entry.get()
        label = tk.Label(root, text=("£", parse(inp)))
        label.pack()


# run tkinter stuff
root = tk.Tk()
app = Application(master=root)
app.mainloop()
