import json
from textwrap import wrap
from pathlib import Path
class Register:

    def next_id(self) -> str:
        root_dir = Path(__file__).resolve().parent.parent
        panel_path = root_dir / "data" / "paneles.json"
        with open(panel_path, "r") as file:
            file_data = json.load(file)

        id_list = list(file_data.keys())
        last_id = id_list[-1]
        next_id = str("id" + str(int(last_id[2:]) + 1))
        return next_id

    def format_phrase(self,phrase: str) -> str|None:
        phrase = phrase.lower().strip()
        phrase_lines = wrap(phrase, 14)
        if len(phrase_lines) > 4 or len(phrase) < 5:
            return None
        return phrase

    def format_hint(self, hint: str) -> str:
        hint = hint.lower().strip()
        if len(hint) > 30 or len(hint) < 5:
            return None
        return hint

    def entry_generator(self, phrase: str, hint: str) -> None:
        with open("paneles.json", "r") as file:
            file_data = json.load(file)

        for id in file_data:
            if file_data[id]["phrase"] == phrase:
                raise ValueError("La frase ya existe en el registro")
            elif file_data[id]["hint"] == hint:
                raise ValueError("La pista ya existe en el registro")

        new_id = self.next_id()
        new_entry = { new_id : {
                        "phrase": phrase,
                        "hint": hint
                        }
                    }

        file_data.update(new_entry)
        with open("paneles.json", "w") as file:
            json.dump(file_data, file, indent=4)
