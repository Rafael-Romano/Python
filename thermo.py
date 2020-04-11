import antoine
import margules
import van_laar

comp_a = antoine.P_sat("A")    # function --> thermo(identificação do composto)
comp_b = antoine.P_sat("B")    # function --> thermo(identificação do compsto)
margules.Margules(2)           # function --> Margules(número de parâmetros)
van_laar.Van_Laar()
