from tkinter import *       # GUI
from tkinter.ttk import *   # Widgets avec thèmes
from tkinter.scrolledtext import ScrolledText as tkst

class Fenetre(Tk):
    """ Mon programme graphique utilisant Python3 et Tkinter """
 
    def __init__(self):
        Tk.__init__(self)   # On dérive de Tk, on reprend sa méthode d'instanciation
 
        self.TxtRecherche = StringVar()
        self.TxtDossier1 = StringVar()
        self.TxtDossier2 = StringVar()
        self.TxtFichier1 = StringVar()
        self.TxtFichier2 = StringVar()
        self.TxtBase64 = StringVar()
        self.TxtBase64T = StringVar()
        self.TxtHtml = StringVar()
        self.TxtAdresse = StringVar()
        self.TxtTagHtml = StringVar()
        self.TxtRe = StringVar()
        self.TxtRechercheT = StringVar()
        
        self.countVar = StringVar()
        self.RechIndex = StringVar()

        self.geometry('800x640')
        self.title('Recherche dans dossier et/ou fichier')

        Frm1 = Frame(self)
        Frm1.pack(side=TOP, padx=0, pady=1)
        Frm2 = Frame(self)
        Frm2.pack(side=TOP, padx=5, pady=1, fill=X)
        Frm3 = Frame(self)
        Frm3.pack(side=TOP, padx=0, pady=1)
        Frm4 = Frame(self)
        Frm4.pack(side=TOP, padx=0, pady=1)
        Frm30 = Frame(self)
        Frm30.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm5 = Frame(self)
        Frm5.pack(side=BOTTOM, padx=1, pady=1, fill=BOTH, expand=Y)

        LblTitre = Label(Frm1, text="Choix de la recherche:", foreground="dark blue",justify=CENTER)
        LblTitre.config(font=("Courier", 15))
        LblTitre.pack(side=LEFT, padx=120, pady=0)

        self.nb = Notebook(Frm2)

        f1 = Frame(self.nb)
        self.nb.add(f1, text="Nom de fichier")

        Frm6 = Frame(f1)
        Frm6.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm7 = Frame(f1)
        Frm7.pack(side=TOP, padx=5, pady=1, fill=X)

        Lbl01 = Label(Frm6, text="Fichier Rechercher:", foreground="dark blue")
        Lbl01.pack(side=LEFT, padx=5, pady=0)
        self.cmbRecherche = Combobox(Frm6, textvariable=self.TxtRecherche)
        self.cmbRecherche.pack(side=LEFT, padx=2, pady=0, expand=Y, fill=X)
        Lbl02 = Label(Frm7, text="Dossier:", foreground="dark blue")
        Lbl02.pack(side=LEFT, padx=5, pady=0)
        self.cmbDossier1 = Combobox(Frm7, textvariable=self.TxtDossier1)
        self.cmbDossier1.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpDosSelect = Button(Frm7, text='...')
        self.BpDosSelect.pack(side=RIGHT, padx=0, pady=0)
        
        

        f2 = Frame(self.nb)
        self.nb.add(f2, text="Texte dans fichier")

        Frm8 = Frame(f2)
        Frm8.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm9 = Frame(f2)
        Frm9.pack(side=TOP, padx=5, pady=1, fill=X)

        Lbl03 = Label(Frm8, text="Texte Rechercher:", foreground="dark blue")
        Lbl03.pack(side=LEFT, padx=5, pady=0)
        self.cmbRecherche2 = Combobox(Frm8, textvariable=self.TxtRecherche)
        self.cmbRecherche2.pack(side=LEFT, padx=2, pady=0, expand=Y, fill=X)
        Lbl04 = Label(Frm9, text="Fichier:", foreground="dark blue")
        Lbl04.pack(side=LEFT, padx=5, pady=0)
        self.cmbFichier1 = Combobox(Frm9, textvariable=self.TxtFichier1)
        self.cmbFichier1.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpFichSelect = Button(Frm9, text='...')#, command=self.ChoixFichier)
        self.BpFichSelect.pack(side=RIGHT, padx=0, pady=0)


        f3 = Frame(self.nb)
        self.nb.add(f3, text="Texte dans dossier")

        Frm10 = Frame(f3)
        Frm10.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm11 = Frame(f3)
        Frm11.pack(side=TOP, padx=5, pady=1, fill=X)
        
        Frm100 = Frame(f3)
        Frm100.pack(side=TOP, padx=5, pady=1, fill=X)

        Lbl05 = Label(Frm10, text="Texte Rechercher:", foreground="dark blue")
        Lbl05.pack(side=LEFT, padx=5, pady=0)
        self.cmbRecherche4 = Combobox(Frm10, textvariable=self.TxtRecherche)
        self.cmbRecherche4.pack(side=LEFT, padx=2, pady=0, expand=Y, fill=X)
        
        Lbl06 = Label(Frm11, text="Dossier:", foreground="dark blue")
        Lbl06.pack(side=LEFT, padx=5, pady=0)
        self.cmbDossier2 = Combobox(Frm11, textvariable=self.TxtDossier1)
        self.cmbDossier2.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpDosSelect2 = Button(Frm11, text='...')#, command=self.ChoixDossier)
        self.BpDosSelect2.pack(side=RIGHT, padx=0, pady=0)

        self.test = StringVar()
        Lbl100 = Label(Frm100, text="Test:", foreground="dark blue")
        Lbl100.pack(side=LEFT, padx=5, pady=0)
        self.cmb100 = Combobox(Frm100, textvariable=self.test)
        self.cmb100.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpTest100 = Button(Frm100, text='test 100')#, command=self.ChoixDossier)
        self.BpTest100.pack(side=RIGHT, padx=0, pady=0)


        f4 = Frame(self.nb)
        self.nb.add(f4, text="Comparer dossier")

        Frm12 = Frame(f4)
        Frm12.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm13 = Frame(f4)
        Frm13.pack(side=TOP, padx=0, pady=1, fill=X)

        Lbl07 = Label(Frm12, text="Dossier 1:", foreground="dark blue")
        Lbl07.pack(side=LEFT, padx=5, pady=0)
        self.cmbDossier3 = Combobox(Frm12, textvariable=self.TxtDossier1)
        self.cmbDossier3.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpDosSelect3 = Button(Frm12, text='...')#, command=self.ChoixDossier)
        self.BpDosSelect3.pack(side=RIGHT, padx=0, pady=0)
        
        Lbl08 = Label(Frm13, text="Dossier 2:", foreground="dark blue")
        Lbl08.pack(side=LEFT, padx=5, pady=0)
        self.cmbDossier4 = Combobox(Frm13, textvariable=self.TxtDossier2)
        self.cmbDossier4.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpDosSelect4 = Button(Frm13, text='...')#, command=self.ChoixDossier2)
        self.BpDosSelect4.pack(side=RIGHT, padx=0, pady=0)

        f5 = Frame(self.nb)
        self.nb.add(f5, text="Comparer fichier")

        Frm14 = Frame(f5)
        Frm14.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm15 = Frame(f5)
        Frm15.pack(side=TOP, padx=0, pady=1, fill=X)

        Lbl09 = Label(Frm14, text="Fichier 1:", foreground="dark blue")
        Lbl09.pack(side=LEFT, padx=5, pady=0)
        self.cmbFichier2 = Combobox(Frm14, textvariable=self.TxtFichier1)
        self.cmbFichier2.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpFichSelect2 = Button(Frm14, text='...')#, command=self.ChoixFichier)
        self.BpFichSelect2.pack(side=RIGHT, padx=0, pady=0)
        
        Lbl08 = Label(Frm15, text="Fichier 2:", foreground="dark blue")
        Lbl08.pack(side=LEFT, padx=5, pady=0)
        self.cmbFichier3 = Combobox(Frm15, textvariable=self.TxtFichier2)
        self.cmbFichier3.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpFichSelect5 = Button(Frm15, text='...')#, command=self.ChoixFichier2)
        self.BpFichSelect5.pack(side=RIGHT, padx=0, pady=0)

        f6 = Frame(self.nb)
        self.nb.add(f6, text="Convertion")

        Frm16 = Frame(f6)
        Frm16.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm17 = Frame(f6)
        Frm17.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm18 = Frame(f6)
        Frm18.pack(side=TOP, padx=0, pady=1, fill=X)

        Lbl10 = Label(Frm16, text="Base64->Text:", foreground="dark blue")
        Lbl10.pack(side=LEFT, padx=5, pady=0)
        self.cmbBase64 = Combobox(Frm16, textvariable=self.TxtBase64)
        self.cmbBase64.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpConv1 = Button(Frm16, text='Convertion')#, command=self.ConvertBase64)
        self.BpConv1.pack(side=RIGHT, padx=0, pady=0)
        
        Lbl11 = Label(Frm17, text="Text->Base64:", foreground="dark blue")
        Lbl11.pack(side=LEFT, padx=5, pady=0)
        self.cmbBase64T = Combobox(Frm17, textvariable=self.TxtBase64T)
        self.cmbBase64T.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpConv2 = Button(Frm17, text='Convertion')#, command=self.ConvertBaseTxt)
        self.BpConv2.pack(side=RIGHT, padx=0, pady=0)
        
        Lbl12 = Label(Frm18, text="Adresse%->http:", foreground="dark blue")
        Lbl12.pack(side=LEFT, padx=5, pady=0)
        self.cmbHtml = Combobox(Frm18, textvariable=self.TxtHtml)
        self.cmbHtml.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpConv3 = Button(Frm18, text='Convertion')#, command=self.ConvertHtml)
        self.BpConv3.pack(side=RIGHT, padx=0, pady=0)
        
        f7 = Frame(self.nb)
        self.nb.add(f7, text="Télécharg")

        Frm19 = Frame(f7)
        Frm19.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm20 = Frame(f7)
        Frm20.pack(side=TOP, padx=0, pady=1, fill=X)
        Frm21 = Frame(f7)
        Frm21.pack(side=TOP, padx=0, pady=1, fill=X)

        Lbl13 = Label(Frm19, text="Adresse:", foreground="dark blue")
        Lbl13.pack(side=LEFT, padx=5, pady=0)
        self.cmbAdresse = Combobox(Frm19, textvariable=self.TxtAdresse)
        self.cmbAdresse.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        #self.BpDl1 = Button(Frm19, text='Afficher')#, command=self.AffichDl)
        #self.BpDl1.pack(side=RIGHT, padx=0, pady=0)

        Lbl14 = Label(Frm20, text="Tag HTML", foreground="dark blue")
        Lbl14.pack(side=LEFT, padx=5, pady=0)
        self.cmbTagHtml = Combobox(Frm20, textvariable=self.TxtTagHtml)
        self.cmbTagHtml.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)

        Lbl15 = Label(Frm21, text="Commande Re:", foreground="dark blue")
        Lbl15.pack(side=LEFT, padx=5, pady=0)
        self.cmbRe = Combobox(Frm21, textvariable=self.TxtRe)
        self.cmbRe.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpDl2 = Button(Frm21, text='Résultat')#, command=self.RechercheRE)
        self.BpDl2.pack(side=RIGHT, padx=0, pady=0)
        
        self.nb.select(f3)

        self.nb.enable_traversal()
        
        self.nb.pack(side=TOP, padx=0, pady=1,fill=X)
        
        self.rechercher = Button(Frm3, text='Rechercher')#, command=self.Recherche)
        self.rechercher.grid(row=0, column=0, sticky=NSEW)
        self.StopRech = Button(Frm3, text='Stop\nRechercher')#, command=self.Stop)
        self.EffaceTxt = Button(Frm3, text='Effacer Résultat')#, command=self.EffaceResult)
        self.EffaceTxt.grid(row=0, column=2, columnspan=3,sticky=W)
        self.quitter = Button(Frm3, text='Quitter')#, command=self.Quitter)
        self.quitter.grid(row=0, column=5, columnspan=3,sticky=E)

        Lbl04 = Label(Frm4, text="Résultat Recherche:", foreground="dark blue")
        Lbl04.config(font=("Courier", 15))
        Lbl04.pack(side=LEFT, padx=10, pady=0)

        Lbl20 = Label(Frm30, text="Recherche dans\nles Résultats:", foreground="dark blue")
        Lbl20.pack(side=LEFT, padx=10, pady=0)
        self.cmbRechercheT = Combobox(Frm30, textvariable=self.TxtRechercheT)
        self.cmbRechercheT.pack(side=LEFT, padx=5, pady=0, expand=Y, fill=X)
        self.BpRechTsuiv = Button(Frm30, text='Suivant')#, command=self.RechercheTxt)
        #self.BpRechTsuiv.pack(side=RIGHT, padx=0, pady=0)
        self.BpResulTcopi = Button(Frm30, text='Copier\nSélection')#, command=self.RechercheTxt)
        self.BpResulTcopi.pack(side=RIGHT, padx=0, pady=0)
        self.BpRechTResult = Button(Frm30, text='Recherche\ntext...')#, command=self.RechercheTxt)
        self.BpRechTResult.pack(side=RIGHT, padx=0, pady=0)
        self.BpRechTpres = Button(Frm30, text='Précédent')#, command=self.RechercheTxt)
        #self.BpRechTpres.pack(side=RIGHT, padx=0, pady=0)
        e21 = Label(Frm30, textvariable=self.countVar, foreground="dark red")
        e21.pack(side=RIGHT, padx=10, pady=0)
        #Lbl21 = Label(Frm30, text="Nb Résult:", foreground="dark blue")
        #Lbl21.pack(side=RIGHT, padx=10, pady=0)

        self.t = tkst(Frm5, height=20, width=40)
        self.t.pack(side=LEFT, padx=0, pady=0, expand=Y, fill=BOTH)
        """scrollb = Scrollbar(Frm5, command=self.t.yview)
        scrollb.pack(side=RIGHT, padx=0, pady=0, fill=BOTH)
        self.t['yscrollcommand'] = scrollb.set"""

        self.MnuEdit = Menu(self, tearoff=0)
