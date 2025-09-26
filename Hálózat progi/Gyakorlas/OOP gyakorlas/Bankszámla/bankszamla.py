import tkinter as tk
from tkinter import Frame, messagebox

class Bankszámla:
    def __init__(self,nev,egyenleg):
        self.nev = nev
        self.egyenleg = egyenleg

    def befizetes(self,osszeg):
        if osszeg > 0:
            self.egyenleg += osszeg
            return True
        else:
            return False
    
    def kivetel(self,osszeg):
        if osszeg > 0 and self.egyenleg >= osszeg:
            self.egyenleg -= osszeg
            return True
        else:
            return False
    
    def egyenleg_lekerdezes(self):
        return f"Jelenleg ennyi forint van a számládon: {self.egyenleg} Ft"




def perform_befizetes(amount):
    if szamla1.befizetes(amount):
        egyenleg_label.config(text=szamla1.egyenleg_lekerdezes())


def perform_kivetel(amount):
    if szamla1.kivetel(amount):
        egyenleg_label.config(text=szamla1.egyenleg_lekerdezes())
    else:
        messagebox.showwarning(title="Hiba", message="Elfogyott a pénzed :)")
    



def show_main_frame():
    befizetes_frame.pack_forget()
    main_frame.pack()
    kivetel_frame.pack_forget()

def show_befizetes_frame():
    main_frame.pack_forget()
    befizetes_frame.pack()
    kivetel_frame.pack_forget()

def show_kivetel_frame():
    main_frame.pack_forget()
    befizetes_frame.pack_forget()
    kivetel_frame.pack()


# GUI
app = tk.Tk()
app.title("Halászos Bank") # Ablak neve
app.geometry("800x600") # Ablak mérete
szamla1 = Bankszámla('Halász István',50000)

main_frame = tk.Frame(app)


# Egyenleg label
egyenleg_text = szamla1.egyenleg_lekerdezes() # Eltárolom egy változóba a számla adatait
egyenleg_label = tk.Label(app, text=egyenleg_text, font=("Poppins", 16)) # Maga a label-be belehelyezem az eltárolt adatot
egyenleg_label.pack(pady=20) # Eligazítom az ablakon belül



# Pénzbefizetés gombok
befizetes_frame = tk.Frame(app)

befizetes_button = tk.Button(main_frame, text="Befizetés", command=show_befizetes_frame)
befizetes_button.pack(pady=20)

befizetes_5000_button = tk.Button(befizetes_frame, text="5 000 Ft", command=lambda:perform_befizetes(5000), font=("Poppins", 10))
befizetes_5000_button.pack(pady=20)

befizetes_10000_button = tk.Button(befizetes_frame, text="10 000 Ft", command=lambda:perform_befizetes(10000), font=("Poppins", 10))
befizetes_10000_button.pack(pady=20)

befizetes_20000_button = tk.Button(befizetes_frame, text="20 000 Ft", command=lambda:perform_befizetes(20000), font=("Poppins", 10))
befizetes_20000_button.pack(pady=20)





# Pénzkivétel gombok
kivetel_frame = tk.Frame(app)

kivetel_button = tk.Button(main_frame, text="Kivétel", command=show_kivetel_frame)
kivetel_button.pack(fill=tk.X,pady=20)


kivetel_5000_button = tk.Button(kivetel_frame, text="5 000 Ft", command=lambda:perform_kivetel(5000), font=("Poppins", 10))
kivetel_5000_button.pack(pady=20)

kivetel_10000_button = tk.Button(kivetel_frame, text="10 000 Ft", command=lambda:perform_kivetel(10000), font=("Poppins", 10))
kivetel_10000_button.pack(pady=20)

kivetel_20000_button = tk.Button(kivetel_frame, text="20 000 Ft", command=lambda:perform_kivetel(20000), font=("Poppins", 10))
kivetel_20000_button.pack(pady=20)



# Vissza gomb
back_button = tk.Button(befizetes_frame, text="Vissza", command=show_main_frame, font=("Poppins", 10))
back_button.pack(pady=20)

back_button = tk.Button(kivetel_frame, text="Vissza", command=show_main_frame, font=("Poppins", 10))
back_button.pack(pady=20)


show_main_frame() # Ez mutatja a főablakot
app.mainloop() # Ez tartja megnyitva az ablakot

