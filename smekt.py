# SmekTekst

# The "ing"s are added by the goofy string builder

from random import choice
from time import sleep

# De "en"s worden later in de code toegevoegd
opbouwWerkwoorden = [
    "Instell",
    "Open",
    "Insmer",
    "Vastschroev",
    "Aanpass",
    "Configurer",
    "Instantiër",
    "Opstok",
    "Bakk",
    "Calibrer",

    "Lad",
    "Aflebber",
    "Oppoets",
    "Informer",
    "Fork",
    "Push",
    "Compiler",
    "Beluister",
    "Aanroep",
    "Inplugg",
    
    "Verbind",
    "Solder",
    "Opwaarder",
    "Verlegg",
    "Beprikk",
    "Afdrukk",
    "Inklapp",
    "Instell",
    "Verbuig",
    "Opbell",

    "Benader",
    "Aanhoud",
    "Ophog",
    "Vermenigvuldig",
    "Installer",
    "Aanbreng"
]

afbouwWerkwoorden = [
    "Afschroev",
    "Comprimer",
    "Schur",
    "Evaluer",
    "Demonter",
    "Afzijk",
    "Desolder",
    "Afpell",
    "Demp",
    "Dichtmak",

    "Sluit",
    "Ontkoppel",
    "Verwijder",
    "Afbrek",
    "Afragg",
    "Doorknipp",
    "Leegmak",
    "Opschon",
    "Verbuig",
    "Ophang",

    "Demagnetiser",
    "Deinstaller",
    "Ontmoedig"
]

versterkingsNaamwoorden = [
    "Versneld",
    "Volledig",
    "Transparant",
    "Grondig",
    "Egaal",
    "Afrondend",
    "Opvallend"
]

bijvoegelijkeNaamwoorden = [
    "onzichtbare",
    "schitterende",
    "veelkleurige",
    "minimalistische",
    "speciale",
    "multifunctionele",
    "modieuze",
    "hyperactieve",
    "snelle",
    "energiezuinige",
    "supergeleidende",
    "weerbarstige",
    "mini",
    "micro",
    "voordelige",
    "bidirectionele",
    "magische",
    "groene",
    "blauwe",
    "rode",
    "ingewikkelde",
    "destructieve"
]

# Mannelijk of meervoud
zelfstandigeNaamwoorden = [
    "inhoud",
    "weergavemodule",
    "API",
    "kristallen",
    "transmutatie",
    "geluiden",
    "bedrading",
    "processor",
    "microcontroller",
    "transistoren",
    "bits",
    "kolommen",
    "menu opties",
    "geheugenmodule",
    "wifiverbinding",
    "bluetooth antenne",
    "cameralens",
    "toetsen",
    "behuizing",
    "diodes",
    "weerstandsarray",
    "douchehokje",
    "lijnbus",
    "spreadsheet",
    "documenten",
    "Raspberry Pi",
    "protocollen",
    "voltage",
    "kernwaarde",
    "chips",
    "signalen",
    "sensoren",
    "warp drive",
    "lichtsnelheid",
    "batterijvoltage",
    "taktieken",
    "fouten",
    "witte rook",
    "software",
    "magneten",
    "geleiders",
    "condensatoren",
    "kijkers"
]

def smekTekst(opbouw):
    smekWoord = choice(zelfstandigeNaamwoorden)
    if choice(range(0,100)) > 90:
        smekWoord = choice(bijvoegelijkeNaamwoorden) + " " + smekWoord

    if opbouw:
        smekWerkwoord = choice(opbouwWerkwoorden) + "en"
    else:
        smekWerkwoord = choice(afbouwWerkwoorden) + "en"

    if choice(range(0,100)) > 90:
        smekWerkwoord = choice(versterkingsNaamwoorden) + " " + smekWerkwoord.lower()

    smekRegel = smekWerkwoord + " " + smekWoord

    if len(smekRegel) < 18:
      smekRegel += "..."

    return smekRegel