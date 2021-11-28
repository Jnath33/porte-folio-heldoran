
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
    return f"<li><ul class=\"poeme\">\n{t}<li><titre>{title}</titre></li>\n{t}<li><numero>Défi n°{d_id}</numero></li>\n{t}" + \
        f"<li><contenu>\n{t}{t}{c_text}\n{t}</contenu></li>\n</ul></li>"



print(get_poeme())