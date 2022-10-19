import tkinter as tk

class DimensionWindow(tk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)

        type = tk.Frame(self)
        type.columnconfigure(1, weight=1)
        tk.Label(type, text="Type:").grid(row=0, column=0)
        typeOptions = ["Card Deck", "Two-Part Box", "Tuck Box"]
        self.typeChosen = tk.StringVar()
        self.typeChosen.set("Card Deck")
        typeDrop = tk.OptionMenu(type,
                                 self.typeChosen, *typeOptions)
        typeDrop.grid(row=0, column=1, sticky=tk.EW)
        type.grid(row=0, column=0, sticky=tk.EW)

        dims = tk.Frame(self)
        tk.Label(dims, text="W:").grid(row=0, column=0)
        tk.Label(dims, text="H:").grid(row=0, column=2)
        tk.Label(dims, text="D:").grid(row=0, column=4)

        self.widthEntry = tk.Entry(dims, width=3)
        self.widthEntry.insert(0, data['width'])
        self.widthEntry.grid(row=0, column=1)
        self.heightEntry = tk.Entry(dims, width=3)
        self.heightEntry.insert(0, data['height'])
        self.heightEntry.grid(row=0, column=3)
        self.depthEntry = tk.Entry(dims, width=3)
        self.depthEntry.insert(0, data['depth'])
        self.depthEntry.grid(row=0, column=5)

        dims.grid(row=1, column=0, sticky=tk.EW)

        units = tk.Frame(self)
        units.columnconfigure(1, weight=1)
        tk.Label(units, text="Units:").grid(
            row=0, column=0, sticky=tk.E)
        unitOptions = ["in", "mm", "cm"]
        self.unitChosen = tk.StringVar()
        self.unitChosen.set(data['units'])
        unitDrop = tk.OptionMenu(units,
                                 self.unitChosen, *unitOptions)
        unitDrop.grid(row=0, column=1, sticky=tk.EW)
        units.grid(row=2, column=0, sticky=tk.EW)

    def report(self, _):
        w = self.widthEntry.get()
        h = self.heightEntry.get()
        d = self.depthEntry.get()
        print(f"{w}x{h}x{d}")