# -*- coding:iso-8859-15 -*-
from ExploreUI import Fenetre
import os,sys #, time
from stat import *
from tkinter import filedialog
from base64 import b64decode, b64encode
#import urllib
import urllib.request
try:
    import bs4
except:
    bs4 = None
import json
import re
import platform
#from tkinter.scrolledtext import ScrolledText
from threading import Thread
from time import sleep
import marshal
from PIL import Image
#import vlc
import mimetypes
import string

try:
    Enum = dict(marshal.load(open("EnumExplorFich.dat", 'rb')))
except:
    Enum= dict({"CmbRecherche":[],
               "CmbDossier":[],
               "CmbFichier":[],
               "CmbBase64":[],
               "CmbBase64T":[],
               "CmbHtml":[],
               "CmbAdresse":[],
               "CmbTagHtml":[],
               "CmbRe":[],
               "CmbRechercheT":[]})

class App():
    """ Mon programme graphique utilisant Python3 et Tkinter """
 
    def __init__(self):
        self.UI = Fenetre()        
        self.UI.BpDosSelect.config(command=self.ChoixDossier)
        self.UI.BpFichSelect.config(command=self.ChoixFichier)
        self.UI.BpDosSelect2.config(command=self.ChoixDossier)
        self.UI.BpDosSelect3.config(command=self.ChoixDossier)
        self.UI.BpDosSelect4.config(command=self.ChoixDossier2)
        self.UI.BpFichSelect2.config(command=self.ChoixFichier)
        self.UI.BpFichSelect5.config(command=self.ChoixFichier2)
        self.UI.BpConv1.config(command=self.ConvertBase64)
        self.UI.BpConv2.config(command=self.ConvertBaseTxt)
        self.UI.BpConv3.config(command=self.ConvertHtml)
        #self.UI.BpDl1.config(command=self.AffichDl)
        self.UI.rechercher.config(command=self.Play)
        self.UI.StopRech.config(command=self.Stop)
        self.UI.EffaceTxt.config(command=self.EffaceResult)
        self.UI.quitter.config(command=self.Quitter)
        self.UI.BpDl2.config(command=self.RechercheRE)
        self.UI.BpRechTResult.config(command=self.RechercheTxt)
        self.UI.BpRechTpres.config(command=self.TxtRechPrec)
        self.UI.BpRechTsuiv.config(command=self.TxtRechSuiv)
        self.UI.BpResulTcopi.config(command=self.copier)
        self.UI.BpRechTpres.pack_forget()
        self.UI.BpRechTsuiv.pack_forget()
        self.UI.MnuEdit.add_command(label="Copier", command=self.copier)
        # attach popup to canvas
        self.UI.t.bind("<Button-3>", self.popup)
        self.UI.t.bind("<Control-Key-a>", self.select_all)
        self.UI.t.bind("<Control-Key-c>", self.copier)
        print(platform.system())
        print(platform.system_alias(platform.system(),platform.release(),platform.version()))

        self.text_characters = "".join(map(chr, range(32, 127)))
        self.text_characters += "\n\r\t\b"
        self._null_trans = str.maketrans("", "")
        VarOs = os.environ
        self.DefRep = ""
        if platform.system()=='Linux':
            try:
                self.DefRep = VarOs['HOME']
            except:
                self.DefRep = "/"
        elif platform.system()=='Windows':
            try:
                self.DefRep = self.VarOs['USERPROFILE']
            except:
                pass
        if self.DefRep == "" or self.DefRep == "/":
            self.UI.t.insert("end",
                             str(platform.system_alias(platform.system(),
                                                       platform.release(),
                                                       platform.version()))+"\n"+
                             str(VarOs))
        self.LidxId = 0
        self.count = 0
        self.UI.RechIndex.set("1.0")
        self.UI.countVar.set("0/0")
        self._thread, self._pause, self._stop = None, False, True
        global Enum
        self.InitCmb()
        
        self.UI.BpTest100.config(command=self.Test)
        self.UI.mainloop()

    def Test(self):
        nouvRech = self.UI.test.get()
        if nouvRech:
            self.SauvTxtRech(nouvRech,"CmbAdresse")
        """nouvRech = self.UI.test.get()
        if nouvRech:
            if len(CmbAdresse)<50:
                if CmbAdresse.count(nouvRech)>0:
                    CmbAdresse.remove(nouvRech)
            else:
                CmbAdresse.pop(0)
            CmbAdresse.append(self.UI.test.get())
            self.UI.cmb100['values'] = list(reversed(CmbAdresse))"""
            
    def SauvTxtRech(self,str,liste):
        list = Enum[liste]
        if str:
            if len(list)<30:
                if list.count(str)>0:
                    list.remove(str)
            else:
                list.pop(0)
            list.append(str)
            Enum[liste]=list
            self.InitCmb()
            
    def InitCmb(self):
        self.UI.cmbRecherche['values'] = list(reversed(Enum["CmbRecherche"]))
        self.UI.cmbDossier1['values'] = list(reversed(Enum["CmbDossier"]))
        self.UI.cmbRecherche2['values'] = list(reversed(Enum["CmbRecherche"]))
        self.UI.cmbFichier1['values'] = list(reversed(Enum["CmbFichier"]))
        self.UI.cmbRecherche4['values'] = list(reversed(Enum["CmbRecherche"]))
        self.UI.cmbDossier2['values'] = list(reversed(Enum["CmbDossier"]))
        self.UI.cmb100['values'] = list(reversed(Enum["CmbAdresse"]))
        self.UI.cmbDossier3['values'] = list(reversed(Enum["CmbDossier"]))
        self.UI.cmbDossier4['values'] = list(reversed(Enum["CmbDossier"]))
        self.UI.cmbFichier2['values'] = list(reversed(Enum["CmbFichier"]))
        self.UI.cmbFichier3['values'] = list(reversed(Enum["CmbFichier"]))
        self.UI.cmbBase64['values'] = list(reversed(Enum["CmbBase64"]))
        self.UI.cmbBase64T['values'] = list(reversed(Enum["CmbBase64T"]))
        self.UI.cmbHtml['values'] = list(reversed(Enum["CmbHtml"]))
        self.UI.cmbAdresse['values'] = list(reversed(Enum["CmbAdresse"]))
        self.UI.cmbTagHtml['values'] = list(reversed(Enum["CmbTagHtml"]))
        self.UI.cmbRe['values'] = list(reversed(Enum["CmbRe"]))
        self.UI.cmbRechercheT['values'] = list(reversed(Enum["CmbRechercheT"]))

    def Play(self):
        if self._thread is None:
            self._stop = False
            self._thread = Thread(target=self.Recherche)
            self._thread.start()
        self._pause = False
        self.UI.rechercher.configure(text="Pause\nRecherche", command=self.pause)
        self.UI.StopRech.grid(row=0, column=1,sticky='w')
 
    def pause(self):
        self._pause = True
        self.UI.rechercher.configure(text="Reprendre\nRechercher", command=self.Play)
 
    def Stop(self):
        if self._thread is not None:
            self._thread, self._pause, self._stop = None, False, True
        self.UI.rechercher.configure(text="Recherche", command=self.Play)
        self.UI.StopRech.grid_forget()

    def popup(self, event):
        print(event)
        self.UI.MnuEdit.post(event.x_root, event.y_root)
        
    def copier(self, event=None):
        texte=self.UI.t.selection_get()
        try:
            self.UI.clipboard_clear() 
            self.UI.clipboard_append(texte)
            #self.UI.withdraw() 
            print ('-'*60)
            print ('Texte copier dans le presse-papier avec succés (via Tkinter).')
            print ('-'*60) 
        except:
            try: 
                import sys 
                from PyQt4 import QtGui, QtCore 
                app = QtGui.QApplication(sys.argv) 
                clipboard = app.clipboard() 
                clipboard.setText('') 
                event = QtCore.QEvent(QtCore.QEvent.Clipboard) 
                app.sendEvent(clipboard, event) 
                print ('-'*60)
                print ('Texte copier dans le presse-papier avec succés (via Pyqt4).')
                print ('-'*60)
            except: 
                print ('Copier puis coller le texte ci-dessous :')
                print ('')
                print (texte)

    def select_all(self, event=None):
        print(str(event))
        self.UI.t.tag_add("sel", "1.0", "end-1c")
        self.UI.t.mark_set("insert", "1.end")
        self.UI.t.see("insert")
        return "break"

    def RechercheRE(self):
        try:
            nouvRech=self.UI.TxtAdresse.get()
            nouvRech2=self.UI.TxtRe.get()
            self.SauvTxtRech(nouvRech,"CmbAdresse")
            self.SauvTxtRech(nouvRech2,"CmbRe")
            with urllib.request.urlopen(nouvRech) as Dl:
                #'<li class=" hd">.+?href="([^"]+)">.+?<script.+?([^;]+);</script>.+?src="([^"]+)".+?<i class="fa fa-clock-o"></i>([^<]+)</span>(.+?)</figcaption>.+?</li>'
                match1 = re.compile(str(self.UI.TxtRe.get()),re.DOTALL | re.IGNORECASE).findall(str(Dl.read()))
                self.UI.t.insert("end", "\n******Re comande pour l'adresse : " + str(nouvRech) + "\n")
                self.UI.t.insert("end", "\n******Re comande = " + str(nouvRech2) + "\n")
                for rep in match1:
                    self.UI.t.insert("end", str(rep) + "\n")
        except Exception as err:
            self.UI.t.insert("end", "*******\n   Erreur de Recherche: \n     "+ str(err) + "\n*******\n")

    def RechercheTxt(self):
        try:
            for i in range(1,self.count+1):
                self.UI.t.tag_remove('Rech'+str(i), '1.0', "end")

            s = self.UI.TxtRechercheT.get()
            self.SauvTxtRech(s,"CmbRechercheT")
            self.count = 0
            self.LidxId = 0
            self.UI.countVar.set(str(self.count))
            prums = False
            if s:
                idx = '1.0'
                while 1:
                    idx = self.UI.t.search(s, idx, stopindex="end") # nocase=1,
                    if not idx: break
                    
                    self.count+=1
                    self.UI.countVar.set("1/"+str(self.count))
                    lastidx = '%s+%dc' % (idx, len(s))
                    self.UI.t.tag_add('Rech'+str(self.count), idx, lastidx)
                    if not prums:
                        self.UI.t.tag_config('Rech'+str(self.count), foreground='yellow',background='red')
                        self.UI.t.see(idx)
                        prums = True
                    else:
                        self.UI.t.tag_config('Rech'+str(self.count), foreground='red',background='yellow')
                    idx = lastidx
            if self.count>1:
                self.UI.BpRechTpres.pack()
                self.UI.BpRechTsuiv.pack()
            else:
                self.UI.BpRechTpres.pack_forget()
                self.UI.BpRechTsuiv.pack_forget()
            #edit.focus_set()
            #pos = self.UI.t.search(self.UI.TxtRechercheT.get(), self.UI.RechIndex.get(), stopindex="end", count=self.UI.countVar)
            #print("******* "+str(pos))
            #print(self.UI.countVar.get())
            
            #self.UI.t.index(pos)
            #self.UI.t.tag_add(self.UI.TxtRechercheT.get(), pos, "%s + %sc" (pos, self.UI.countVar.get()))
        except Exception as err:
            self.UI.t.insert("end", "*******\n   Erreur de recherche: \n     "+ str(err) + "\n*******\n")
            
    def TxtRechSuiv(self):
        self.UI.t.tag_config('Rech'+str(self.LidxId+1), foreground='red',background='yellow')
        if self.LidxId<self.count-1:
            self.LidxId +=1
        else:
            self.LidxId = 0
        self.UI.t.see(self.UI.t.tag_ranges('Rech'+str(self.LidxId+1))[1])
        self.UI.countVar.set(str(self.LidxId+1)+"/"+str(self.count))
        self.UI.t.tag_config('Rech'+str(self.LidxId+1), foreground='yellow',background='red')

    def TxtRechPrec(self):
        self.UI.t.tag_config('Rech'+str(self.LidxId+1), foreground='red',background='yellow')
        if self.LidxId>0:
            self.LidxId -=1
        else:
            self.LidxId = self.count-1
        self.UI.t.see(self.UI.t.tag_ranges('Rech'+str(self.LidxId+1))[1])
        self.UI.countVar.set(str(self.LidxId+1)+"/"+str(self.count))
        self.UI.t.tag_config('Rech'+str(self.LidxId+1), foreground='yellow',background='red')
            

    def AffichDl(self):
        try:
            self.SauvTxtRech(self.UI.TxtAdresse.get(),"CmbAdresse")
            with urllib.request.urlopen(self.UI.TxtAdresse.get()) as Dl:
                xinf = Dl.info()
                print(xinf)
                #Content-Type: text/html; charset=UTF-8
                Ext = str(xinf).split("Content-Type: ")[1].split("\n")[0]
                Ext = Ext.replace("/","(*.")+")"
                self.UI.t.insert("end", "*******Type de fichier a Telecharger: \n   "+ Ext + "\n")
                if Ext[:4]=="text":
                    if Ext[7:11]=="html":
                        if bs4:
                            soup = bs4.BeautifulSoup(Dl.read(),features="html.parser")
                            #self.UI.t.insert("end", str(dir(soup)) + "\n")
                            Tag = self.UI.TxtTagHtml.get()
                            self.SauvTxtRech(Tag,"CmbTagHtml")
                            if not Tag:
                                self.UI.t.insert("end", str(soup) + "\n")
                            else:
                                for a in soup.find_all(Tag):
                                    self.UI.t.insert("end", str(a) + "\n")
                        else:
                            self.UI.t.insert("end", str(Dl.read()) + "\n")
                    elif Ext[5:9]=="json":
                        rawjson = Dl.read() #.decode('UTF-8')
                        parsedjson = json.loads(rawjson)
                        self.UI.t.insert("end", str(parsedjson) + "\n")
                    else:
                        print(Ext)
                else:
                    self.UI.t.insert("end", Ext + "\n")
                    print(Ext)
                """with open(self.dest, 'wb') as vid:
                    print("Ecriture de : "+self.dest)
                    i = 0
                    for i in range(0, self.longeur, Longeur):
                        sleep(0.01)
                        vid.write(Dl.read(Longeur))
                        pourcentage = ((i*100)/self.longeur)
                        self.progduthread.emit(pourcentage)
                    if self.longeur < i:
                        vid.write(video.read(self.longeur-i))
                    self.progduthread.emit(100)
                    # signale que le thread est terminï¿œ
                    print("00000000")
                    self.finduthread.emit("Fin du tï¿œlï¿œchargement")
                    print("00000001")
                    sleep(2)"""
        except Exception as err:
            self.UI.t.insert("end", "*******Erreur de tï¿œlï¿œchargement: \n   "+ str(err) + "\n*******\n")
        """try:
            import json
            from datetime import datetime
            if not Nasa:
                with urllib.request.urlopen(self.BINGURL + self.JSONURL) as response:
                    rawjson = response.read().decode('utf-8')
                    parsedjson = json.loads(rawjson)
                    if self.listimage:
                        for ListPhoto in parsedjson:
                            imgfilename = datetime.today().strftime('%Y%m%d-%H%M%S') + '_' + ListPhoto['author'] + "." + ListPhoto['url'].split('.')[-1]
                            print("Enregistrement de l'image:\n" + os.path.join(DossierImage, imgfilename))
                            urllib.request.urlretrieve(ListPhoto['url'], os.path.join(DossierImage, imgfilename))
                    else:
                        return self.BINGURL + parsedjson['images'][0]['url'][1:]
            else:
                with urllib.request.urlopen(self.NasaURL) as response:
                    rawjson = response.read().decode('utf-8')
                    parsedjson = json.loads(rawjson)
                    print(parsedjson['url'])#['hdurl'])
                    return parsedjson['url']
        except:
            pass"""

    def ConvertBaseTxt(self):
        self.SauvTxtRech(self.UI.TxtBase64T.get(),"CmbBase64T")
        rep=b64encode(self.UI.TxtBase64T.get().encode("utf-8"))
        self.UI.TxtBase64T.set(rep)
        self.UI.t.insert("end", "*******convertion du texte en B64: \n"+ str(rep) + "\n")

    def ConvertBase64(self):
        self.SauvTxtRech(self.UI.TxtBase64.get(),"CmbBase64")
        rep=b64decode(self.UI.TxtBase64.get().encode("utf-8"))
        self.UI.TxtBase64.set(rep)
        self.UI.t.insert("end", "*******convertion de la Base64 en Texte: \n"+ str(rep) + "\n")

    def ConvertHtml(self):
        self.SauvTxtRech(self.UI.TxtHtml.get(),"CmbHtml")
        rep=urllib.parse.unquote(self.UI.TxtHtml.get())
        self.UI.TxtAdresse.set(rep)
        self.UI.t.insert("end", "*******convertion de l'adresse Html en Adresse lisible: \n"+ str(rep) + "\n")

    def istextfile(self, filename, blocksize = 512):
        try:
            return self.istext(open(filename).read(blocksize))
        except:
            return 0

    def istext(self,s):
        if "\0" in s:
            return 0
        
        if not s:  # Empty files are considered text
            return 1

        # Get the non-text characters (maps a character to itself then
        # use the 'remove' option to get rid of the text characters.)
        t = s.translate(self._null_trans, self.text_characters)

        # If more than 30% non-text characters, then
        # this is considered a binary file
        if len(t)/len(s) > 0.30:
            return 0
        return 1

    def is_binary(self, AdressFich):
        mime = mimetypes.guess_type(AdressFich)
        if mime[0]!= None:
            if mime[0][:4] =='text':
                return False
            else:
                #table = {0: "binary", 1: "text"}
                #self.UI.t.insert("end", "\nAdressFich:"+AdressFich+"\n*******istextfile: "+ str(table[self.istextfile(AdressFich)]))
                #self.UI.t.insert("end", "\n*******mime: "+ str(mime[0]) + "\n")
                return True
        else:
            try:
                fich=open(AdressFich, 'rb').read(1024)
                textchars = bytearray([7,8,9,10,12,13,27]) + bytearray(range(0x20, 0x7f)) + bytearray(range(0x80, 0x100))
                binary = lambda bytes: bool(bytes.translate(None, textchars))
                return binary(fich)
            except:
                return True

    def Recherche(self):
        NumCherch = self.UI.nb.index(self.UI.nb.select())
        Texttrouv = self.UI.TxtRecherche.get()
        Dossier = self.UI.TxtDossier1.get()
        Dossier2 = self.UI.TxtDossier2.get()
        Fichier = self.UI.TxtFichier1.get()
        Fichier2 = self.UI.TxtFichier2.get()
        if NumCherch==0:
            self.UI.t.insert("end", "\n----Recherche: "+Texttrouv+"\nDans le dossier: "+Dossier+"\n")
            self.SauvTxtRech(Texttrouv,"CmbRecherche")
            self.SauvTxtRech(Dossier,"CmbDossier")
            for dirname, dirnames, filenames in os.walk(Dossier):
                # print path to all filenames.
                for filename in filenames:
                    if self._stop:
                        break
                    while self._pause:
                        sleep(0.1)
                    if Texttrouv in filename:
                        Nom1 = os.path.join(dirname, filename)
                        self.UI.t.insert("end", Nom1 + "\n")
                    sleep(0.02)
        elif NumCherch==1:
            self.UI.t.insert("end", "\n----Dans le Fichier "+Fichier+":\n")
            self.SauvTxtRech(Texttrouv,"CmbRecherche")
            self.SauvTxtRech(Dossier,"CmbFichier")
            NumeroLigne=0
            if len(Fichier)>0:
                #if not self.is_binary(Fichier):
                try:
                    f = open(Fichier, mode='rt', encoding = "ISO-8859-1")
                    for Ligne in f.readlines():
                        if self._stop:
                            break
                        while self._pause:
                            sleep(0.1)
                        NumeroLigne+=1
                        if Texttrouv in Ligne:
                            self.UI.t.insert("end", "\n   A la ligne: "+str(NumeroLigne) + "\nDans le texte: "+Ligne)
                        sleep(0.02)
                except Exception as err:
                    print(err)
                    self.UI.t.insert("end", "Erreur lecture fichier: "+Fichier+"\n"+str(err))
                f.close()
                #else:
                #    self.UI.t.insert("end", "         Erreur lecture fichier: \n   Ce fichier n'est pas un fichier texte...")
        elif NumCherch==2:
            self.UI.t.insert("end", "\n-----Recherche: "+Texttrouv+"\nDans le dossier: "+Dossier)
            self.SauvTxtRech(Texttrouv,"CmbRecherche")
            self.SauvTxtRech(Dossier,"CmbDossier")
            for dirname, dirnames, filenames in os.walk(Dossier):
                for filename in filenames:
                    if self._stop:
                        break
                    while self._pause:
                        sleep(0.1)
                    Nom1 = os.path.join(dirname, filename)
                    NumeroLigne=0
                    if not self.is_binary(Nom1): #if filename[-4:]!=".pyo":
                        self.UI.t.insert("end", "\nOuverture du Fichier "+filename)
                        try:
                            f = open(Nom1, encoding = "ISO-8859-1")
                            for Ligne in f.readlines():
                                if self._stop:
                                    break
                                while self._pause:
                                    sleep(0.01)
                                NumeroLigne+=1
                                if Texttrouv in Ligne:
                                    self.UI.t.insert("end", "\nDans le Fichier "+Nom1[len(Dossier):]+":\n   A la ligne: "+str(NumeroLigne))
                                    self.UI.t.insert("end", "\nDans le texte: "+Ligne+"\n")
                            sleep(0.02)
                        except Exception as err:
                            self.UI.t.insert("end", "\nErreur lecture fichier: "+Nom1+"\n"+str(err))
                        try:
                            f.close()
                        except:
                            pass
        elif NumCherch==3:
            self.UI.t.insert("end", "\n-----Recherche de différence entre les dossiers:\n Dossier 1 = "+Dossier+"\n Dossier 2 = "+Dossier2)
            self.SauvTxtRech(Dossier,"CmbDossier")
            self.SauvTxtRech(Dossier2,"CmbDossier")
            for dirname, dirnames, filenames in os.walk(Dossier):
                # print("path to all filenames.")
                for filename in filenames:
                    if self._stop:
                        break
                    while self._pause:
                        sleep(0.1)
                    Nom1 = os.path.join(dirname, filename)
                    Nom2 = os.path.join(Dossier2, dirname[len(Dossier)+1:], filename)
                    Taille1 = 0
                    Taille2 = 0
                    TMod1 = 0
                    TMod2 = 0
                    f = None
                    g = None
                    if os.path.exists(Nom2):
                        try:
                            st = os.stat(Nom1)
                        except IOError:
                            self.UI.t.insert("end", "\nErreur de recherche d'information sur le fichier: "+ Nom1)
                        else:
                            #print("\n"+str(st))
                            #print("\n"+str(ST_SIZE))
                            Taille1 = st[ST_SIZE]
                            TMod1 = st[ST_MTIME]
                            #print("file modified:", time.asctime(time.localtime(st[ST_MTIME])))
                            try:
                                st = os.stat(Nom2)
                            except IOError:
                                self.UI.t.insert("end", "\nErreur de recherche d'information sur le fichier: "+ Nom2)
                            else:
                                Taille2 = st[ST_SIZE]
                                TMod2 = st[ST_MTIME]
                                if Taille2 != Taille1:
                                    self.UI.t.insert("end", "\nLa taille du fichier "+os.path.join(dirname[len(Dossier)+1:], filename)+" est different!")
                                    
                                if TMod1 != TMod2:
                                    self.UI.t.insert("end", "\nLa date du fichier "+os.path.join(dirname[len(Dossier)+1:], filename)+" est different!")
                                
                                try:
                                    #if filename[-3:]==".py" or filename[-4:]==".txt"  or filename[-4:]==".xml"  or filename[-4:]==".png"  :
                                    if not self.is_binary(Nom1) and not self.is_binary(Nom2):
                                        f = open(Nom1, encoding = "ISO-8859-1")
                                        g = open(Nom2, encoding = "ISO-8859-1")
                                        ch1 = f.read()
                                        ch2 = g.read()
                                        if len(ch1)!=len(ch2):
                                            self.UI.t.insert("end", '\nTaille du fichier '+filename+' :'+str(len(ch1)))
                                            self.UI.t.insert("end", '\nTaille dans le dossier 2 :'+str(len(ch2)))
                                        for x in iter(range(min(len(ch1),len(ch2)))):
                                            if self._stop:
                                                break
                                            while self._pause:
                                                sleep(0.1)
                                            if ch1[x]!=ch2[x]:
                                                self.UI.t.insert("end", "\nLes deux fichiers sont identiques jusqu'a:\n")
                                                deb = x-100
                                                if deb<0:
                                                    self.UI.t.insert("end", repr(ch1[0:x]))
                                                else:
                                                    self.UI.t.insert("end", "..........."+repr(ch1[deb:x]))
                                                self.UI.t.insert("end", "\nPuis les deux caracteres suivants sont different:")
                                                self.UI.t.insert("end", "\nfichier un:\n"+repr(ch1[x:x+100]))
                                                self.UI.t.insert("end", "\nfichier deux:\n"+repr(ch2[x:x+100]))
                                                break
                                    
                                    sleep(0.02)
                                except Exception as err:
                                     self.UI.t.insert("end", "\nErreur de lecture du fichier: "+ Nom1)
                                try:
                                    f.close()
                                    g.close()
                                except:
                                    pass
                    else:
                        self.UI.t.insert("end", "\n*****Fichier present que dans le dossier1: "+os.path.join(dirname[len(Dossier)+1:],filename))
                    sleep(0.02)
            for dirname, dirnames, filenames in os.walk(Dossier2):
                # print path to all filenames.
                for filename in filenames:
                    if self._stop:
                        break
                    while self._pause:
                        sleep(0.1)
                    Nom2 = os.path.join(Dossier, dirname[len(Dossier2)+1:], filename)
                    if not os.path.exists(Nom2):
                        self.UI.t.insert("end", "\n*****Fichier present que dans le dossier2: "+os.path.join(dirname[len(Dossier2)+1:],filename))
                    sleep(0.02)
        elif NumCherch==4:
            Nom1 = Fichier
            Nom2 = Fichier2
            if len(Fichier)>0 and len(Fichier2)>0:
                self.UI.t.insert("end", "\n-----Recherche de difference entre les Fichiers:\n Fichier 1 = "+Fichier+"\n Fichier 2 = "+Fichier2)
                self.SauvTxtRech(Fichier,"CmbFichier")
                self.SauvTxtRech(Fichier2,"CmbFichier")
                try:
                    #if filename[-3:]==".py" or filename[-4:]==".txt"  or filename[-4:]==".xml"  or filename[-4:]==".png"  :
                    if not self.is_binary(Fichier) and not self.is_binary(Fichier2):
                        f = open(Fichier, encoding = "ISO-8859-1")
                        g = open(Fichier2, encoding = "ISO-8859-1")
                        ch1 = f.read()
                        ch2 = g.read()
                        for x in iter(range(min(len(ch1),len(ch2)))):
                            if self._stop:
                                break
                            while self._pause:
                                sleep(0.1)
                            if ch1[x]!=ch2[x]:
                                self.UI.t.insert("end", "\nLes deux fichiers sont identiques jusqu'a:\n")
                                deb = x-100
                                if deb<0:
                                    self.UI.t.insert("end", repr(ch1[0:x]))
                                else:
                                    self.UI.t.insert("end", "..........."+repr(ch1[deb:x]))
                                self.UI.t.insert("end", "\nPuis les deux caracteres suivants sont differents:")
                                self.UI.t.insert("end", "\nfichier un:\n"+repr(ch1[x:x+100]))
                                self.UI.t.insert("end", "\nfichier deux:\n"+repr(ch2[x:x+100]))
                                break
                    sleep(0.02)
                except Exception as err:
                     self.UI.t.insert("end", "\nErreur de lecture du fichier: "+ str(err))
                try:
                    f.close()
                    g.close()
                except:
                    pass
            else:
                self.UI.t.insert("end", "\n-----Veuillez choisir les Fichiers... ")
        elif(NumCherch==6):
            try:
                self.SauvTxtRech(self.UI.TxtAdresse.get(),"CmbAdresse")
                with urllib.request.urlopen(self.UI.TxtAdresse.get()) as Dl:
                    xinf = Dl.info()
                    print(xinf)
                    #Content-Type: text/html; charset=UTF-8
                    Ext = str(xinf).split("Content-Type: ")[1].split("\n")[0]
                    Ext = Ext.replace("/","(*.")+")"
                    self.UI.t.insert("end", "*******Type de fichier a Telecharger: \n   "+ Ext + "\n")
                    if Ext[:4]=="text":
                        if Ext[7:11]=="html":
                            if bs4:
                                soup = bs4.BeautifulSoup(Dl.read(),features="html.parser")
                                #self.UI.t.insert("end", str(dir(soup)) + "\n")
                                Tag = self.UI.TxtTagHtml.get()
                                self.SauvTxtRech(Tag,"CmbTagHtml")
                                if not Tag:
                                    self.UI.t.insert("end", str(soup) + "\n")
                                else:
                                    for a in soup.find_all(Tag):
                                        self.UI.t.insert("end", str(a) + "\n")
                            else:
                                self.UI.t.insert("end", str(Dl.read()) + "\n")
                        elif Ext[5:9]=="json":
                            rawjson = Dl.read() #.decode('UTF-8')
                            parsedjson = json.loads(rawjson)
                            self.UI.t.insert("end", str(parsedjson) + "\n")
                        else:
                            print(Ext)
                    elif Ext[0:5]=="image":
                        import requests
                        import shutil
                        from tkinter import PhotoImage
                        r = requests.get(self.UI.TxtAdresse.get(), stream=True)
                        if r.status_code == 200:
                            with open("imageText.jpg", 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                        im = Image.open("imageText.jpg") #PhotoImage(file = "imageText.jpg")
                        im.show()
                        #self.UI.t.image_create("end", image = im) # Example 1
                        #self.UI.t.window_create(tk.END, window = tk.Label(text, image = img)) # Example 2
                    else:
                        self.UI.t.insert("end", Ext + "\n")
                        print(Ext)
                    """with open(self.dest, 'wb') as vid:
                        print("Ecriture de : "+self.dest)
                        i = 0
                        for i in range(0, self.longeur, Longeur):
                            sleep(0.01)
                            vid.write(Dl.read(Longeur))
                            pourcentage = ((i*100)/self.longeur)
                            self.progduthread.emit(pourcentage)
                        if self.longeur < i:
                            vid.write(video.read(self.longeur-i))
                        self.progduthread.emit(100)
                        # signale que le thread est terminï¿œ
                        print("00000000")
                        self.finduthread.emit("Fin du tï¿œlï¿œchargement")
                        print("00000001")
                        sleep(2)"""
            except Exception as err:
                self.UI.t.insert("end", "*******Erreur de telechargement: \n   "+ str(err) + "\n*******\n")
            """try:
                import json
                from datetime import datetime
                if not Nasa:
                    with urllib.request.urlopen(self.BINGURL + self.JSONURL) as response:
                        rawjson = response.read().decode('utf-8')
                        parsedjson = json.loads(rawjson)
                        if self.listimage:
                            for ListPhoto in parsedjson:
                                imgfilename = datetime.today().strftime('%Y%m%d-%H%M%S') + '_' + ListPhoto['author'] + "." + ListPhoto['url'].split('.')[-1]
                                print("Enregistrement de l'image:\n" + os.path.join(DossierImage, imgfilename))
                                urllib.request.urlretrieve(ListPhoto['url'], os.path.join(DossierImage, imgfilename))
                        else:
                            return self.BINGURL + parsedjson['images'][0]['url'][1:]
                else:
                    with urllib.request.urlopen(self.NasaURL) as response:
                        rawjson = response.read().decode('utf-8')
                        parsedjson = json.loads(rawjson)
                        print(parsedjson['url'])#['hdurl'])
                        return parsedjson['url']
            except:
                pass"""
        else:
            self.UI.t.insert("end", "\nNuméro recherche inconnu: "+str(NumCherch))
        self.UI.t.insert("end", "\n*****  Recherche terminée  *****")
        self.Stop()

    def get_file_type(self,path):
        """Retrieve the file type of the path
        :param path: The path to get the file type for
        :return: The file type as a string or None on error
        """
        f_types = {
                    'socket':           stat.S_IFSOCK,
                    'regular':          stat.S_IFREG,
                    'block':            stat.S_IFBLK,
                    'directory':        stat.S_IFDIR,
                    'character_device': stat.S_IFCHR,
                    'fifo':             stat.S_IFIFO,
                }
        if not path or not os.path.exists(path):
            return None

        obj = os.stat(path).st_mode
        for key,val in f_types.items():
            if obj & val == val:
                return key

    def ChoixDossier(self):
        rep = filedialog.askdirectory(initialdir=self.DefRep,title='Choisissez un repertoire')
        if len(rep) > 0:
            self.UI.TxtDossier1.set(rep)
            self.DefRep = rep

    def ChoixDossier2(self):
        rep = filedialog.askdirectory(initialdir=self.DefRep,title='Choisissez un repertoire')
        if len(rep) > 0:
            self.UI.TxtDossier2.set(rep)
            self.DefRep = rep

    def ChoixFichier(self):
        Fich = filedialog.askopenfilename(title="Ouvrir un fichier texte",filetypes=[('all files','.*')],initialdir=self.DefRep)#[('gif files','.gif'),('all files','.*')]
        if len(Fich) > 0:
            self.UI.TxtFichier1.set(Fich)
            self.DefRep = os.path.dirname(Fich)
            
    def ChoixFichier2(self):
        Fich = filedialog.askopenfilename(title="Ouvrir un fichier texte",filetypes=[('all files','.*')],initialdir=self.DefRep)#[('gif files','.gif'),('all files','.*')]
        if len(Fich) > 0:
            self.UI.TxtFichier2.set(Fich)
            self.DefRep = os.path.dirname(Fich)

    def EffaceResult(self):
        self.UI.t.delete('1.0', "end")
    
    def Quitter(self):
        quit()


if __name__ == '__main__':
    application = App()    # Instanciation de la classe
    print(Enum)
    marshal.dump(Enum, open('EnumExplorFich.dat', 'wb'))
    #application.mainloop()          # Boucle pour garder le programme en vie
    #application.quit()              # Fermeture propre ï¿œ la sortie de la boucle
