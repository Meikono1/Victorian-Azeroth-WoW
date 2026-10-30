"""Länder- und Kulturprofile für va_fill_buildings.py (VA-029).

Jedes Reich bekommt eine Persönlichkeit (Kono): Mächtige Länder bekommen mehr Start-Gebäude, Kulturen und
Lore verschieben die Gewichte. Ein Profil ist ein dict Gruppe → Faktor, fehlende Gruppen zählen 1.
Gruppen: "all" (alles), "food" (Getreide, Ranch), "fish" (Fischerei, Walfang), "plantation", "wood", "mines",
oder eine einzelne Gebäudeart aus RATES (z. B. "building_coal_mine"). Faktoren multiplizieren sich.
Länder ohne Eintrag zählen 1, damit bereits gefüllte Regionen (26, 27) unverändert bleiben.
"""
import logging

log = logging.getLogger("va_profiles")

# Kultur → Profil; gilt, wenn eine Kultur im State vorkommt (wie bisher der Zwergenfaktor)
CULTURES = {
    "bronzebeard": {"mines": 1.5},
    "wildhammer": {"mines": 1.5},
    "dark_iron": {"mines": 1.5},
}

# Süd-EK (28)
_SUED_EK = {
    # Großmacht der Allianz: Kornkammer Elwynn/Westfall, Holz aus Elwynn, Minen Jasperlode/Fargodeep
    "STORMWIND": {"all": 1.4, "food": 1.2, "wood": 1.2},
    # Goblin-Handelsmacht, Hafen Booty Bay: Fisch und Handelsfrüchte statt Ackerbau
    "STEAMWHEEDLE_CARTEL": {"all": 1.2, "fish": 2.0, "plantation": 1.5, "food": 0.7, "wood": 0.8},
    "HARDWRENCH_INDUSTRIES": {"mines": 1.8, "wood": 1.5, "food": 0.5, "plantation": 0.5},
    "VENTURE_CO": {"mines": 1.8, "wood": 2.0, "food": 0.5, "plantation": 0.5},
    # Rest des Gurubashi-Reichs: großes Trollreich, Dschungelfrüchte
    "GURUBASHI_TRIBE": {"all": 1.1, "plantation": 1.3},
    "ZANZIL_WITCHDOCTORS": {"all": 0.7, "plantation": 1.2},
    "BLOODSCALP_TRIBE": {"all": 0.6},
    "SKULLSPLITTER_TRIBE": {"all": 0.6},
    "BAMBALA": {"all": 0.7},
    # Banditen: brennen Höfe nieder, Deadmines (Gold, Werft)
    "DEFIAS_BROTHERHOOD": {"all": 0.8, "food": 0.6, "mines": 1.5, "wood": 1.3},
    # Orks der Schwarzfelsen in Redridge: Krieg und Minen, kaum Landwirtschaft
    "BLACKROCK_CLAN": {"all": 0.8, "food": 0.6, "plantation": 0.3, "mines": 1.3},
    "BLACKROCK_NORTHSHIRE": {"all": 0.5, "food": 0.5},
    # Allianz- und Horde-Außenposten
    "MARSHTIDE_WATCH": {"all": 1.0},
    "STONARD": {"all": 0.9, "mines": 1.2, "plantation": 0.6},
    "NETHERGARDE_KEEP": {"all": 1.0, "food": 0.7, "mines": 1.3},
    "GROMGOL_BASE": {"all": 0.9},
    "GILNEAS_EXPEDITION": {"all": 0.9},
    "SUNVEIL_EXCURSION": {"all": 0.9},
    "AZEROTH_DEFENDERS": {"all": 0.9},
    "KARAZHAN": {"all": 0.8},
    "KURZEN_COMPOUND": {"all": 0.7},
    "NESINGWARY_EXPEDITION": {"all": 0.8, "building_livestock_ranch": 1.5},
    # Gnolle, Oger, Worgen: Stämme und Banden, wenig Wirtschaft
    "RIVERPAW_PACK": {"all": 0.6},
    "REDGRIDGE_PACK": {"all": 0.6},
    "SPLINTERFIST_CLAN": {"all": 0.6},
    "MOSHOGG_OGRE": {"all": 0.6},
    "DREADMAUL_OGRES": {"all": 0.6, "mines": 1.2},
    "DEADWIND_OGRE": {"all": 0.6},
    "NIGHTBANE_WORGEN": {"all": 0.5},
    "WORMTHORN_CORRUPTION": {"all": 0.4},
    "LOST_ONES": {"all": 0.4},
    # Wasservölker: Fisch statt Acker
    "BLOODSAIL_PIRATES": {"all": 0.8, "fish": 1.8, "food": 0.6},
    "BLOODWASH_NAGA": {"all": 0.6, "fish": 2.0, "food": 0.5},
    "STRANGLETHRON_NAGA": {"all": 0.6, "fish": 2.0, "food": 0.5},
    "MARSHFIN_MURLOC": {"all": 0.5, "fish": 2.5, "food": 0.3},
    "MURKGILL_TRIBE": {"all": 0.5, "fish": 2.5, "food": 0.3},
}

