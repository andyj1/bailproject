from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import pandas as pd

bjs = pd.read_csv('data/BJS Offense_Code_Crosswalk.csv')

NATION   = Node("USA")
LA       = Node("Louisianna", parent=NATION)
NY       = Node("New York", parent=NATION)
MI       = Node("Michigan", parent=NATION)
AR       = Node("Arkansas", parent=NATION)

EBR      = Node("East Baton Rogue", parent=LA)
NYC      = Node("New York City", parent=NY)
WAYNE    = Node("Wayne County", parent=MI)
NW_AR    = Node("Northwest Arkansas", parent=AR)


CRIME    = Node("Crime")
VIO      = Node("Violent", parent=CRIME)
PROP     = Node("Property", parent=CRIME)
DRUG     = Node("Drug", parent=CRIME)

D_TRAFF  = Node("Drug\nTrafficking", parent=DRUG)
D_POSS   = Node("Drug\nPosssession/Use", parent=DRUG)
D_OTH    = Node("Drug\nOther", parent=DRUG)

# WEAP_OFF  = Node("Weapons\nOffense")  
# MURDER    = Node("Murder")
# HOMICIDE  = Node("Unspecified\nHomicide")
# MANSLA_NN = Node("Non-negligent\nManslaughter")
# MANSLA_N  = Node("Negligent Manslaughter")
# KIDNAP    = Node("Kidnapping")
# SEX_ASS   = Node("Sexual Assault")
# ROBBERY   = Node("Robbery")
# ASSAULT   = Node("Assault")
# OTH_VIO   = Node("Other\nViolent")
# OTH_VIO   = Node("Other\nViolent")
# STO_PROP  = 
# TRES_PROP = Node()
# DRUG_POS  = Node("Drug\nPossession", parent=CRIME)
# DRUG_TRAF = 
# OTHER     = 

SCH_1    = Node("SCH I", parent=D_POSS)
SCH_2    = Node("SCH II", parent=D_POSS)
SCH_3    = Node("SCH III", parent=D_POSS)
SCH_4    = Node("SCH IV", parent=D_POSS)
SCH_5    = Node("SCH V", parent=D_POSS)

# graphviz needs to be installed for the next line!
DotExporter(NATION).to_picture("plots/loc_tree.png")
DotExporter(CRIME).to_picture("plots/crime_tree.png")