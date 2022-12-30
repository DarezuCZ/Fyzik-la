solvent_names = []
solvent_temperature = []
solvent_enthalpy = []


with open('liquids_names.txt', encoding = 'utf-8') as solvents_list:
    for solvent in solvents_list:
        solvent = solvent.rstrip()
        solvent_names.append(solvent)

with open('liquids_C_at_pressure.txt', encoding = 'utf-8') as solvents_list:
    for solvent in solvents_list:
        solvent = solvent.rstrip()
        solvent_temperature.append(solvent)

with open('liquids_enthalpy_of_vap.txt', encoding = 'utf-8') as solvents_list:
    for solvent in solvents_list:
        solvent = solvent.rstrip()
        solvent_enthalpy.append(solvent)