# Zentral-Kalimdor (24): Durotar, Brachland, Mulgore, Desolace, Steinkrallen, Düstermarschen
_ZENTRAL_KALIMDOR = {
    # Hordehauptstadt: karges Durotar, Minen und Kriegswirtschaft, Hafen Orgrimmar/Razor Hill
    "ORGRIMMAR": {"all": 1.3, "food": 0.9, "mines": 1.3, "wood": 0.8, "fish": 1.2},
    # Tauren: Hirtenvolk der Ebenen, achten die Erde (wenig Bergbau)
    "THUNDERBLUFF": {"all": 1.2, "building_livestock_ranch": 1.6, "mines": 0.5, "wood": 0.8},
    "CLIFFWALKER": {"all": 0.8, "building_livestock_ranch": 1.4, "mines": 0.6},
    "GRIMMTOTEM": {"all": 0.7, "building_livestock_ranch": 1.3},
    "BLACKHOOF": {"all": 0.7, "building_livestock_ranch": 1.3},
    "DIREHORN": {"all": 0.7, "building_livestock_ranch": 1.3},
    # Allianz-Hafenstadt der Kul Tiraner unter Jaina
    "THERAMORE": {"all": 1.2, "fish": 1.5, "plantation": 1.2},
    "NORTHWATCH_EXPEDITION": {"all": 0.8, "food": 0.8, "mines": 1.3},
    "HONOR_STAND": {"all": 0.8},
    # Nachtelfen: Wald schonen, kaum Bergbau
    "DARNASSUS": {"all": 1.1, "wood": 0.5, "mines": 0.5},
    "THAL_DARAH": {"all": 0.8, "wood": 0.5, "mines": 0.7},
    "CENARION_CIRCLE": {"all": 0.9, "wood": 0.3, "mines": 0.3},
    "DRUIDS_OF_FANG": {"all": 0.5},
    # Dunkelspeere: Inseltrolle, Fischfang und Dschungelfrüchte
    "DARKSPEAR": {"all": 0.9, "fish": 1.5, "plantation": 1.2},
    "SHADOWPREY": {"all": 0.6, "fish": 1.3},
    # Dämonenkult der Orks: Krieg, Schwefel und Eisen, kaum Landwirtschaft
    "BURNING_BLADE": {"all": 0.7, "food": 0.7, "plantation": 0.3, "mines": 1.2},
    # Schwarzer Drachenschwarm: Hort statt Wirtschaft
    "BLACK_DRAGONFLIGHT_ONYXIA": {"all": 0.4},
    # Goblins
    "SLUDGEWERKS": {"all": 0.8, "food": 0.6, "mines": 1.5, "plantation": 0.5},
    "FRAZZLECRAZ": {"all": 0.7, "mines": 1.5, "food": 0.6},
    # Zwerge von Bael Modan (Minen über den Kulturfaktor)
    "BEAL_DUN": {"all": 0.8},
    # Zentauren: Nomaden, Herden statt Äcker
    "MAROUDINE": {"all": 0.6, "building_livestock_ranch": 1.5},
    "GELKIS": {"all": 0.6, "building_livestock_ranch": 1.5},
    "MAGRAM": {"all": 0.6, "building_livestock_ranch": 1.5},
    # Stachelebern, Gnolle, Kobolde, Harpyien, Satyrn, Oger: Stämme ohne nennenswerte Wirtschaft
    "BRISTLEBACK_QUILBOARS": {"all": 0.6},
    "RAZORFEN": {"all": 0.6},
    "RAZORMANE": {"all": 0.6},
    "PALEMANE_GNOLL": {"all": 0.6},
    "BOULDERSLIDE_KOBOLD": {"all": 0.5, "mines": 1.5},
    "WITCHWING_HARPIE": {"all": 0.4},
    "DUSTWIND_HARPY": {"all": 0.4},
    "WINDFURY_HARPY": {"all": 0.4},
    "HATEFURY_SATYRS": {"all": 0.4},
    "BRACKENWALL": {"all": 0.6},
    # Wasservölker
    "SLITHERBLADE_NAGA": {"all": 0.6, "fish": 2.0, "food": 0.5},
    "STRASHAZ": {"all": 0.6, "fish": 2.0, "food": 0.5},
    "MIREFIN_MURLOC": {"all": 0.5, "fish": 2.5, "food": 0.3},
}

