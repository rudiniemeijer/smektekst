from smekt import smekTekst
from random import choice
from time import sleep


while True:
    opbouw = choice([True, False])
    smekRegel = smekTekst(opbouw)

    if not opbouw:
        smekRegel = "- " + smekRegel
    else:
        smekRegel = "+ " + smekRegel

    print(smekRegel)
    sleep(1)