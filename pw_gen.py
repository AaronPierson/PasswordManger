#!/usr/bin/env pythonw
import sqlite3
import random
import string
import wx
import glob
import csv
import os.path

# pythonw "C:\Users\rpgam\OneDrive\Docs\School\SouthEast Tech\Summer 2020\CIS 293 30C AO - Advanced Technologies\Project1\pw_gen.py"

# Functions

# shuffle password

def insert_into(web, url, login, question, answer, password):
        conn = sqlite3.connect('AA_db.sqlite')
        cur = conn.cursor()
        cur.execute('''INSERT INTO userPasswords 
        (Website, Url, Login, Question, Answer, SavedPassword) 
        values (?, ?, ?, ?, ?, ?)''', 
        (web, url, login, question, answer, password))
        conn.commit()
        conn.close

def create_table():
        if os.path.exists('AA_db.sqlite') == False:
            conn = sqlite3.connect('AA_db.sqlite')
            cur = conn.cursor()
            cur.execute('''CREATE TABLE userPasswords 
                (Website VARCHAR, 
                Url VARCHAR, 
                Login VARCHAR, 
                Question VARCHAR, 
                Answer VARCHAR, 
                SavedPassword VARCHAR)''')
            conn.close()
            #database does exsit close
            conn.close()
        else:
            print('already exists')

def load_DB():
     # connect to database 
    conn = sqlite3.connect('AA_db.sqlite')
    cur = conn.cursor()
    # display web site, username, and password from database
    sql_command = """
    SELECT * FROM userPasswords'
    """
    cur.execute('SELECT * FROM userPasswords')
    rows = cur.fetchall()
    # for d in rows:
    #     data = d
    conn.close
    return rows

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# random special character


def randChar(length=2):
    characters = '@#$%&!'
    return ''.join((random.choice(characters)) for i in range(length))

# random uppercase letter


def randUpper(length=1):
    uppers = chr(random.randint(65, 90))
    return ''.join((random.choice(uppers)) for i in range(length))

# random lowercase letter


def randLower(length=1):
    lowers = chr(random.randint(97, 122))
    return ''.join((random.choice(lowers)) for i in range(length))

# random number


def randDigit(length=1):
    digits = chr(random.randint(48, 57))
    return ''.join((random.choice(digits)) for i in range(length))

# generate password


def password(length=8):
    # generate random characters using above functions
    uppercaseLetter1 = randUpper()
    uppercaseLetter2 = randUpper()
    lowercaseLetter1 = randLower()
    lowercaseLetter2 = randLower()
    digit1 = randDigit()
    digit2 = randDigit()
    specialChars = randChar()

    # Generate password using all the characters, in random order
    password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + \
        lowercaseLetter2 + digit1 + digit2 + specialChars
    return shuffle(password)

# Saved user data class
class SavedData(object):


    def _init_(self, Website, URL, Login, SecQ, SecA, Password):
        # constructor
        self.Website = web
        self.URL = url
        self.Login = login
        self.SecQ = secq
        self.SecA = seca
        self.Password = password

# GUI

# panel


class PasswordPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        #self.row_obj_dict = {}

