import tkinter as tk
from tkinter import messagebox
import random
import string

# --- LISTA DE CUVINTE CU INDICII (fara diacritice) ---
cuvinte_usoare = [
    ("voltmetru", "Instrument pentru masurarea tensiunii electrice dintre doua puncte"),
    ("ampermetru", "Instrument pentru masurarea intensitatii curentului electric"),
    ("baterie", "Sursa de energie chimica transformata in energie electrica"),
    ("senzor", "Dispozitiv care detecteaza un fenomen fizic sau chimic si il transforma intr-un semnal"),
    ("dioda", "Componenta electronica care permite trecerea curentului intr-o singura directie"),
    ("semnal", "Variatie a unei marimi fizice care transmite informatii"),
    ("capacitate", "Masoara capacitatea unui condensator de a stoca sarcina electrica"),
    ("retea", "Ansamblu de componente interconectate pentru a transporta energie sau semnale"),
    ("gradient", "Variatia unei marimi in functie de pozitie"),
    ("foton", "Cuanta de energie a luminii sau a radiatiei electromagnetice"),
    ("parametru", "Marime care caracterizeaza un sistem sau un fenomen"),
    ("inductanta", "Proprietatea unui conductor de a se opune schimbarii curentului"),
    ("camp magnetic", "Regiune in care actioneaza forta magnetica"),
    ("camp electric", "Regiune in care actioneaza forta electrica"),
    ("legea lui Ohm", "Relatia dintre tensiune, curent si rezistenta intr-un conductor"),
    ("legea lui Faraday", "Lege care defineste tensiunea indusa prin variatia fluxului magnetic"),
    ("curent de dispersie", "Curent care apare prin imperfectiuni ale unui material"),
    ("curent continuu", "Curent electric care circula intotdeauna in aceeasi directie"),
    ("curent alternativ", "Curent electric care isi schimba periodic sensul"),
    ("tensiune de alimentare", "Tensiunea furnizata unui circuit pentru a functiona"),
    ("divizor de tensiune", "Circuit care imparte tensiunea in parti proportionale"),
    ("scurtcircuit", "Legatura directa intre doua puncte ale unui circuit cu rezistenta foarte mica"),
    ("comutator", "Dispozitiv care intrerupe sau inchide un circuit electric")
]

cuvinte_dificile = [
    ("condensator", "Componenta care stocheaza energie electrica in camp electric"),
    ("inductanta", "Proprietatea unui conductor de a se opune schimbarii curentului"),
    ("transistor", "Dispozitiv semiconductor utilizat ca amplificator sau comutator"),
    ("semiconductor", "Material a carui conductivitate este intre conductor si izolator"),
    ("amplificator", "Dispozitiv care mareste amplitudinea semnalelor electrice"),
    ("osciloscop", "Instrument pentru vizualizarea si masurarea semnalelor electrice variabile"),
    ("rezistivitate", "Masoara cat de mult opune un material trecerii curentului electric"),
    ("inductivitate", "Masoara capacitatea unui circuit de a induce tensiune prin schimbarea curentului"),
    ("capacitate", "Masoara cantitatea de sarcina pe care o poate stoca un condensator"),
    ("filtrare", "Proces de eliminare a componentelor nedorite dintr-un semnal"),
    ("termistor", "Rezistor a carui rezistenta variaza semnificativ cu temperatura"),
    ("amplificatoare", "Dispozitive care amplifica semnale electrice"),
    ("voltmetru", "Instrument pentru masurarea tensiunii electrice dintre doua puncte"),
    ("ampermetru", "Instrument pentru masurarea intensitatii curentului electric"),
    ("inductoare", "Componente care stocheaza energie in camp magnetic"),
    ("transformatoare", "Dispozitive care modifica tensiunea curentului alternativ"),
    ("microprocesoare", "Circuit integrat complex care executa instructiuni si calculeaza date"),
    ("entropie", "Marime care masoara gradul de dezordine sau aleatorietate a unui sistem"),
    ("impedanta", "Rezistenta efectiva a unui circuit la curent alternativ"),
    ("admitanta", "Măsura ușurinței cu care curentul alternativ trece printr-un circuit"),
    ("frecventa de rezonanta", "Frecventa la care un sistem oscileaza natural cu amplitudine maxima"),
    ("transformare Laplace", "Transformare matematica utilizata pentru rezolvarea ecuatiilor diferentiale"),
    ("factor de amortizare", "Masoara reducerea amplitudinii oscilatiilor intr-un sistem"),
    ("amplificator de semnal", "Amplifica un semnal electric fara a-i schimba forma"),
    ("impedanta de intrare", "Rezistenta unui circuit la intrarea semnalului"),
    ("impedanta de iesire", "Rezistenta unui circuit la iesirea semnalului"),
    ("transformator de putere", "Transformator utilizat pentru transferul de energie intre circuite"),
    ("amplificator de curent", "Amplifica intensitatea curentului electric")
]

