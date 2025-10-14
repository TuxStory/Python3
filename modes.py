def get_mode_notes(mode, root_note):
    # Définition des intervalles pour chaque mode
    modes_intervals = {
        "ionien": [2, 2, 1, 2, 2, 2, 1],  # Majeur
        "dorien": [2, 1, 2, 2, 2, 1, 2],
        "phrygien": [1, 2, 2, 2, 1, 2, 2],
        "lydien": [2, 2, 2, 1, 2, 2, 1],
        "mixolydien": [2, 2, 1, 2, 2, 1, 2],
        "éolien": [2, 1, 2, 2, 1, 2, 2],  # Mineur naturel
        "locrien": [1, 2, 2, 1, 2, 2, 2]
    }

    # Notes de la gamme chromatique
    notes = ["Do", "Do♯", "Ré", "Ré♯", "Mi", "Fa", "Fa♯", "Sol", "Sol♯", "La", "La♯", "Si"]

    if mode in modes_intervals and root_note in notes:
        # Trouver l'index de la note fondamentale
        root_index = notes.index(root_note)
        mode_notes = []

        # Générer les notes du mode en fonction des intervalles
        for interval in modes_intervals[mode]:
            mode_notes.append(notes[root_index % len(notes)])
            root_index += interval

        return mode_notes
    else:
        return None

def main():
    mode = input("Entrez le mode (ionien, dorien, phrygien, lydien, mixolydien, éolien, locrien) : ").lower()
    root_note = input("Entrez la note fondamentale (Do, Do♯, Ré, Ré♯, Mi, Fa, Fa♯, Sol, Sol♯, La, La♯, Si) : ").capitalize()

    notes = get_mode_notes(mode, root_note)

    if notes:
        print(f"Les notes du mode {mode} à partir de {root_note} sont : {', '.join(notes)}")
    else:
        print("Mode ou note fondamentale invalide.")

if __name__ == "__main__":
    main()

