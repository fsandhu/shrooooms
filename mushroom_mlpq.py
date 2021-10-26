__author__ = 'Justin Lang'


# Justin Lang, Sarah Roscoe, Oleksiy Al-saadi, Fateh Sandhu
# CSCE 413/813 - Database Systems
# Program for converting mushroom dataset to MLPQ-readable file

class Mushroom():

    def __init__(self, classification, cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment, gill_spacing,
                 gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring,
                 stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type,
                 spore_print_color, population, habitat):
        self.classification = classification
        self.cap_shape = cap_shape
        self.cap_surface = cap_surface
        self.cap_color = cap_color
        self.bruises = bruises
        self.odor = odor
        self.gill_attachment = gill_attachment
        self.gill_spacing = gill_spacing
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_shape = stalk_shape
        self.stalk_root = stalk_root
        self.stalk_surface_above_ring = stalk_surface_above_ring
        self.stalk_surface_below_ring = stalk_surface_below_ring
        self.stalk_color_above_ring = stalk_color_above_ring
        self.stalk_color_below_ring = stalk_color_below_ring
        self.veil_type = veil_type
        self.veil_color = veil_color
        self.ring_number = ring_number
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        self.population = population
        self.habitat = habitat

    def set_classification(self, new_class):
        self.classification = new_class

    def get_classification(self):
        return self.classification

    def set_cap_shape(self, new_cap_shape):
        self.cap_shape = new_cap_shape

    def get_cap_shape(self):
        return self.cap_shape

    def set_cap_surface(self, new_surface):
        self.cap_surface = new_surface

    def get_cap_surface(self):
        return self.cap_surface

    def set_cap_color(self, new_color):
        self.cap_color = new_color

    def get_cap_color(self):
        return self.cap_color

    def set_bruises(self, condition):
        self.bruises = condition

    def get_bruises(self):
        return self.bruises

    def set_odor(self, odor):
        self.odor = odor

    def get_odor(self):
        return self.odor

    def set_gill_attachment(self, attachment):
        self.gill_attachment = attachment

    def get_gill_attachment(self):
        return self.gill_attachment

    def set_gill_spacing(self, spacing):
        self.gill_spacing = spacing

    def get_gill_spacing(self):
        return self.gill_spacing

    def set_gill_size(self, size):
        self.gill_size = size

    def get_gill_size(self):
        return self.gill_size

    def set_gill_color(self, color):
        self.gill_color = color

    def get_gill_color(self):
        return self.gill_color

    def set_stalk_shape(self, shape):
        self.stalk_shape = shape

    def get_stalk_shape(self):
        return self.stalk_shape

    def set_stalk_root(self, root):
        self.stalk_root = root

    def get_stalk_root(self):
        return self.stalk_root

    def set_stalk_surface_above_ring(self, surface):
        self.stalk_surface_above_ring = surface

    def get_stalk_surface_above_ring(self):
        return self.stalk_surface_above_ring

    def set_stalk_surface_below_ring(self, surface):
        self.stalk_surface_below_ring = surface

    def get_stalk_surface_below_ring(self):
        return self.stalk_surface_below_ring

    def set_stalk_color_above_ring(self, color):
        self.stalk_color_above_ring = color

    def get_stalk_color_above_ring(self):
        return self.stalk_color_above_ring

    def set_stalk_color_below_ring(self, color):
        self.stalk_color_below_ring = color

    def get_stalk_color_below_ring(self):
        return self.stalk_color_below_ring

    def set_veil_type(self, type):
        self.veil_type = type

    def get_veil_type(self):
        return self.veil_type

    def set_veil_color(self, color):
        self.veil_color = color

    def get_veil_color(self):
        return self.veil_color

    def set_ring_number(self, number):
        self.ring_number = number

    def get_ring_number(self):
        return self.ring_number

    def set_ring_type(self, type):
        self.ring_type = type

    def get_ring_type(self):
        return self.ring_type

    def set_spore_print_color(self, color):
        self.spore_print_color = color

    def get_spore_print_color(self):
        return self.spore_print_color

    def set_population(self, population):
        self.population = population

    def get_population(self):
        return self.population

    def set_habitat(self, habitat):
        self.habitat = habitat

    def get_habitat(self):
        return self.habitat

    def __str__(self):
        return (self.classification + " " +
                self.cap_shape + " " +
                self.cap_surface + " " +
                self.cap_color + " " +
                self.bruises + " " +
                self.odor + " " +
                self.gill_attachment + " " +
                self.gill_spacing + " " +
                self.gill_size + " " +
                self.gill_color + " " +
                self.stalk_shape + " " +
                self.stalk_root + " " +
                self.stalk_surface_above_ring + " " +
                self.stalk_surface_below_ring + " " +
                self.stalk_color_above_ring + " " +
                self.stalk_color_below_ring + " " +
                self.veil_type + " " +
                self.veil_color + " " +
                self.ring_number + " " +
                self.ring_type + " " +
                self.spore_print_color + " " +
                self.population + " " +
                self.habitat)


