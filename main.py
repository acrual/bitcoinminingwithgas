from taxes import *
from depreciations import *
from genset import *
from energysource import *
from revenues import *
from operationsite import Site
from variablecost import Variablecost
from capex import Capex
import ejecutar


taxes = Taxes(10)
depreciations = Depreciations(3, 20)
motor = Genset('motor1', 100, 10000, 5, 30, 100)
source = Energysource(True, 3, 0, motor)
site = Site(1,1,Revenues(1, 165, 0.1, 12019, Savings('bopd', 10000, 2, 3)), Variablecost(1, 0.03, 1000), Energysource(True, 3, 0, Genset('genset1', 400, 100000, 5, 30, 2000)), Depreciations(3,20), Taxes(30), Capex(1, 3000, 3000, 100000))
print(site.__str__())
print(site.btcRevenuesOfMonth(1))

# siguientes pasos:
# crear un site con flask
# hacerlo bonito con bootstrap
# pedir al usuario que identifique el site con el nombre que quiera
# hacer hash de ese nombre y los últimos 6 caracteres de ese hash serán el id público
# mostrar formularios con datos a introducir de todos los parámetros
# crear salidas y resultados de los cálculos según lo que decida el usuario


