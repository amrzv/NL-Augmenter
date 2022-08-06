"""This list comes from appendix of https://arxiv.org/pdf/1807.11714.pdf

It was extended with two possessive pronouns: 'his' and 'her'.
"""

GENDER_PAIRS = {
    "gods": "goddesses",
    "manager": "manageress",
    "barons": "baronesses",
    "nephew": "niece",
    "prince": "princess",
    "boars": "sows",
    "baron": "baroness",
    "stepfathers": "stepmothers",
    "wizard": "witch",
    "father": "mother",
    "stepsons": "stepdaughters",
    "sons-in-law": "daughters-in-law",
    "dukes": "duchesses",
    "boyfriend": "girlfriend",
    "fiances": "fiancees",
    "dad": "mom",
    "shepherd": "shepherdess",
    "uncles": "aunts",
    "beau": "belle",
    "males": "females",
    "hunter": "huntress",
    "beaus": "belles",
    "grandfathers": "grandmothers",
    "lads": "lasses",
    "daddies": "mummies",
    "step-son": "step-daughter",
    "masters": "mistresses",
    "policeman": "policewoman",
    "nephews": "nieces",
    "brother": "sister",
    "grandfather": "grandmother",
    "priest": "priestess",
    "hosts": "hostesses",
    "landlord": "landlady",
    "husband": "wife",
    "poet": "poetess",
    "landlords": "landladies",
    "fathers": "mothers",
    "masseur": "masseuse",
    "monks": "nuns",
    "usher": "usherette",
    "hero": "heroine",
    "stepson": "stepdaughter",
    "postman": "postwoman",
    "god": "goddess",
    "milkmen": "milkmaids",
    "stags": "hinds",
    "grandpa": "grandma",
    "chairmen": "chairwomen",
    "husbands": "wives",
    "grandpas": "grandmas",
    "stewards": "stewardesses",
    "murderer": "murderess",
    "manservant": "maidservant",
    "men": "women",
    "host": "hostess",
    "heirs": "heiresses",
    "masseurs": "masseuses",
    "boy": "girl",
    "male": "female",
    "son-in-law": "daughter-in-law",
    "waiter": "waitress",
    "tutors": "governesses",
    "priests": "priestesses",
    "bachelor": "spinster",
    "millionaire": "millionairess",
    "steward": "stewardess",
    "businessmen": "businesswomen",
    "congressman": "congresswoman",
    "emperor": "empress",
    "duke": "duchess",
    "sire": "dam",
    "son": "daughter",
    "sirs": "madams",
    "widower": "widow",
    "kings": "queens",
    "papas": "mamas",
    "grandsons": "granddaughters",
    "proprietor": "proprietress",
    "monk": "nun",
    "headmasters": "headmistresses",
    "grooms": "brides",
    "heir": "heiress",
    "boys": "girls",
    "gentleman": "lady",
    "uncle": "aunt",
    "he": "she",
    "king": "queen",
    "princes": "princesses",
    "policemen": "policewomen",
    "governor": "matron",
    "fiance": "fiancee",
    "step-father": "step-mother",
    "waiters": "waitresses",
    "mr": "mrs",
    "stepfather": "stepmother",
    "daddy": "mummy",
    "lords": "ladies",
    "widowers": "widows",
    "emperors": "empresses",
    "father-in-law": "mother-in-law",
    "abbot": "abbess",
    "sir": "madam",
    "actor": "actress",
    "mr.": "mrs.",
    "wizards": "witches",
    "actors": "actresses",
    "chairman": "chairwoman",
    "sorcerer": "sorceress",
    "postmaster": "postmistress",
    "brothers": "sisters",
    "lad": "lass",
    "headmaster": "headmistress",
    "papa": "mama",
    "milkman": "milkmaid",
    "heroes": "heroines",
    "man": "woman",
    "grandson": "granddaughter",
    "groom": "bride",
    "sons": "daughters",
    "congressmen": "congresswomen",
    "businessman": "businesswoman",
    "boyfriends": "girlfriends",
    "dads": "moms",
    "goddesses": "gods",
    "manageress": "manager",
    "baronesses": "barons",
    "niece": "nephew",
    "princess": "prince",
    "sows": "boars",
    "baroness": "baron",
    "stepmothers": "stepfathers",
    "witch": "wizard",
    "mother": "father",
    "stepdaughters": "stepsons",
    "daughters-in-law": "sons-in-law",
    "duchesses": "dukes",
    "girlfriend": "boyfriend",
    "fiancees": "fiances",
    "mom": "dad",
    "shepherdess": "shepherd",
    "aunts": "uncles",
    "belle": "beau",
    "females": "males",
    "huntress": "hunter",
    "belles": "beaus",
    "grandmothers": "grandfathers",
    "lasses": "lads",
    "mummies": "daddies",
    "step-daughter": "step-son",
    "mistresses": "masters",
    "policewoman": "policeman",
    "nieces": "nephews",
    "sister": "brother",
    "grandmother": "grandfather",
    "priestess": "priest",
    "hostesses": "hosts",
    "landlady": "landlord",
    "wife": "husband",
    "poetess": "poet",
    "landladies": "landlords",
    "mothers": "fathers",
    "masseuse": "masseur",
    "nuns": "monks",
    "usherette": "usher",
    "heroine": "hero",
    "stepdaughter": "stepson",
    "postwoman": "postman",
    "goddess": "god",
    "milkmaids": "milkmen",
    "hinds": "stags",
    "grandma": "grandpa",
    "chairwomen": "chairmen",
    "wives": "husbands",
    "grandmas": "grandpas",
    "stewardesses": "stewards",
    "murderess": "murderer",
    "maidservant": "manservant",
    "women": "men",
    "hostess": "host",
    "heiresses": "heirs",
    "masseuses": "masseurs",
    "girl": "boy",
    "female": "male",
    "daughter-in-law": "son-in-law",
    "waitress": "waiter",
    "governesses": "tutors",
    "priestesses": "priests",
    "spinster": "bachelor",
    "millionairess": "millionaire",
    "stewardess": "steward",
    "businesswomen": "businessmen",
    "congresswoman": "congressman",
    "empress": "emperor",
    "duchess": "duke",
    "dam": "sire",
    "daughter": "son",
    "madams": "sirs",
    "widow": "widower",
    "queens": "kings",
    "mamas": "papas",
    "granddaughters": "grandsons",
    "proprietress": "proprietor",
    "nun": "monk",
    "headmistresses": "headmasters",
    "brides": "grooms",
    "heiress": "heir",
    "girls": "boys",
    "lady": "gentleman",
    "aunt": "uncle",
    "she": "he",
    "queen": "king",
    "princesses": "princes",
    "policewomen": "policemen",
    "matron": "governor",
    "fiancee": "fiance",
    "step-mother": "step-father",
    "waitresses": "waiters",
    "mrs": "mr",
    "stepmother": "stepfather",
    "mummy": "daddy",
    "ladies": "lords",
    "widows": "widowers",
    "empresses": "emperors",
    "mother-in-law": "father-in-law",
    "abbess": "abbot",
    "madam": "sir",
    "actress": "actor",
    "mrs.": "mr.",
    "witches": "wizards",
    "actresses": "actors",
    "chairwoman": "chairman",
    "sorceress": "sorcerer",
    "postmistress": "postmaster",
    "sisters": "brothers",
    "lass": "lad",
    "headmistress": "headmaster",
    "mama": "papa",
    "milkmaid": "milkman",
    "heroines": "heroes",
    "woman": "man",
    "granddaughter": "grandson",
    "bride": "groom",
    "daughters": "sons",
    "congresswomen": "congressmen",
    "businesswoman": "businessman",
    "girlfriends": "boyfriends",
    "moms": "dads",
    "his": "her",  # Added
    "her": "his",  # Added
}