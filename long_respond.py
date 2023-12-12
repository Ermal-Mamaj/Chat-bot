import random

A_pershendetje = "Përshëndetje"
A_SiJeni = "Mirë faleminderit , po ju?"
A_mirmengjes = 'Mirëmëngjesi , shpresoj që të keni një ditë sa më të bukur'
A_mirdita = 'Mirëdita , shpresoj që dita juaj po shkonë sa më mirë që të jetë e mundur'
A_mirmrama = 'Mirëmbrëma, shpresoj që dita juaj ka shkuar sa më mirë të jetë e mundur'
A_diqkaInteresant = 'Kur nuk të donë familja joteeee , , nuk të don as Kojshia'
A_Bugga = "E ngjo , pe lujeke fort CS Go-ne"
A_Kaprolli = 'Po mar qysh se ngjo Dionis Currin'

def unknown():
    response = ["Coulde u please re-phrase that?",
                "Shko mytu",
                "Ti koke hut",
                "what doese that mean?"][random.randrange(4)]
    return response