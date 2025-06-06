import os
import chempy


os.system('cls')


def formule_transformation(form):
    """
    This function transforms chemical formuls into the dictionary,
    that contains elements symbols and their quantity in molecule.
    For making this function work, the library 'chempy' slould be installed.
    """
    f = chempy.Substance.from_formula(form)
    elements = []
    numbers = []
    for i in f.composition:
        elements.append(chempy.util.periodic.symbols[i-1])
        numbers.append(f.composition[i])
    result = dict(zip(elements, numbers))
    return result


formule_transformation('H2O')
formule_transformation('Mg(OH)2')
formule_transformation('K4[ON(SO3)2]2')
formule_transformation('[Cu(NH3)4](OH)2')
formule_transformation('H2[AuCl4]')
formule_transformation('[Ca(H2O)6](NO3)2')
formule_transformation('[Ni(NH3)6](NO3)3')
