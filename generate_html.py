
title = \
"""Jeux Olympiques"""

t = "    "

d_id = 1

text = \
"""Datant de la grande Olympie,
Grande ville antique du sport,
Vidant la faim de ces kelpies
Aux métiers venant du sport.

A ce jour, toutes les nations
Ce battent avec acharnement,
Grâce a la détermination
D'athlètes aux milles entrainement.

Ils datent de la Grèce antique,
Mais ils ont changé leurs mimiques,
Et admirez les de nos jours,

Ils sont toujours de retour.
Regardez les, ces Magnifiques,
Admirez les Jeux Olympiques."""

def get_somaire():
    print("")

def get_poeme():
    c_text = text.replace('\n', f"<br/>\n{t}{t}")
    return f"<div class=\"poeme\">\n{t}<titre>{title}</titre>\n{t}<numero>Défi n°{d_id}</numero>\n{t}" + \
        f"<contenu>\n{t}{t}{c_text}\n{t}</contenu>\n</div>"



print(get_poeme())