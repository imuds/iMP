Memo for IMP Python ver. 

1. You need 
    a) numpy 
    b) scipy [optional, if you choose to use sparse matrix solver (asked when running)] 
    c) mocsy [optional, if you choose to use mocsy as co2 cheimistry calculation method (asked when running)] 
        (See memo_mocsy_Python.txt for installation of mocsy.) 
    d) PyCO2SYS [optional, if you choose to use CO2SYS as co2 chemistry calculation method (asked when running)] 
        (See memo_CO2SYS_Python.txt for installation of PyCO2SYS.) 
2. Main code (caco3.py) is written in Python 2.7. 
    You can use Python 3.x by converting the code via 2to3 (typing '2to3 caco3.py -w').
3. Run the source code caco3.py (e.g., type 'python caco3.py'):
    You will be asked to enter variables to conduct simulations. 
    E.g.
    (1) Results in Section 3.1 can be obtained by entering:
       simulation_name for simulation name
       co2 for co2 chemistry calculation method 
       fickian for bioturbation style
       True or False for oxic only for OM degradation
       6e-6 to 60e-6 for CaCO3 rain flux
       0.0 to 1.5 for OM/CaCO3 rain ratio
       0.24 to 6.0 for water depth
       1e8 for time step *** 
       sense for simulation mode
       False for other True/False options
    *** NOTE: with a larger time step, simulation reaches a steady state sooner,
           but with a higher probability to face difficulty in convergence ***
    *** NOTE: you can use caco3_sense.py for running in series 
        for ranges of boundary conditions (water depth and rain flux and ratios) ***
        
    (2) Results in Sections 3.2.1 can be obtained by entering:
       simulation_name for simulation name
       co2 for co2 chemistry calculation method 
       nobio, fickian, labs or turbo2 for bioturbation style
       False for oxic only for OM degradation
       True for use of external input file
       False for the other True/False options
       (Note that you need corresponding input file for temporal changes of boundary and signal conditions:
            This can be done by typing following lines:
            'cd ../input' 
            'cp EXAMPLES/rectime_EXAMPLE-BIOT.in rectime.in'
            'cp EXAMPLES/imp_input_EXAMPLE-BIOT.in imp_input.in')
        
    (3) Results in Sections 3.2.1 can be obtained by entering:
       simulation_name for simulation name
       co2 for co2 chemistry calculation method 
       nobio, fickian or turbo2 for bioturbation style
       False for oxic only for OM degradation
       True for use of external input file
       False for the other True/False options
       (Note that you need corresponding input file for temporal changes of boundary and signal conditions:
            This can be done by typing following lines:
            'cd ../input' 
            'cp EXAMPLES/rectime_EXAMPLE-DIS.in rectime.in'
            'cp EXAMPLES/imp_input_EXAMPLE-DIS-xx.in imp_input.in')
       
    (4) Results in Section 3.2.3 can be obtained by entering:
       simulation_name for simulation name
       co2 for co2 chemistry calculation method 
       nobio, fickian or turbo2 for bioturbation style
       False for oxic only for OM degradation
       True for use of external input file
       size for additional tracking feature
       False for the other True/False options
       (Note that you need corresponding input file for temporal changes of boundary and signal conditions:
            This can be done by typing following lines:
            'cd ../input' 
            'cp EXAMPLES/rectime_EXAMPLE-SIZE.in rectime.in'
            'cp EXAMPLES/imp_input_EXAMPLE-SIZE.in imp_input.in')
       
    (5) Results in Section S1.1.1 may be obtained*** by entering:
       simulation_name for simulation name
       co2 for co2 chemistry calculation method 
       nobio, fickian or turbo2 for bioturbation style
       False for oxic only for OM degradation
       12e-6 for CaCO3 rain flux
       0.7 for OM/CaCO3 rain ratio
       5.0 for water depth
       1e3 for time step 
       track2 for simulation mode
       False for other True/False options
    *** NOTE: it will take a very long time 
          as such consistency with Fortran ver. has not been checked ***
       
    (6) Results in Section S1.1.2 can be obtained by entering:
       simulation_name for simulation name
       co2 for co2 chemistry calculation method 
       nobio, fickian or turbo2 for bioturbation style
       False for oxic only for OM degradation
       True for use of external input file
       isotrack for additional tracking feature
       True or False for checking kie effect
       False for the other True/False options
       (Note that you need corresponding input file for temporal changes of boundary and signal conditions:
            This can be done by typing following lines:
            'cd ../input' 
            'cp EXAMPLES/rectime_EXAMPLE-ISO.in rectime.in'
            'cp EXAMPLES/imp_input_EXAMPLE-ISO.in imp_input.in')
          
    (7) Results in Section S1.2 can be obtained by entering:
       simulation_name for simulation name
       mocsy or co2sys for co2 chemistry calculation method 
       fickian for bioturbation style
       True or False for oxic only for OM degradation
       6e-6 to 60e-6 for CaCO3 rain flux
       0.0 to 1.5 for OM/CaCO3 rain ratio
       0.24 to 6.0 for water depth
       1e8 for time step *** 
       sense for simulation mode
       False for other True/False options
    *** NOTE: with a larger time step, simulation reaches a steady state sooner,
           but with a higher probability to face difficulty in convergence ***
    *** NOTE: you can use caco3_sense.py for running in series 
        for ranges of boundary conditions (water depth and rain flux and ratios) ***
       
    (8) Results in Section S1.3 can be obtained by entering the same answers as in (2)-(4) but additionally enter:
       True for tracking model time

Output data is made in almost the same formats as those in the other versions. 
In case of Python ver., result directory is made in a directory under 'python' branches. 
E.g., /imp_output/python/simulation_name_specified/profiles/oxanox/, 
    /imp_output/python/simulation_name_specified/res/oxanox/
Plotting the results can be done with python scripts in /plot directory. 
    You need to indicate you are plotting Python ver. results  
    (i.e., enter 'python' in code list in these scripts; see the scripts or readme therein for details)
    and plotting against diagnosed depth or time (when model time is tracked)
    (i.e., enter 'diagdep' or 'time' as pltstyle in these scripts; see the scripts or readme therein for details). 
    
   