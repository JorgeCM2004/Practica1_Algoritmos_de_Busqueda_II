import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from F_P1_Stadistics import P1_Stadistics

stadistics = P1_Stadistics()
stadistics.show()
