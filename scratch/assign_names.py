# -*- coding: utf-8 -*-
"""
Client Name Assignment & Validation Module.
Maps raw cropped card indexes (0 to 98) from the presentation slides to exact Brand Names.
"""

import os
import json
from typing import Dict, List, Tuple

# Default canonical in-code mapping (Index 0-98 -> Brand Name)
DEFAULT_NAMES: Dict[int, str] = {
    # Part 1: Slide 1 (Rows 0-5 x 9 Cols = Index 0-53)
    0: "Aarts Industries",
    1: "ABB",
    2: "Aditya Birla",
    3: "Adani",
    4: "Alembic",
    5: "Ajanta Pharma",
    6: "Anoopam Mission",
    7: "Apollo Hospitals",
    8: "Apothecon Pharmaceuticals",
    9: "Armein Pharmaceuticals",
    10: "ATE",
    11: "Arkel",
    12: "Anupam",
    13: "Aadicura Super Speciality Hospital",
    14: "Anant National University",
    15: "Agni Solar / Agni",
    16: "Atul",
    17: "Borosil Renewables",
    18: "Bhalakia University / Bhalakia",
    19: "Baroda Dairy",
    20: "CGSM",
    21: "Cipla",
    22: "CHARUSAT",
    23: "DLFA",
    24: "Echjay Industries",
    25: "Elecon",
    26: "Elmex",
    27: "Epoxy House",
    28: "ERDA",
    29: "FMC",
    30: "Flint Group",
    31: "GACL (Gujarat Alkalies and Chemicals)",
    32: "Gala",
    33: "GCPL (Gujarat Chemical Port / Godrej)",
    34: "Gandhi Special Tubes",
    35: "GGRC (Gujarat Green Revolution Company)",
    36: "Encube Ethicals",
    37: "JSW Steel",
    38: "KSP",
    39: "KP Group",
    40: "KPGU Vadodara",
    41: "INEOS",
    42: "INOX-GSP / INOX",
    43: "Indian Oil (IOCL)",
    44: "MetTube",
    45: "Meghmani Group",
    46: "National Foods",
    47: "NJ Group",
    48: "Larsen & Toubro (L&T)",
    49: "OPAL (ONGC Petro additions)",
    50: "ORBIT / Oerlikon",
    51: "Pakona Engineers",
    52: "Toyo Engineering",
    53: "Sardar Sarovar Narmada Nigam (SSNNL)",

    # Part 2: Slide 2 (Rows 0-4 x 9 Cols = Index 54-98)
    54: "Amneal Pharmaceuticals",
    55: "Banco",
    56: "Deepak Nitrite / Phenolics",
    57: "Gujarat Metal Cast",
    58: "GETCO",
    59: "GNFC",
    60: "GSRTC",
    61: "GSP Crop Science",
    62: "MGVCL",
    63: "Paramount Enterprises (PE)",
    64: "Pragati Glass",
    65: "Polycab",
    66: "Reliance Industries",
    67: "Shannen International School",
    68: "Shaily Engineering Plastics",
    69: "Silox",
    70: "Sudeep Pharma",
    71: "Shiva Pharmachem",
    72: "Signify",
    73: "Sintex",
    74: "Sisecam",
    75: "Unaty",
    76: "United Phosphorus (UPL)",
    77: "Sun Pharma",
    78: "Tara Suns",
    79: "Torrent Power",
    80: "TTK Prestige",
    81: "Pratibha Elecinfra",
    82: "Vedanta",
    83: "NDDB Dairy Services",
    84: "Central Warehousing Corporation",
    85: "UPL (United Phosphorus Limited)",
    86: "Utopia",
    87: "VCCI",
    88: "Welcare Hospital",
    89: "Welspun",
    90: "Indian Air Force (IAF)",
    91: "Western Railway",
    92: "Vadodara City Police",
    93: "Central Industrial Security Force (CISF)",
    94: "Vadodara Municipal Corporation (VMC)",
    95: "Government of India / Gujarat",
    96: "Gujarat Police",
    97: "Railway Protection Force / Police",
    98: "Zydus Cadila",
}

def load_names_from_json(json_path: str = "c:/nimit/data/client_names.json") -> Dict[int, str]:
    """Loads name mapping from data/client_names.json if available, or returns DEFAULT_NAMES."""
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {int(k): str(v) for k, v in data.items()}
        except Exception:
            pass
    return dict(DEFAULT_NAMES)

def save_names_to_json(mapping: Dict[int, str], json_path: str = "c:/nimit/data/client_names.json") -> None:
    """Exports the name mapping back to JSON format."""
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in sorted(mapping.items())}, f, indent=2, ensure_ascii=False)

# Backward-compatible global dictionary imported by other scripts
names: Dict[int, str] = load_names_from_json()

def get_client_name(idx: int, default: str = "") -> str:
    """Returns the brand name for the given crop index (0-98)."""
    return names.get(idx, default or f"Client #{idx:02d}")

def get_sorted_clients() -> List[Tuple[int, str]]:
    """Returns a list of (index, name) tuples sorted alphabetically A-to-Z."""
    return sorted(names.items(), key=lambda item: item[1].lower())

def validate_mapping(expected_count: int = 99) -> bool:
    """Debug and validate integrity of the name mappings."""
    print("=" * 60)
    print("  CLIENT BRAND NAME MAPPING DIAGNOSTICS")
    print("=" * 60)
    
    total = len(names)
    print(f"[*] Total entries mapped: {total} / {expected_count}")

    # Check for missing indices
    missing = [i for i in range(expected_count) if i not in names]
    if missing:
        print(f"[-] WARNING: Missing crop indices: {missing}")
    else:
        print("[+] All indices 0 to 98 are present with no gaps.")

    # Check for empty or placeholder names
    empty_entries = [i for i, n in names.items() if not n or not n.strip()]
    if empty_entries:
        print(f"[-] WARNING: Empty names found for indices: {empty_entries}")
    else:
        print("[+] No empty or blank names found.")

    # Check for duplicate names
    name_occurrences: Dict[str, List[int]] = {}
    for idx, name_str in names.items():
        name_occurrences.setdefault(name_str.strip().lower(), []).append(idx)
    
    duplicates = {k: v for k, v in name_occurrences.items() if len(v) > 1}
    if duplicates:
        print(f"[!] Info: Found {len(duplicates)} duplicate/repeated brand references:")
        for name_key, idxs in duplicates.items():
            print(f"    - \"{names[idxs[0]]}\" at indices: {idxs}")
    else:
        print("[+] All 99 brand names are unique.")

    sorted_list = get_sorted_clients()
    print("-" * 60)
    print(f"[+] Alphabetical Range: '{sorted_list[0][1]}' -> '{sorted_list[-1][1]}'")
    print("=" * 60)
    return len(missing) == 0 and len(empty_entries) == 0

if __name__ == "__main__":
    is_valid = validate_mapping(99)
    # Ensure JSON stays in sync
    save_names_to_json(names)
    print(f"Total mapped: {len(names)} names.")