mushroom_data_names = {'classification': {'e': 'edible', 'p': 'poisonous'},
                       'cap_shape': {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 'k': 'knobbed',
                                     's': 'sunken'},
                       'cap_surface': {'f': 'fibrous', 'g': 'grooves', 'y': 'scaly', 's': 'smooth'},
                       'cap_color': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'r': 'green', 'p': 'pink',
                                     'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'},
                       'bruises': {'t': 'yes', 'f': 'no'},
                       'odor': {'a': 'almond', 'l': 'anise', 'c': 'creosote', 'y': 'fishy', 'f': 'foul', 'm': 'musty',
                                'n': 'none', 'p': 'pungent', 's': 'spicy'},
                       'gill_attachment': {'a': 'attached', 'd': 'descending', 'f': 'free', 'n': 'notched'},
                       'gill_spacing': {'c': 'close', 'w': 'crowded', 'd': 'distant'},
                       'gill_size': {'b': 'broad', 'n': 'narrow'},
                       'gill_color': {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'g': 'gray',
                                      'r': 'green', 'o': 'orange', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white',
                                      'y': 'yellow'},
                       'stalk_shape': {'e': 'enlarging', 't': 'tapering'},
                       'stalk_root': {'b': 'bulbous', 'c': 'club', 'u': 'cup', 'e': 'equal',
                                      'z': 'rhizomorphs', 'r': 'rooted', '?': 'missing'},
                       'stalk_surface_above_ring': {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'},
                       'stalk_surface_below_ring': {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'},
                       'stalk_color_above_ring': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray',
                                                  'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'},
                       'stalk_color_below_ring': {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray',
                                                  'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'},
                       'veil_type': {'p': 'partial', 'u': 'universal'},
                       'veil_color': {'n': 'brown', 'o': 'orange', 'w': 'white', 'y': 'yellow'},
                       'ring_number': {'n': 'none', 'o': 'one', 't': 'two'},
                       'ring_type': {'c': 'cobwebby', 'e': 'evanescent', 'f': 'flaring', 'l': 'large',
                                     'n': 'none', 'p': 'pendant', 's': 'sheathing', 'z': 'zone'},
                       'spore_print_color': {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'r': 'green',
                                             'o': 'orange', 'u': 'purple', 'w': 'white',
                                             'y': 'yellow'},
                       'population': {'a': 'abundant', 'c': 'clustered', 'n': 'numerous', 's': 'scattered',
                                      'v': 'several', 'y': 'solitary'},
                       'habitat': {'g': 'grasses', 'l': 'leaves', 'm': 'meadows',
                                   'p': 'paths', 'u': 'urban', 'w': 'waste', 'd': 'woods'}}

# def expand_datanames():
#     file = open('agaricus-lepiota.data', "r", encoding="utf8")
#     for line in file:
#         record = line.split(',')

