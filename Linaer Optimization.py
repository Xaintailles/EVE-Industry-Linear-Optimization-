# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:19:17 2019

@author: Calixte.allier

Problem: Need to craft a ship with 100 Tritanium and 200 Mexallon
Arkonor = 10 Tritanium + 20 Mexallon
Gneiss = 20 Tritanium + 10 Mexallon
"""

import pulp

# List of ores
Ore = ['Bright Spodumain','Crimson Arkonor','Sharp Crokite','Onyx Ochre','Triclinic Bistot','Iridescent Gneiss']

# Dictionnary of needed minerals
Tritanium = 62725038,
Pyerite = 15403238,
Mexallon = 5736811,
Isogen = 899047,
Nocxium = 253724,
Zydrine = 91025,
Megacyte = 39246,
Morphite = 0

#Dictionnaries of the yield of each of the ores
Tritanium_yield = {'Bright Spodumain': 36.75 ,
                   'Crimson Arkonor':  14.438 ,
                   'Sharp Crokite': 13.781 ,
                   'Onyx Ochre': 13.125 ,
                   'Triclinic Bistot': 0 ,
                   'Iridescent Gneiss': 0 
        }

Pyerite_yield = {'Bright Spodumain': 7.908 ,
                   'Crimson Arkonor':  0 ,
                   'Sharp Crokite': 0 ,
                   'Onyx Ochre': 0 ,
                   'Triclinic Bistot': 7.875 ,
                   'Iridescent Gneiss': 4.620
        }

Mexallon_yield = {'Bright Spodumain': 1.378 ,
                   'Crimson Arkonor':  1.641 ,
                   'Sharp Crokite': 0 ,
                   'Onyx Ochre': 0 ,
                   'Triclinic Bistot': 0 ,
                   'Iridescent Gneiss': 5.040 
        }

Isogen_yield = {'Bright Spodumain': 0.295 ,
                   'Crimson Arkonor':  0 ,
                   'Sharp Crokite': 0 ,
                   'Onyx Ochre': 2.1 ,
                   'Triclinic Bistot': 0 ,
                   'Iridescent Gneiss': 0.630 
        }

Nocxium_yield = {'Bright Spodumain': 0 ,
                   'Crimson Arkonor':  0 ,
                   'Sharp Crokite': 0.499 ,
                   'Onyx Ochre': 0.158 ,
                   'Triclinic Bistot': 0 ,
                   'Iridescent Gneiss': 0 
        }

Zydrine_yield = {'Bright Spodumain': 0 ,
                   'Crimson Arkonor':  0 ,
                   'Sharp Crokite': 0.089 ,
                   'Onyx Ochre': 0 ,
                   'Triclinic Bistot': 0.295 ,
                   'Iridescent Gneiss': 0 
        }

Megacyte_yield = {'Bright Spodumain': 0 ,
                   'Crimson Arkonor':  0.210 ,
                   'Sharp Crokite': 0 ,
                   'Onyx Ochre': 0 ,
                   'Triclinic Bistot': 0.066 ,
                   'Iridescent Gneiss': 0 
        }

Morphite_yield = {'Bright Spodumain': 0 ,
                   'Crimson Arkonor':  0 ,
                   'Sharp Crokite': 0 ,
                   'Onyx Ochre': 0 ,
                   'Triclinic Bistot': 0 ,
                   'Iridescent Gneiss': 0 
        }


# Creating the problem
prob = pulp.LpProblem("Capital Crafting",pulp.LpMinimize)

# Defining the variables for the problem
ore_vars = pulp.LpVariable.dicts("Ore",Ore,0)

# Defining the Optimal Function
prob += pulp.lpSum(ore_vars[i] for i in Ore)

# Defining the constraints

prob += pulp.lpSum(Tritanium_yield[i] * ore_vars[i] for i in Ore) >= Tritanium , "Tritanium Constraint"
prob += pulp.lpSum(Pyerite_yield[i] * ore_vars[i] for i in Ore) >= Pyerite , "Pyerite Constraint"
prob += pulp.lpSum(Mexallon_yield[i] * ore_vars[i] for i in Ore) >= Mexallon , "Mexallon Constraint"
prob += pulp.lpSum(Isogen_yield[i] * ore_vars[i] for i in Ore) >= Isogen , "Isogen Constraint"
prob += pulp.lpSum(Nocxium_yield[i] * ore_vars[i] for i in Ore) >= Nocxium , "Nocxium Constraint"
prob += pulp.lpSum(Zydrine_yield[i] * ore_vars[i] for i in Ore) >= Zydrine , "Zydrine Constraint"
prob += pulp.lpSum(Megacyte_yield[i] * ore_vars[i] for i in Ore) >= Megacyte , "Megacyte Constraint"
prob += pulp.lpSum(Morphite_yield[i] * ore_vars[i] for i in Ore) >= Morphite , "Morphite Constraint"

#Writting the Problem
prob.writeLP("CapitalCrafting.lp")

prob.solve()

print("Status:", pulp.LpStatus[prob.status])

result = prob.variables

for v in prob.variables():
    print(v.name, "=", v.varValue)
    
print(result)