COUNTRIES = {**_SUED_EK, **_ZENTRAL_KALIMDOR}
# Ein Tag darf nur in einer Regionsliste stehen, sonst überschreibt die spätere still die frühere.
_DUP = set(_SUED_EK) & set(_ZENTRAL_KALIMDOR)
if _DUP:
    log.warning("Profil doppelt definiert: %s", sorted(_DUP))

FOOD = ("grain", "building_livestock_ranch")
# Nahrung nie unter diesen Faktor: VA-029 ist eine Hungersnot, schwache Reiche sollen nicht verhungern.
# Schwäche zeigt sich bei Holz, Minen und Plantagen.
FOOD_MIN = 0.8


def group_of(kind):
    """Gebäudeart aus RATES (oder konkretes Gebäude) → Profilgruppe."""
    if kind in FOOD or kind.endswith("_farm"):
        return "food"
    if kind in ("fish", "building_fishing_wharf", "building_whaling_station"):
        return "fish"
    if "plantation" in kind:
        return "plantation"
    if kind == "building_logging_camp":
        return "wood"
    if kind.endswith("_mine"):
        return "mines"
    log.warning("unbekannte Gebäudeart %s, keine Profilgruppe", kind)
    return None


def factor(profile, kind):
    if not profile:
        return 1.0
    f = profile.get("all", 1.0) * profile.get(kind, 1.0)
    g = group_of(kind)
    f = f * profile.get(g, 1.0) if g else f
    return max(f, FOOD_MIN) if g == "food" else f


def country_factor(tag, kind):
    return factor(COUNTRIES.get(tag), kind)


def culture_factor(r, kind):
    """Kulturfaktor eines States (größter, wenn mehrere Profil-Kulturen vorkommen)."""
    return max((factor(CULTURES[c], kind) for c in r["cultures"] if c in CULTURES), default=1.0)


def state_factor(r, kind):
    """Faktor eines States: Länder nach Pop-Anteil gemittelt, mal Kulturfaktor."""
    owners = r["owners"]
    total = sum(owners.values())
    f = sum(n * country_factor(t, kind) for t, n in owners.items()) / total if total else 1.0
    return f * culture_factor(r, kind)
