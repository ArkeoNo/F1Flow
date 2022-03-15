import fastf1 as ff1
session = ff1.get_session(2021, 1)
race = session.get_race()
resultats = race.results
print(f'{len(resultats)} Pilote Pendant cette course')
classement_nom = []

for pilote in resultats : 
    classement_nom.append(pilote['Driver']['familyName'])
print(classement_nom)

