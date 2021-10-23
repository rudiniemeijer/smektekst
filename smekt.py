# SmekTekst

# The "ing"s are added by the goofy string builder

from random import choice
from time import sleep

# De "en"s worden later in de code toegevoegd
opbouwWerkwoorden = [
    "Aanroep",
    "Instell",
    "Configurer",
    "Versnell",
    "Ophog",
    "Inlad",
    "Certificer",
    "Compileren en link",
    "Parametriser",
    "Vectoriser",
    "Legaliser",
    "Open",
    "Instantiër",
    "Uitklapp",
    "Oplad",
    "Sommer",
    "Opschal"
]
afbouwWerkwoorden = [
    "Vertrag",
    "Desolder",
    "Inklapp",
    "Degrader",
    "Demagnetiser",
    "Ontlad",
    "Afschal",
    "Verwijder",
    "Opschon",
    "Afbrek"
]

versterkingsNaamwoorden = [
    "Vertraagd",
    "Gecontroleerd",
    "Gelijkmatig",
    "Afrondend",
    "Structureel",
    "Nauwkeurig",
    "Efficiënt",
    "Definitief",

    "Serieel",
    "Parallel",
    "Geluidloos"
]

bijvoegelijkeNaamwoorden = [
    "onzichtbare",
    "onduidelijke",
    "meerkleurige",
    "kleine",
    "speciale",
    "multifunctionele",
    "goedkope",
    "hyperactieve",
    "snelle",
    "energiezuinige",

    "geleidende",
    "weerbarstige",
    "miniatuur",
    "micro",
    "voordelige",
    "bidirectionele",
    "magische",
    "groene",
    "blauwe",
    "rode",

    "ingewikkelde",
    "destructieve",
    "talrijke",
    "explosieve",
    "geladen",
    "ontladen",
    "gewichtige",
    "illegale"
]

# Mannelijk of meervoud
zelfstandigeNaamwoorden = [
    "printsporen",
    "processor",
    "condensator",
    "zenerdiode",
    "Cucumber testen",
    "Robot framework",
    "unittesten",
    "weerstandsarray",
    "certificaten",
    "wifiverbinding",
    "lijnbus",
    "toetsconfiguratie",
    "broncode",
    "geleider",
    "transmutatiemodule",
    "geheugenmodule",
    "spreadsheet",
    "getallen",
    "router",
    "gateway",
    "airfryer"
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