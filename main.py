a = "['El' 'dúo' 'ganó' 'su' 'partido' 'de' 'primera' 'ronda' 'contra' 'los' 'mejores' 'sembrados' 'Juan' 'Sebastián' 'Cabal' 'y' 'Robert' 'Farah' 'en' 'sets' 'corridos' ',' 'luego' 'en' 'cuartos' 'a' 'Daniel' 'Evans' 'y' 'Ken' 'Skupski' 'también' 'en' 'sets' 'corridos' '.']"

import ast

b = ast.literal_eval(a.replace("' '", "','"))
print(b)
print(type(b))