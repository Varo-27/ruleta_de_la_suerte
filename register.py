import json

class Register:

    def next_id(self) -> str:
        with open("paneles.json", "r") as file:
            file_data = json.load(file)

        id_list = list(file_data.keys())
        last_id = id_list[-1]
        next_id = str("id" + str(int(last_id[2:]) + 1))
        return next_id

    def pick_phrase(self) -> str|None:
        phrase = "Prueba de frase"
        
        
        return phrase.strip()


    def pick_hint(self) -> str:
        return "frase prueba numero cuatro"

    def entry_generator(self):
        with open("paneles.json", "r") as file:
            file_data = json.load(file)

        id = self.next_id()
        phrase = self.pick_phrase()
        hint = self.pick_hint()
        new_entry = { id : {
                        "frase": phrase,
                        "pista": hint
                        }
                    }

        file_data.update(new_entry)
        with open("paneles.json", "w") as file:
            json.dump(file_data, file, indent=4)


if __name__ == "__main__":
    r = Register()
    r.entry_generator()
