endereco = "Rua das Flores 72, casa 1002, Laranjeiras, RJ, 23440120" # ou 23440-120


import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
# Números dentro dos {} indicam quantificadores para os conjuntos
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)