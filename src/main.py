import sys
from Environment import Environment
from Utils.global_vars import add_flags

add_flags(sys.argv) #Adiciona parametros passados pelo input.
environment = Environment()
environment.run()