shrooms = []
infile = open('agaricus-lepiota.data', "r", encoding="utf8")
for line in infile:
    line = line.strip()
    r = line.split(',')
    r[0] = mushroom_data_names.get('classification').get(r[0])
    r[1] = mushroom_data_names.get('cap_shape').get(r[1])
    r[2] = mushroom_data_names.get('cap_surface').get(r[2])
    r[3] = mushroom_data_names.get('cap_color').get(r[3])
    r[4] = mushroom_data_names.get('bruises').get(r[4])
    r[5] = mushroom_data_names.get('odor').get(r[5])
    r[6] = mushroom_data_names.get('gill_attachment').get(r[6])
    r[7] = mushroom_data_names.get('gill_spacing').get(r[7])
    r[8] = mushroom_data_names.get('gill_size').get(r[8])
    r[9] = mushroom_data_names.get('gill_color').get(r[9])
    r[10] = mushroom_data_names.get('stalk_shape').get(r[10])
    r[11] = mushroom_data_names.get('stalk_root').get(r[11])
    r[12] = mushroom_data_names.get('stalk_surface_above_ring').get(r[12])
    r[13] = mushroom_data_names.get('stalk_surface_below_ring').get(r[13])
    r[14] = mushroom_data_names.get('stalk_color_above_ring').get(r[14])
    r[15] = mushroom_data_names.get('stalk_color_below_ring').get(r[15])
    r[16] = mushroom_data_names.get('veil_type').get(r[16])
    r[17] = mushroom_data_names.get('veil_color').get(r[17])
    r[18] = mushroom_data_names.get('ring_number').get(r[18])
    r[19] = mushroom_data_names.get('ring_type').get(r[19])
    r[20] = mushroom_data_names.get('spore_print_color').get(r[20])
    r[21] = mushroom_data_names.get('population').get(r[21])
    r[22] = mushroom_data_names.get('habitat').get(r[22])
    m = Mushroom(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15],
                 r[16], r[17], r[18], r[19], r[20], r[21], r[22])
    # print(m)
    shrooms.append(m)

outfile = open('mushrooms_mlpq.txt', 'w', encoding='utf8')
print("begin %MLPQ%", file=outfile)
for mushroom in shrooms:
    print("Mushrooms(classification,cap_shape,cap_surface,cap_color,bruises,odor,gill_attachment,gill_spacing, "
          "gill_size,gill_color,stalk_shape,stalk_root,stalk_surface_above_ring,stalk_surface_below_ring, "
          "stalk_color_above_ring,stalk_color_below_ring,veil_type,veil_color,ring_number,ring_type, "
          "spore_print_color,population,habitat) :- classification=\"%s\", cap_shape=\"%s\", "
          "cap_surface=\"%s\", cap_color=\"%s\", bruises=\"%s\", odor=\"%s\", gill_attachment=\"%s\", "
          "gill_spacing=\"%s\", gill_size=\"%s\", gill_color=\"%s\", stalk_shape=\"%s\", stalk_root=\"%s\", "
          "stalk_surface_above_ring=\"%s\", stalk_surface_below_ring=\"%s\", stalk_color_above_ring=\"%s\", "
          "stalk_color_below_ring=\"%s\", veil_type=\"%s\", veil_color=\"%s\", ring_number=\"%s\", "
          "ring_type=\"%s\", spore_print_color=\"%s\", population=\"%s\", habitat=\"%s\"." % (
              mushroom.get_classification(), mushroom.get_cap_shape(), mushroom.get_cap_surface(),
              mushroom.get_cap_color(),
              mushroom.get_bruises(), mushroom.get_odor(), mushroom.get_gill_attachment(), mushroom.get_gill_size(),
              mushroom.get_gill_size(), mushroom.get_gill_color(), mushroom.get_stalk_shape(),
              mushroom.get_stalk_root(),
              mushroom.get_stalk_surface_above_ring(), mushroom.get_stalk_surface_below_ring(),
              mushroom.get_stalk_color_above_ring(), mushroom.get_stalk_color_below_ring(), mushroom.get_veil_type(),
              mushroom.get_veil_color(), mushroom.get_ring_number(), mushroom.get_ring_type(),
              mushroom.get_spore_print_color(), mushroom.get_population(), mushroom.get_habitat()), file=outfile)
print("end %MLPQ%", file=outfile)