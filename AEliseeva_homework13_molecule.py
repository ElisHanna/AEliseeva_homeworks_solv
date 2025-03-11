import os
from chempy import Substance
from chempy.util import periodic as P

os.system('cls')


def formule_transformation(form):
    """
    This function transforms chemical formuls into the dictionary,
    that contains elements symbols and their quantity in molecule.
    For making this function work, the module 'chempy' slould be installed.
    """
    f = Substance.from_formula(form)
    elements = []
    numbers = []
    for i in f.composition:
        elements.append(P.symbols[i-1])
        numbers.append(f.composition[i])
    result = {e: n for e, n in zip(elements, numbers)}
    print(result)


formule_transformation('H2O')
formule_transformation('Mg(OH)2')
formule_transformation('K4[ON(SO3)2]2')
formule_transformation('[Cu(NH3)4](OH)2')
formule_transformation('H2[AuCl4]')
formule_transformation('[Ca(H2O)6](NO3)2')
formule_transformation('[Ni(NH3)6](NO3)3')