# Panel Sizers
        full_panel = wx.BoxSizer(wx.VERTICAL)
        display_panel = wx.BoxSizer(wx.VERTICAL)
        btn_panel = wx.BoxSizer(wx.HORIZONTAL)
    # encompasses all entry textbox panels
        text_panel = wx.BoxSizer(wx.VERTICAL)
        web_sizer = wx.BoxSizer(wx.HORIZONTAL)
        url_sizer = wx.BoxSizer(wx.HORIZONTAL)
        login_sizer = wx.BoxSizer(wx.HORIZONTAL)
        secq_sizer = wx.BoxSizer(wx.HORIZONTAL)
        seca_sizer = wx.BoxSizer(wx.HORIZONTAL)
        pw_sizer = wx.BoxSizer(wx.HORIZONTAL)

    # database display
        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 200),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Website/Company', width=140)
        self.list_ctrl.InsertColumn(1, 'URL', width=140)
        self.list_ctrl.InsertColumn(2, 'Login/ID', width=200)
        self.list_ctrl.InsertColumn(3, 'Security Question', width=200)
        self.list_ctrl.InsertColumn(4, 'Security Answer', width=200)
        self.list_ctrl.InsertColumn(5, 'Password', width=200)
        display_panel.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
            #Load DB
        data = load_DB()
        for d in data:
            self.list_ctrl.InsertItem(0, d[0]) #web
            self.list_ctrl.SetItem(0, 1, d[1]) #url
            self.list_ctrl.SetItem(0, 2, d[2]) #login
            self.list_ctrl.SetItem(0, 3, d[3]) #secq
            self.list_ctrl.SetItem(0, 4, d[4]) #seca
            self.list_ctrl.SetItem(0, 5, d[5]) #pw

    # website text box
        stWeb = wx.StaticText(
            self, label='Website/Company:', style=wx.ALIGN_CENTER)
        self.text_web = wx.TextCtrl(self, value="", style=wx.TE_LEFT)
        # add to sizer
        web_sizer.Add(stWeb, 0, wx.ALL | wx.EXPAND, 5)
        web_sizer.Add(self.text_web, 0, wx.EXPAND)

    # url text box
        stUrl = wx.StaticText(self, label='URL:', style=wx.ALIGN_CENTER)
        self.text_url = wx.TextCtrl(self, value="", style=wx.TE_LEFT)
        # add to sizer
        url_sizer.Add(stUrl, 0, wx.ALL | wx.EXPAND, 5)
        url_sizer.Add(self.text_url, 0, wx.EXPAND)

    # login text box
        stLogin = wx.StaticText(self, label='Login/ID:', style=wx.ALIGN_CENTER)
        self.text_login = wx.TextCtrl(self, value="", style=wx.TE_LEFT)
        # add to sizer
        login_sizer.Add(stLogin, 0, wx.ALL | wx.EXPAND, 5)
        login_sizer.Add(self.text_login, 0, wx.EXPAND)

    # security question text box
        stSecQ = wx.StaticText(
            self, label='Security Question:', style=wx.ALIGN_CENTER)
        self.text_secq = wx.TextCtrl(self, value="", style=wx.TE_LEFT)
        # add to sizer
        secq_sizer.Add(stSecQ, 0, wx.ALL | wx.EXPAND, 5)
        secq_sizer.Add(self.text_secq, 0, wx.EXPAND)

    # security answer text box
        stSecA = wx.StaticText(
            self, label='Security Answer:', style=wx.ALIGN_CENTER)
        self.text_seca = wx.TextCtrl(self, value="", style=wx.TE_LEFT)
        # add to sizer
        seca_sizer.Add(stSecA, 0, wx.ALL | wx.EXPAND, 5)
        seca_sizer.Add(self.text_seca, 0, wx.EXPAND)

    # generate password section
        pwgen_btn = wx.Button(self, label='Generate Password')
        pwgen_btn.Bind(wx.EVT_BUTTON, self.on_press)
        self.text_pw = wx.TextCtrl(self, value="", style=wx.TE_LEFT)
        copy_btn = wx.Button(self, label='Copy')
        copy_btn.Bind(wx.EVT_BUTTON, self.on_copy)
        # add to sizer
        pw_sizer.Add(pwgen_btn, 0, wx.ALL | wx.CENTER, 5)
        pw_sizer.Add(self.text_pw, 0, wx.ALL | wx.EXPAND, 5)
        pw_sizer.Add(copy_btn, 0, wx.ALL | wx.CENTER, 5)

    # add sizers to text_panel
        text_panel.Add(web_sizer, 0, wx.EXPAND, 5)
        text_panel.Add(url_sizer, 0, wx.EXPAND, 5)
        text_panel.Add(login_sizer, 0, wx.ALL | wx.EXPAND, 5)
        text_panel.Add(secq_sizer, 0, wx.ALL | wx.EXPAND, 5)
        text_panel.Add(seca_sizer, 0, wx.ALL | wx.EXPAND, 5)
        text_panel.Add(pw_sizer, 0, wx.ALL | wx.EXPAND, 5)

    # button panel
        add_btn = wx.Button(self, label='Add')
        add_btn.Bind(wx.EVT_BUTTON, self.on_add)
        edit_btn = wx.Button(self, label='Edit')
        #edit_btn.Bind(wx.EVT_BUTTON, self.on_edit)
        # add to sizer
        btn_panel.Add(add_btn, 0, wx.ALL | wx.CENTER, 5)
        btn_panel.Add(edit_btn, 0, wx.ALL | wx.CENTER, 5)

    # add all sub-panels to full_panel
        full_panel.Add(display_panel, flag=wx.EXPAND |
                       wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        full_panel.Add((-1, 10))
        full_panel.Add(text_panel, flag=wx.EXPAND | wx.LEFT |
                       wx.RIGHT | wx.TOP, border=10)
        full_panel.Add((-1, 10))
        full_panel.Add(btn_panel, flag=wx.EXPAND | wx.LEFT |
                       wx.RIGHT | wx.TOP, border=10)
        full_panel.Add((-1, 10))
        # set box sizer and display
        self.SetSizer(full_panel)



# buttons
# action for generate password button
    def on_press(self, event):
        self.text_pw.SetValue(password())
        self.text_pw.SetFocus()
        self.text_pw.SelectAll()
        create_table()

# action for copy button
    def on_copy(self, event):
        self.text_pw.SelectAll()
        self.text_pw.Copy()

# action for add to database
    def on_add(self, event):
        web = self.text_web.GetValue()
        url = self.text_url.GetValue()
        login = self.text_login.GetValue()
        secq = self.text_secq.GetValue()
        seca = self.text_seca.GetValue()
        pw = self.text_pw.GetValue()
        insert_into(web, url, login, secq, seca, pw)
        
        self.list_ctrl.InsertItem(0, web)
        self.list_ctrl.SetItem(0, 1, url)
        self.list_ctrl.SetItem(0, 2, login)
        self.list_ctrl.SetItem(0, 3, secq)
        self.list_ctrl.SetItem(0, 4, seca)
        self.list_ctrl.SetItem(0, 5, pw)
        self.text_web.Clear()
        self.text_url.Clear()
        self.text_login.Clear()
        self.text_secq.Clear()
        self.text_seca.Clear()
        self.text_pw.Clear()
        
# write to csv file

        csvRow=[web, url, login, secq, seca, pw]
        csvfile="passwords.csv"
        with open('passwords.csv', 'a', newline='') as csv_file:
            wr = csv.writer(csv_file, dialect='excel', lineterminator='\n')
            fields = ['Website','URL','User Name', 'Security Q', 'Security A', 'Password']
            wr.writerow(fields)
            
            wr.writerow(csvRow)

# def on_edit(self, event):
#    selection = self.list_ctrl.GetFocusedItem()
#    if selection >= 0:
#        dlg = EditRecord(selection)
#        dlg.ShowModal()

# windows
# main frame


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Password Generator', size=(1200, 600))
        self.panel = PasswordPanel(self)
        self.Show()

# edit modal dialog


class EditRecord(wx.Dialog):
    def __init__(self, record):
        title = f'Editing'
        super().__init__(parent=None, title=title)
        stEditLabel = wx.StaticText(
            self, label='This will be a modal dialog for editing records')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
