# SmekTekst

# The "ing"s are added by the goofy string builder

from random import choice
from time import sleep

# De "en"s worden later in de code toegevoegd
opbouwWerkwoorden = [
    "Instell",
    "Open",
    "Verdel",
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
    "Versnell",
    "Fork",
    "Push",
    "Compiler",
    "Beluister",
    "Aanroep",
    "Inplugg",
    
    "Verbind",
    "Vastsolder",
    "Opwaarder",
    "Verlegg",
    "Betast",
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
    "Aanbreng",
    "Opsmukk",
    "Verenig",
    "Compileren en link",
    "Legaliser",

    "Certificer",
    "Identificer",
    "Oplad",
    "Vectoriser",
    "Parametriser",
    "Extern inbell",
    "Transmuter"
]

afbouwWerkwoorden = [
    "Afschroev",
    "Comprimer",
    "Afschal",
    "Evaluer",
    "Demonter",
    "Bekritiser",
    "Desolder",
    "Afpell",
    "Demp",
    "Dichtmak",

    "Afsluit",
    "Ontkoppel",
    "Verwijder",
    "Afbrek",
    "Vertrag",
    "Versnijd",
    "Leegmak",
    "Opschon",
    "Verbuig",
    "Ophang",

    "Demagnetiser",
    "Deinstaller",
    "Ontmoedig",
    "Uitsmer",
    "Vernietig",
    "Neerhal",
    "Inschuiv",
    "Aanhoud",
    "Uitholl",
    "Degrader",

    "Ontlad",
    "Oploss"
]

versterkingsNaamwoorden = [
    "Versneld",
    "Vertraagd",
    "Transparant",
    "Fundamenteel",
    "Gelijkmatig",
    "Afrondend",
    "Structureel",
    "Nauwkeurig",
    "Efficiënt",
    "Effectief",

    "Serieel",
    "Parallel",
    "Random",
    "Geluidloos",
    "Pontificaal"
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
    "gewichtige"
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
    "douchehokjes",
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
    "magneet",

    "geleider",
    "condensatoren",
    "kijker",
    "getallen",
    "resultaten",
    "producten",
    "verpakking",
    "broncode",
    "COBOL code",
    "Flask module",

    "Cucumber testen",
    "berekeningen",
    "certificaten",
    "illegalen",
    "neanderthalers",
    "Spark",
    "ledverlichting",
    "spookverlichting",
    "stroomsterkte"
    ""
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