class Spanzuratoare:
    def __init__(self, master):
        self.master = master
        master.title("Spanzuratoarea pentru politehnisti")

        self.nivel = None
        self.cuvant_secret = ""
        self.indiciu = ""
        self.litere_gasite = []
        self.litere_folosite = []
        self.greseli = 0
        self.max_greseli = 6
        self.scor = 0
        self.indiciu_folosit = False
        self.litera_bonus_folosita = False

        # Componentele grafice
        self.canvas = tk.Canvas(master, width=300, height=300)
        self.canvas.pack()

        self.nivel_label = tk.Label(master, text="", font=("Arial", 12), anchor="e")
        self.nivel_label.place(x=250, y=5)  # Dreapta sus

        self.cuvant_label = tk.Label(master, text="", font=("Arial", 24))
        self.cuvant_label.pack(pady=10)

        self.greseli_label = tk.Label(master, text="", font=("Arial", 14))
        self.greseli_label.pack()

        self.folosite_label = tk.Label(master, text="", font=("Arial", 12))
        self.folosite_label.pack(pady=5)

        self.scor_label = tk.Label(master, text="Scor: 0", font=("Arial", 14))
        self.scor_label.pack(pady=5)

        # Frame pentru litere
        self.litere_frame = tk.Frame(master)
        self.litere_frame.pack(pady=10)

        # Frame pentru dificultate
        self.dificultate_frame = tk.Frame(master)
        self.dificultate_frame.pack(pady=10)

        tk.Label(self.dificultate_frame, text="Alege dificultatea:").pack(side=tk.LEFT)
        self.usor_btn = tk.Button(self.dificultate_frame, text="Usor", command=lambda: self.start_joc("usor"))
        self.usor_btn.pack(side=tk.LEFT, padx=5)
        self.dificil_btn = tk.Button(self.dificultate_frame, text="Dificil", command=lambda: self.start_joc("dificil"))
        self.dificil_btn.pack(side=tk.LEFT, padx=5)

        # Butoane indiciu si bonus (initial invizibile)
        self.indiciu_btn = tk.Button(master, text="Cere un indiciu", command=self.arata_indiciu, state=tk.DISABLED)
        self.indiciu_btn.pack(pady=5)
        self.litera_bonus_btn = tk.Button(master, text="Foloseste 3 puncte pentru o litera", command=self.litera_bonus, state=tk.DISABLED)
        self.litera_bonus_btn.pack(pady=5)

    def start_joc(self, nivel):
        # Blocam alegerea dificultatii
        self.usor_btn.config(state=tk.DISABLED)
        self.dificil_btn.config(state=tk.DISABLED)

        self.nivel = nivel
        self.nivel_label.config(text=f"Nivel: {nivel.capitalize()}")
        self.litere_folosite = []
        self.greseli = 0
        self.indiciu_folosit = False
        self.litera_bonus_folosita = False

        # Alegerea cuvantului
        if nivel == "usor":
            self.cuvant_secret, self.indiciu = random.choice(cuvinte_usor)
        else:
            self.cuvant_secret, self.indiciu = random.choice(cuvinte_dificil)

        self.litere_gasite = [l if not l.isalpha() else "_" for l in self.cuvant_secret]

        # Activam butoanele abia dupa alegerea dificultatii
        self.indiciu_btn.config(state=tk.NORMAL)
        self.litera_bonus_btn.config(state=tk.NORMAL)

        self.update_litere_buttons()
        self.update_display()
        self.deseneaza_spanzuratoare()

    def update_litere_buttons(self):
        for widget in self.litere_frame.winfo_children():
            widget.destroy()
        for idx, litera in enumerate(string.ascii_lowercase):
            btn = tk.Button(self.litere_frame, text=litera.upper(), width=4,
                            command=lambda l=litera: self.verifica_litera(l))
            btn.grid(row=idx//9, column=idx%9, padx=2, pady=2)

    def verifica_litera(self, litera):
        if litera in self.litere_folosite:
            return
        self.litere_folosite.append(litera)

        if litera in self.cuvant_secret:
            for idx, l in enumerate(self.cuvant_secret):
                if l == litera:
                    self.litere_gasite[idx] = litera
                    self.scor += 1  # 1 punct per litera ghicita
        else:
            self.greseli += 1

        self.update_display()
        self.deseneaza_spanzuratoare()
        self.check_game_over()

    def update_display(self):
        self.cuvant_label.config(text=" ".join(self.litere_gasite))
        self.greseli_label.config(text=f"Greseli: {self.greseli}/{self.max_greseli}")
        self.folosite_label.config(text="Litere folosite: " + ", ".join(self.litere_folosite))
        self.scor_label.config(text=f"Scor: {self.scor}")

    def arata_indiciu(self):
        ghicite = sum(1 for l1, l2 in zip(self.litere_gasite, self.cuvant_secret) if l1 == l2 and l1 != "_")
        if ghicite >= 3:
            self.indiciu_folosit = True
            messagebox.showinfo("Indiciu", self.indiciu)
        else:
            messagebox.showinfo("Indiciu", "Trebuie sa ghicesti cel putin 3 litere pentru a cere indiciu!")

    def litera_bonus(self):
        if self.scor >= 3:
            for idx, l in enumerate(self.litere_gasite):
                if l == "_":
                    self.litere_gasite[idx] = self.cuvant_secret[idx]
                    self.scor -= 3
                    self.litera_bonus_folosita = True
                    break
            self.update_display()
            self.check_game_over()
        else:
            messagebox.showinfo("Litera bonus", "Nu ai suficiente puncte (3 puncte necesare)")

    def check_game_over(self):
        if "_" not in self.litere_gasite:
            # Punctaj final dupa dificultate
            if self.nivel == "usor":
                self.scor += 3
            else:
                self.scor += 5
            # Bonus pentru utilizarea minima a indiciului / literelor bonus
            if not self.indiciu_folosit:
                self.scor += 2
            if not self.litera_bonus_folosita:
                self.scor += 2

            msg = f"Ai ghicit cuvantul: {self.cuvant_secret}\nScor curent: {self.scor}\nVrei sa continui jocul?"
            if messagebox.askyesno("Felicitari!", msg):
                self.start_joc(self.nivel)
            else:
                self.master.destroy()
        elif self.greseli >= self.max_greseli:
            messagebox.showinfo("Game Over", f"Ai pierdut! Cuvantul era: {self.cuvant_secret}\nScor final: {self.scor}")
            self.master.destroy()

    def deseneaza_spanzuratoare(self):
        self.canvas.delete("all")
        self.canvas.create_line(50, 250, 200, 250, width=2)
        self.canvas.create_line(125, 250, 125, 50, width=2)
        self.canvas.create_line(125, 50, 200, 50, width=2)
        self.canvas.create_line(200, 50, 200, 70, width=2)

        if self.greseli >= 1:
            self.canvas.create_oval(180, 70, 220, 110, width=2)
        if self.greseli >= 2:
            self.canvas.create_line(200, 110, 200, 170, width=2)
        if self.greseli >= 3:
            self.canvas.create_line(200, 120, 170, 150, width=2)
        if self.greseli >= 4:
            self.canvas.create_line(200, 120, 230, 150, width=2)
        if self.greseli >= 5:
            self.canvas.create_line(200, 170, 170, 200, width=2)
        if self.greseli >= 6:
            self.canvas.create_line(200, 170, 230, 200, width=2)

root = tk.Tk()
joc = Spanzuratoare(root)
root.mainloop()
