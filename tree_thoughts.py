from anytree import Node, RenderTree
from anytree.exporter import DotExporter

nation   = Node("USA")
LA       = Node("Louisianna", parent=nation)
NY       = Node("New York", parent=nation)

EBR      = Node("East Baton Rogue", parent=LA)
NYC      = Node("New York City", parent=NY)

LA_1     = Node("EBR SCH 1", parent=EBR)
LA_2     = Node("EBR SCH 2", parent=EBR)
LA_3     = Node("EBR SCH 3", parent=EBR)
LA_4     = Node("EBR SCH 4", parent=EBR)
LA_5     = Node("EBR SCH 5", parent=EBR)

NYC_1    = Node("NYC SCH 1", parent=NYC)
NYC_2    = Node("NYC SCH 2", parent=NYC)
NYC_3    = Node("NYC SCH 3", parent=NYC)
NYC_4    = Node("NYC SCH 4", parent=NYC)
NYC_5    = Node("NYC SCH 5", parent=NYC)

# graphviz needs to be installed for the next line!
DotExporter(nation).to_picture("plots/tree.png")
