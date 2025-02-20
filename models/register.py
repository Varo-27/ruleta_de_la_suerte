import json
from textwrap import wrap
from pathlib import Path
class Register:
    panel_path: Path

    def __init__(self):
        root_dir = Path(__file__).resolve().parent.parent
        self.panel_path = root_dir / "data" / "paneles.json"

    def next_id(self, file_data: dict) -> str:
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

    def format_hint(self, hint: str) -> str | None:
        hint = hint.lower().strip()
        if len(hint) > 30 or len(hint) < 5:
            return None
        return hint

    def entry_generator(self, phrase: str, hint: str) -> None:
        with open(self.panel_path, "r", encoding="utf-8") as file:
            file_data = json.load(file)

        for entry_id in file_data:
            if file_data[entry_id]["phrase"] == phrase:
                raise ValueError("La frase ya existe en el registro")
            elif file_data[entry_id]["hint"] == hint:
                raise ValueError("La pista ya existe en el registro")

        new_id = self.next_id(file_data)
        new_entry = { new_id : {
                        "phrase": phrase,
                        "hint": hint
                        }
                    }

        file_data.update(new_entry)
        with open(self.panel_path, "w", encoding="utf-8") as file:
            json.dump(file_data, file, indent=4)
