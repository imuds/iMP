Memo for IMP Python ver. 

1. You need 
    a) numpy 
    b) scipy [optional, if you choose to use sparse matrix solver (asked when running)] 
    c) mocsy [optional, if you choose to use mocsy as co2 cheimistry calculation method (asked when running)] 
        (See memo_mocsy_Python.txt for installation of mocsy.) 
2. Main code (caco3.py) is written in Python 2.7. 
    You can use Python 3.x by converting the code via 2to3 (typing '2to3 caco3.py -w').
3. Run the source code caco3.py (e.g., type 'python caco3.py'):
    You will be asked to enter variables to conduct simulations. 
    E.g.)
    Results in Section 3.1 can be obtained by entering:
       co2 for co2 chemistry calculation method 
       6e-6 to 60e-6 for CaCO3 rain flux
       0.0 to 1.5 for OM/CaCO3 rain ratio
       0.24 to 6.0 for water depth
       1e8 for time step *** 
       simulation_name for simulation name
       fickian for bioturbation style
       True or False for oxic only for OM degradation
       sense for simulation mode
    *** NOTE: with a larger time step, simulation reaches a steady state sooner,
           but with a higher probability to face difficulty in convergence ***
    *** NOTE: you can use caco3_sense.py for running in series 
        for ranges of boundary conditions (water depth and rain flux and ratios) ***
        
    Results in Section 3.2.1 can be obtained by entering:
       co2 for co2 chemistry calculation method 
       12e-6 for CaCO3 rain flux
       0.7 for OM/CaCO3 rain ratio
       3.5 for water depth
       1000. for time step (this can be any value as time step is automatically calculated in signal tracking simulations)
       simulation_name for simulation name
       nobio, fickian, labs or turbo2 for bioturbation style
       False for oxic only for OM degradation
       biotest for simulation mode
       
    Results in Section 3.2.2 can be obtained by entering:
       co2 for co2 chemistry calculation method 
       12e-6 for CaCO3 rain flux
       0.7 for OM/CaCO3 rain ratio
       3.5, 4.5 or 5.0 for water depth
       1000. for time step (this can be any value as time step is automatically calculated in signal tracking simulations)
       simulation_name for simulation name
       nobio, fickian or turbo2 for bioturbation style
       False for oxic only for OM degradation
       diss. exp. for simulation mode
       
    Results in Section 3.2.3 can be obtained by entering:
       co2 for co2 chemistry calculation method 
       12e-6 for CaCO3 rain flux
       0.7 for OM/CaCO3 rain ratio
       3.5 for water depth
       1000. for time step (this can be any value as time step is automatically calculated in signal tracking simulations)
       simulation_name for simulation name
       nobio, fickian or turbo2 for bioturbation style
       False for oxic only for OM degradation
       size for simulation mode
       
    Results in Section 3.3.1 may be obtained*** by entering:
       co2 for co2 chemistry calculation method 
       12e-6 for CaCO3 rain flux
       0.7 for OM/CaCO3 rain ratio
       5.0 for water depth
       1000. for time step (this can be any value as time step is automatically calculated in signal tracking simulations)
       simulation_name for simulation name
       nobio, fickian or turbo2 for bioturbation style
       False for oxic only for OM degradation
       diss. exp. for simulation mode
    *** NOTE: it will take a very long time 
          as such consistency with Fortran ver. has not been checked ***
       
    Results in Section 3.3.2 can be obtained by entering:
       co2 for co2 chemistry calculation method 
       12e-6 for CaCO3 rain flux
       0.7 for OM/CaCO3 rain ratio
       5.0 for water depth
       1000. for time step (this can be any value as time step is automatically calculated in signal tracking simulations)
       simulation_name for simulation name
       nobio, fickian or turbo2 for bioturbation style
       False for oxic only for OM degradation
       isotrack or iso_kie for simulation mode
          
    Results in Section 3.3.3 can be obtained by entering:
       mocsy for co2 chemistry calculation method 
       6e-6 to 60e-6 for CaCO3 rain flux
       0.0 to 1.5 for OM/CaCO3 rain ratio
       0.24 to 6.0 for water depth
       1e8 for time step *** 
       simulation_name for simulation name
       fickian for bioturbation style
       True or False for oxic only for OM degradation
       sense for simulation mode
    *** NOTE: with a larger time step, simulation reaches a steady state sooner,
           but with a higher probability to face difficulty in convergence ***

******** CAUTION: IMP Python ver. currently does not track time explicitly. Time-depth relationship is estimated based on burial rate. 
    When plotting against the burial-rate-based time scale, results by Python ver. are exactly the same as those with Fortran ver. 
    Lysocline estimates are irrelevant to time-track so they are the same between different source codes (Fortran, Python and MATLAB). ********    

Output data is made in almost the same formats as those in Fortran ver. 
In case of Python ver., result directory is made in a directory under 'python' branches. 
E.g., /imp_output/python/simulation_name_specified/profiles/oxanox/, 
    /imp_output/python/simulation_name_specified/res/oxanox/
Ploting the results can be done with python scripts in /plot directory. 
You need to indicate you are plotting Python ver. results by switch on/off 
    (i.e., make a logical parameter 'python' = True in these scripts). 
   