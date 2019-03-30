import re

import jellyfish as jellyfish


class DescriptionService:

    def jaro_winkler_distance(self, expected, actual):
        # problem: case sensitive!!!
        return jellyfish.jaro_winkler(expected, actual)

    def find_numeric_info(self, description_list, index):
        i = 1
        while i < 3 and (index - i) >= 0 and (index + i) < len(description_list):
            nr_found1 = re.sub("[^0-9]", "", description_list[index - i])
            nr_found2 = re.sub("[^0-9]", "", description_list[index + i])

            if len(nr_found1) > 0:
                return nr_found1
            if len(nr_found2) > 0:
                return nr_found2
            i = i + 1
        return None

    def find_values(self, description_list, description_dictionary):
        result = {'nr_camere': None,
                  'suprafata': None,
                  'etajul': None,
                  'pret': None}
        for key, value in description_dictionary.items():
            value_found = self.find_numeric_info(description_list, value[2])
            result[key] = value_found

        return result

    def get_description_info(self, description):
        description = description.lower().replace(',', ' ')
        description_list = description.split(' ')

        description_dictionary = {'nr_camere': ["", 0, -1],
                                  'suprafata': ["", 0, -1],
                                  'etajul': ["", 0, -1],
                                  'pret': ["", 0, -1]}
        key_solver_dictionary = {'nr_camere': ["camere", "cam"],
                                 'suprafata': ["suprafata", "mp", "metri patrati"],
                                 'etajul': ["etajul", "et"],
                                 'pret': ["pret", "pretul"]}
        i = 0
        for word in description_list:
            for key, value in key_solver_dictionary.items():
                for elem in value:
                    dist = self.jaro_winkler_distance(elem, word)
                    if dist > 0.75 and description_dictionary[key][1] < dist:
                        description_dictionary[key][0] = word
                        description_dictionary[key][1] = dist
                        description_dictionary[key][2] = i
            i = i + 1
        return self.find_values(description_list, description_dictionary)
