############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        # thought process:
        
        # self.code = code                  # to call self.code it has to be defined first?
        # def code(self, code = 'unknown'):
        #     print(f" Reporting code: {self.code}")

        #self.first_harvest = first_harvest
        #  def first_harvest(self, first_harvest = 'unknown'):
        #     print(f"{name}'s first harvest in: {self.first_harvest}")


        # self.name = name
        #   def name(self, name ='unknown'):
        #        print(f" Name: {self.name}")

        
        #self.color = (color, color = 'unknown')
        #   def color(self, color ='unknown'):
        #        print(f" Color: {self.color}")

        #self.is_seedless =
        #   def is_seedless(self, is_seedless ='unknown'):
        #        print(f" Seedless: {self.is_seedless}")

        #self.is_bestseller = 
        #   def is_bestseller(self, is_bestseller ='unknown'):
        #        print(f" Bestseller: {self.is_bestseller}")
        

# class Animal:

#   def speak(self, greet='Hey'):
#        print(f"{greet}, I'm {self.name} the {self.species}")


# class Cat(Animal):

 #   def speak(self):
 #       super().speak('Meow')


        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



