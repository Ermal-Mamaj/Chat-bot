import random
import time

A_pershendetje = "Përshëndetje"
A_prezantimi = "Unë jamë një program i thejshtë për këtë arsye unë nuk kam emer"
A_aftesit = ("une mund të:     *******")
A_filem = "Unë do ju rekomandoja filmin 'Inception' ose 'Interstellar',të dy filma të zhandrit fatastiko-shkencor"
A_SiJeni = "Mirë faleminderit , po ju?"
A_mirmengjes = 'Mirëmëngjesi , shpresoj që të keni një ditë sa më të bukur'
A_mirdita = 'Mirëdita , shpresoj që dita juaj po shkonë sa më mirë që të jetë e mundur'
A_mirmrama = 'Mirëmbrëma, shpresoj që dita juaj ka shkuar sa më mirë të jetë e mundur'
A_serial = "Ndër serialet më të shikuar dhe më të rekomanduar në botë janë: 'Game of Thrones','La Casa De Papel','Prison Breake'"
local_time = time.localtime(time.time())
A_koha = 'Ora tani është'+time.strftime(" %H:%M:%S",local_time).__str__()
A_data = 'Data sot është'+time.strftime("%d-%m-%Y" ,local_time).__str__()



A_diqkaInteresant = 'Kur nuk të donë familja joteeee , , nuk të don as Kojshia'
A_Libra = 'Unë do ju sugjeroja librin Hamlet nga William Shkekspire'
A_Muzik = 'Në bazë të zhanrit që preferoni, unë mund të ju rekumandoj:\n Hip-Hop -> 50 cent & Lil Wayne \n Balad-> The Weeknd \n Rap -> Eminem & Kendrick Lemar'


response_counter = 0
def unknown():
    global response_counter
    response_counter += 1
    if response_counter > 2:
        return "Kërkoj falje por unë nuk e di përgjigjjen e kësaj pyetje"
    response = ["Nuk po e kuptoj qfar doni të thoni",
                "A mund ta përsërisni edhe një herë ",
                "Kontrolloni nëse pyetja është e shkruar saktë",
                ][random.randrange(3)]

    return response
