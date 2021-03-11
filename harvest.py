############
# Part 1   #
############


# def __init__() is a set-up (a part of that class object, takes in all of the attributes)
# the rest are functions under def __init__()?

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

 
# thought process:
        
# self.code = code                 
# def code(self, code = 'unknown'):
#     print(f" Reporting code: {self.code}")

#self.first_harvest = first_harvest
#   def first_harvest(self, first_harvest = 'unknown'):
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
        
# self.pairs_with = 
#   def pairs_with(self, pairs_with ='unknown'):
#        print(f" Pairs best with: {self.pairs_with}")


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""


        
        for food_pair in range(len(pairings_list)):

# use self.pairing to get into attribute and then append it 
               
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



# do we need dictionaries of these attributes to hold the values? not yet
# like the key would be the name of the attribute, value is the attributes

# code = {
#     1: 'musk',
#     2: 'cas',
#     3: 'cren',
#     4: 'yw'
# }

# first_harvest = {
#     1: '1998',
#     2: '2003',
#     3: '1996',
#     4: '2013'
# }

# color = { 
#     1: 'orange',
#     2: 'green',
#     3: 'yellow',
#     4: 'light green'
# }

# is_seedless = {
#     1: 'seedless',
#     2: 'has seeds'
# }

# is_ bestseller = {
#     1: 'True',
#     2: 'False'
# }

# name = {
#     1: 'Muskmelon',
#     2: 'Casaba',
#     3: 'Crenshaw',
#     4: 'Yellow Watermelon'
#  }

# pairs_with = {
#     1: 'mint',
#     2: 'strawberries',
#     3: 'proscuitto',
#     4: 'ice cream'
# }
       

# thought process:

# want to get a specific value from the dictionary, pairs_with,
# you'd use pairs_with[]
# so pairs_with[1] = 'mint' 
# but i didn't put these dictionaries in order with the order of the names
# so i'm assuming we'll have to index to get the specific values
#       pairings_list.append(pair_with[i])
#       print(pairings_list)

# if pairings_list is a dictionary in class MelonTypes,
# can we pull from the list? and how?        
            