import random

A_pershendetje = "Përshëndetje"
A_prezantimi = "Unë jamë një program i thejshtë për këtë arsye unë nuk kam emer"
A_aftesit = ("une mund të:     *******")
A_filem = "Unë do ju rekomandoja filmin 'Inception' ose 'Interstellar',të dy filma të zhandrit fatastiko-shkencor"
A_SiJeni = "Mirë faleminderit , po ju?"
A_mirmengjes = 'Mirëmëngjesi , shpresoj që të keni një ditë sa më të bukur'
A_mirdita = 'Mirëdita , shpresoj që dita juaj po shkonë sa më mirë që të jetë e mundur'
A_mirmrama = 'Mirëmbrëma, shpresoj që dita juaj ka shkuar sa më mirë të jetë e mundur'
A_serial = "Ndër serialet më të shikuar dhe më të rekomanduar në botë janë: 'Game of Thrones','La Casa De Papel','Prison Breake'"



A_diqkaInteresant = 'Kur nuk të donë familja joteeee , , nuk të don as Kojshia'
A_Bugga = "E ngjo , pe lujeke fort CS Go-ne"
A_Kaprolli = 'Po mar qysh se ngjo Dionis Currin'
A_Libra = 'Unë do ju sugjeroja librin Hamlet nga William Shkekspire'
A_Muzik = 'Në bazë të zhanrit që preferoni, unë mund të ju rekumandoj:\n Hip-Hop -> 50 cent & Lil Wayne \n Balad-> The Weeknd \n Rap -> Eminem & Kendrick Lemar'

def unknown():
    response = ["Coulde u please re-phrase that?",
                "Shko mytu",
                "Ti koke hut",
                "what doese that mean?"][random.randrange(4)]
    return response