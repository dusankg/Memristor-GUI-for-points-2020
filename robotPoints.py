import tkinter as tk


''' TODO
1. setuj da ne bude resizable
2. podesi sve unose
3. napravi backend funkcije za racunanje
'''

# set windows
win = tk.Tk()
win.resizable(0,0)
win.title("Robot points 2020")
win.geometry("600x600")
#image1 = Image.open('background_image.jpg')
backgroundImage = tk.PhotoImage(file = 'background_image_case.png')
background_label = tk.Label(win, image=backgroundImage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# points variables
table_points = tk.IntVar()
robot_points = tk.IntVar()
total_points = tk.IntVar()

# true or false variables
vetrokaz1 = tk.BooleanVar()
vetrokaz2 = tk.BooleanVar()
antena = tk.BooleanVar()
zastavica = tk.BooleanVar()
# count of glasses variables
crvene_linija_velika = tk.IntVar()
case_unutar_velika = tk.IntVar()
zelene_linija_velika = tk.IntVar()
crvene_mala = tk.IntVar()
zelene_mala = tk.IntVar()
unutar_mala = tk.IntVar()
roboti_u_dobroj_luci = tk.IntVar()

# functions for count points
def count_table_points():
    # logic for counting points
    ukupno = 0

    # velika luka
    # 1 bod za sve u luci, 1 bod po svakoj koja je na svojoj boji, 2 boda za svaki par
    validne_case = crvene_linija_velika.get() + zelene_linija_velika.get() + case_unutar_velika.get()
    parovi = int((crvene_linija_velika.get() + zelene_linija_velika.get()) / 2 )
    ukupno = ukupno + validne_case + crvene_linija_velika.get() + zelene_linija_velika.get() + parovi*2

    # mala luka
    # 1 bod za sve u luci, 1 bod po svakoj koja je na svojoj boji, 2 boda za svaki par
    validne_case = crvene_mala.get() + zelene_mala.get() + unutar_mala.get()
    parovi = int((crvene_mala.get() + zelene_mala.get()) / 2 )
    ukupno = ukupno + validne_case + crvene_mala.get() + zelene_mala.get() + parovi*2

    # vetrenjace
    vetrenjace_bodovi = 0
    if (vetrokaz1.get() == 1 and vetrokaz2.get() == 1):
        vetrenjace_bodovi = 15
    elif ((vetrokaz1.get() == 1 and vetrokaz2.get() == 0) or (vetrokaz1.get() == 0 and vetrokaz2.get() == 1)):
        vetrenjace_bodovi = 5
    ukupno = ukupno + vetrenjace_bodovi

    # svetionik bodovi
    # 2 boda ako je postavljen, +3 ako je aktiviran, +10 ako je validan
    # za sada cu da stavim samo jedan bool za svih 15, da smanjim komplikaciju
    svetionik_bodovi = 0
    if(antena.get()):
        svetionik_bodovi = 15
    ukupno = ukupno + svetionik_bodovi

    # roboti u luci
    # doraditi logiku na osnovu strane 16 iz pravila
    roboti_luka_bodovi = roboti_u_dobroj_luci.get() * 5
    ukupno = ukupno + roboti_luka_bodovi

    # podignuta zasavica
    zastavica_bodovi = 0
    if(zastavica.get()):
        zastavica_bodovi = 10

    ukupno = ukupno + zastavica_bodovi

    table_points.set(ukupno)


def count_total_points():
    delta = robot_points.get() - table_points.get()
    if(delta < 0):
        delta = - delta

    bonus = (0.3 * table_points.get()) - delta
    if(bonus < 0):
        bonus = 0

    total_points.set(table_points.get() + bonus)


# elements of GUI
lab_antena = tk.Label(win, text = "Svetionik")
lab_antena.place(x=417, y=50)
tk.Checkbutton(win, variable=antena).place(x=425, y=65)

lab_vetrokaz1 = tk.Label(win, text = "Vetrokaz 1")
lab_vetrokaz1.place(x=360, y=360)
tk.Checkbutton(win, variable=vetrokaz1).place(x=370, y=380)

lab_vetrokaz2 = tk.Label(win, text = "Vetrokaz 2")
lab_vetrokaz2.place(x=420, y=360)
tk.Checkbutton(win, variable=vetrokaz2).place(x=430, y=380)

# case
lab_crvene_na_liniji_velika = tk.Label(win, text = "Crvene na liniji")
lab_crvene_na_liniji_velika.place(x=500, y=140)
tk.OptionMenu(win, crvene_linija_velika, 0,1,2,3,4,5,6).place(x=515, y=160)

lab_case_unutar_velika = tk.Label(win, text = "Case unutar")
lab_case_unutar_velika.place(x=500, y=190)
tk.OptionMenu(win, case_unutar_velika, 0,1,2,3,4,5,6).place(x=515, y=210)

lab_zelene_na_liniji_velika = tk.Label(win, text = "Zelene na liniji")
lab_zelene_na_liniji_velika.place(x=500, y=240)
tk.OptionMenu(win, zelene_linija_velika, 0,1,2,3,4,5,6).place(x=515, y=260)

lab_zelene_na_liniji_mala = tk.Label(win, text = "Zelene")
lab_zelene_na_liniji_mala.place(x=130, y=350)
tk.OptionMenu(win, zelene_mala, 0,1,2,3,4,5,6).place(x=130, y=370)


lab_crvene_na_liniji_mala = tk.Label(win, text = "Crvene")
lab_crvene_na_liniji_mala.place(x=235, y=350)
tk.OptionMenu(win, crvene_mala, 0,1,2,3,4,5,6).place(x=230, y=370)


lab_unutar_mala = tk.Label(win, text = "Unutar")
lab_unutar_mala.place(x=180, y=350)
tk.OptionMenu(win, unutar_mala, 0,1,2,3,4,5,6).place(x=180, y=370)

# button for counting points from table
tk.Button(win, text="Bodovi sa stola", command = count_table_points).place(x=80, y=530)
tk.Label(win, textvariable = table_points).place(x=200, y=530)

# enter prediction points
tk.Label(win, text = "Predikcija: ").place(x=290, y=450)
box_prediction = tk.Entry(win, textvariable = robot_points)
box_prediction.place(x=350, y=450)

# total points
tk.Button(win, text = "Ukupni bodovi", command = count_total_points).place(x=290, y=530)
tk.Label(win, textvariable = total_points).place(x=410, y=530)

# robots in valid mooring zone
tk.Label(win, text = "Roboti u dobroj luci: ").place(x=80, y=450)
tk.OptionMenu(win, roboti_u_dobroj_luci, 0,1,2).place(x=210, y=442)

# raisted flag
tk.Label(win, text = "Podignuta zastavica").place(x=80, y=485)
tk.Checkbutton(win, variable=zastavica).place(x=210, y=485)

win.mainloop()


