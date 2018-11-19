 #THIS IMPORTS SOME PREDEFINED PYTHON LIBRARIES USED BY PYTHONBIOGEME
from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *
from random import random
from loglikelihood import *

#IN THIS SECTION YOU DEFINE THE PARAMETERS TO BE ESTIMATED 
# Arguments:
#   1  Name used in report file. Typically, the same as the variable name.
#   2  Starting value of the parameter
#   3  Lower bound of the parameter
#   4  Upper bound of the parameter
#   5  0: estimate the parameter, 1: keep it fixed (this can be used to estimate simpler models)
Bprice = Beta('Bprice',0,-100,100,0 )

Bbattery1 = Beta('Bbattery1',0,-100,100,0)
Bbattery2 = Beta('Bbattery2',0,-100,100,0)
Bbattery3 = Beta('Bbattery3',0,-100,100,0)

Bppi1 = Beta('Bppi1',0,-100,100,0)
Bppi2 = Beta('Bppi2',0,-100,100,0)
Bppi3 = Beta('Bppi3',0,-100,100,0)

Bproc1 = Beta('Bproc1',0,-100,100,0)
Bproc2 = Beta('Bproc2',0,-100,100,0)
Bproc3 = Beta('Bproc3',0,-100,100,0)

Bram1 = Beta('Bram1',0,-100,100,0)
Bram2 = Beta('Bram2',0,-100,100,0)
Bram3 = Beta('Bram3',0,-100,100,0)

Bcam1 = Beta('Bcam1',0,-100,100,0)
Bcam2 = Beta('Bcam2',0,-100,100,0)
Bcam3 = Beta('Bcam3',0,-100,100,0)


ASC_1 = Beta('ASC_1', 0, -100, 100, 1)
ASC_2 = Beta('ASC_2', 0, -100, 100, 0)
ASC_3 = Beta('ASC_3', 0, -100, 100, 0)

###################################################################
# HERE EXPRESSIONS ARE GIVEN TO DEFINE AND RECALCULATE VARIABLES



#RESCALE THE VARIABLES TO AVOID COMPUTATIONAL PROBLEMS
####################################################################################################
#THIS SECTION DEFINES THE SYSTEMATIC UTILITY FUNCTIONS
#Fairphone
V1 = ASC_1 + Bprice * price1 + Bbattery1 * battery1 + Bproc1 * proc1 + Bram1 * ram1 + Bcam1 * cam1
#Apple I-phone
V2 = ASC_2 + Bprice * price2 + Bbattery2 * battery2 + Bproc2 * proc2 + Bram2 * ram2 + Bcam2 * cam2
#Samsung Galaxy
V3 = ASC_3 + Bprice * price3 + Bbattery3 * battery3 + Bproc3 * proc3 + Bram3 * ram3 + Bcam3 * cam3

#####################################################################################################
#HERE THE EXCLUDES CAN BE DEFINED USING STATEMENTS
#define exclude variable
exclude = 0.0
exclude += ( price1 < 0 )
#####################################################################################################

BIOGEME_OBJECT.EXCLUDE = ( exclude > 0.0 )


##########################################################################
#Put the systematic utility functions in one matrix in order to provide correspondence between choice and V
V = {1: V1,
      2: V2,
      3: V3,
    }
#Put availability variables in matrix	    
av = {1: 1,
      2: 2,
      3: 3
	}
#Defines an iterator on the data
rowIterator('ObsIter') 

#################################################################
# ESTIMATION SECTION (MULTINOMIAL LOGIT MODEL)
# The choice model is a logit, with availability conditions captured by av
# The choice probability is calculated using the predefined function bioLogit
# It takes as arguments the systematic utility functions (V), whether the alternatives are available for the respondent (av) and the choice made (choice)
# This variable gives therefore the probability of the chosen alternative
probchosen = bioLogit(V,av,choice)
# Define the likelihood function. This function is maximized by the estimation routine.
BIOGEME_OBJECT.ESTIMATE = Sum(log(probchosen),'ObsIter')
# Statistics
choiceSet = [1,2,3]
#cteLoglikelihood(choiceSet,choice,'ObsIter')
#availabilityStatistics(av,'ObsIter')