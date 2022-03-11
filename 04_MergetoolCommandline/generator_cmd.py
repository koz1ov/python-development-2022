import cmd

import pynames


class GeneratorCmd(cmd.Cmd):
    prompt = '> '
    lang = pynames.LANGUAGE.NATIVE
    

    GENERATORS = {
        'scandinavian': pynames.generators.scandinavian.ScandinavianNamesGenerator(),
        'russian': pynames.generators.russian.PaganNamesGenerator(),
        'mongolian': pynames.generators.mongolian.MongolianNamesGenerator(),
        'korean': pynames.generators.korean.KoreanNamesGenerator(),
        'goblins': pynames.generators.goblin.GoblinGenerator(),
        'orcs': pynames.generators.orc.OrcNamesGenerator(),

        'elven': {
            'warhammer': pynames.generators.elven.WarhammerNamesGenerator(),
            'dnd': pynames.generators.elven.DnDNamesGenerator(),
        },

        'iron_kingdoms': {
            'gobber': pynames.generators.iron_kingdoms.GobberFullnameGenerator(),
            'thurian': pynames.generators.iron_kingdoms.ThurianFullnameGenerator(),
            'morridane': pynames.generators.iron_kingdoms.MorridaneFullnameGenerator(),
            'tordoran': pynames.generators.iron_kingdoms.TordoranFullnameGenerator(),
            'ryn': pynames.generators.iron_kingdoms.RynFullnameGenerator(),
            'dwarf': pynames.generators.iron_kingdoms.DwarfFullnameGenerator(),
            'iossan_nyss': pynames.generators.iron_kingdoms.IossanNyssFullnameGenerator(),
            'caspian_midlunder_sulese': pynames.generators.iron_kingdoms.CaspianMidlunderSuleseFullnameGenerator(),
            'khadoran': pynames.generators.iron_kingdoms.KhadoranFullnameGenerator(),
            'ogrun': pynames.generators.iron_kingdoms.OgrunFullnameGenerator(),
            'trollkin': pynames.generators.iron_kingdoms.TrollkinFullnameGenerator(),
        }
    }

    GENDERS = {
        'male': pynames.GENDER.MALE,
        'female': pynames.GENDER.FEMALE,
    }

    def do_language(self, lang):

        lang = lang.lower()
        if lang in pynames.LANGUAGE.ALL:
            self.lang = lang
        else:
            print(f'sorry, language must be one of '
                  f'{", ".join(s.upper() for s in pynames.LANGUAGE.ALL)}"')

    def complete_language(self, text, line, begidx, endidx):
        return [lang for lang in pynames.LANGUAGE.ALL if lang.startswith(text)] 
        
    def do_info(self, args):
        
        args = args.split()
        race = args[0] if args else None
        arg_idx = 1

        if race not in self.GENERATORS:
            print("No such race")
            return

        if isinstance(self.GENERATORS[race], dict):
            if len(args) < 2:
                print("No subclass chosen")
                return

            race_dict = self.GENERATORS[race]

            if args[1] not in race_dict:
                print("No such subclass")
                return

            gen = race_dict[args[arg_idx]]
            arg_idx = 2
        else:
            gen = self.GENERATORS[race]

        next_arg = args[arg_idx] if arg_idx < len(args) else None
        if next_arg == 'language':
            print(*gen.languages)
        else:
            gender = self.GENDERS.get(next_arg, pynames.GENDER.ALL)
            print(gen.get_names_number(gender))

    def complete_info(self, text, line, begidx, endidx):

        args = line[:begidx].split()
        if len(args) == 1:
            return [race for race in self.GENERATORS if race.startswith(text)]
        
        has_subclass = isinstance(self.GENERATORS.get(args[1]), dict)
        if len(args) == 2 and has_subclass:
            return [subclass for subclass in self.GENERATORS[args[1]] if subclass.startswith(text)]

        if len(args) == 2 and not has_subclass or len(args) == 3 and has_subclass:
            return [suggest for suggest in ['male', 'female', 'language'] if suggest.startswith(text)]

    def complete_generate(self, text, line, begidx, endidx):

        args = line[:begidx].split()
        if len(args) == 1:
            return [race for race in self.GENERATORS if race.startswith(text)]

        has_subclass = isinstance(self.GENERATORS.get(args[1]), dict)

        suggests = []
        if len(args) == 2 or len(args) == 3 and has_subclass and args[2] in self.GENERATORS[args[1]].keys():
            suggests = list(self.GENDERS.keys())
        if len(args) == 2 and has_subclass:
            suggests += list(self.GENERATORS[args[1]].keys())
        return [suggest for suggest in suggests if suggest.startswith(text)]

    def do_generate(self, args):

        pass

GeneratorCmd().cmdloop()
