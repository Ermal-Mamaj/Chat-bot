import random

R_eating = "I dont like eating anything cause im a bot i dont eat!"
R_pershendetje = "Përshëndetje"
R_SiJeni = "Mirë faleminderit , po ju?"
def unknown():
    response = ["Coulde u please re-phrase that?",
                "Shko mytu",
                "Ti koke hut",
                "what doese that mean?"][random.randrange(4)]
    return response