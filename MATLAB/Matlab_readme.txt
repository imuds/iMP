%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%   Memo for MATLAB version of the model   %%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

1) The function to run the model can be found in the file run_sig_iso_dtchange.m and can be executed via:

run_sig_iso_dtchange(cc_rain_flx_in, rainratio_in, dep_in, dt_in, oxonly_in, biotmode, folder) 

and example call would be: run_sig_iso_dtchange(12e-6, 0.7, 3.5, 1d8, false, 'fickian', '1207_test')

Inputs are respectively: 

CaCO3 rain flux (mol cm-2 yr-1), 
OM/CaCO3 rain ratio, 
water depth (km), 
time step for each iteration (yr),
OM degradation model (oxic only degradation if true; oxic and anoxic degradation if false), 
bioturbation mode ('fickian','nobio','labs' or 'turbo2' for Fickian-, no-, LABS- and homogeneous-mixing, respectively), and 
simulation name (which becomes the name of directory where results are stored). 

If one chooses to use input files to define boundary conditions (def_reading = true), 
values for cc_rain_flx_in, rainratio_in, dep_in, dt_in are not reflected in as they are read from input file
(see, e.g., Examples 2-4 below) 


2) To run the lysocline experiments (i.e., Section 3.1 in the manuscript) execute the functions in the file lysocline_exp.m


3) Subroutines of the main code can be found in caco3_main.m


4) CaCO3 thermodynamic subroutines & functions are in caco3_therm.m (and call_co2sys.m when you use CO2SYS; see Matlab_readme_CO2SYS.txt for the details)


5) Test functions used during model development can be found in caco3_test.m 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% Boundary/initial conditions and  model options

Boundary/initial conditions can be changed in caco3_main.caco3_set_boundary_cond(), such as bottom water concentrations/fluxes

Global properties such as depth of simulated sediment column, grid numbers, densities, threshold values, rate constants and model options (e.g. OM degradation method, type of mixing to be used, enable signal tracking?)
are defined under properties of the class caco3_main. 



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% Plotting of the results is possible with python scripts in iMP/plot/ direactory:

1) caco3_lys.py		    :	plots the lysocline results for oxic-only and oxic-anoxic OM degradation model, e.g. as in Figs. 7+8 of the manuscript

2) caco3_signals_xx.py  :	plots the time change of the proxy signals, e.g. as in Fig. 10 of the manuscript

In these plot scripts, you need to specigy that 

    a) you are using the MATLAB version 
    
    b) your experiment name (the same as input folder in the function run_sig_iso_dtchange)
    
    c) subdirectory name for caco3_signals_xx.py: 
        cc-xx_rr-yy-dep-zz, where xx is CaCO3 rainflux value, yy is OM/CaCO3 rain ratio and dep is water depth

    See the comments on these scripts or readme in /iMP/plot/ directory


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%			Examples:  model development paper experiments				%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  1) Section 3.1:
change properties in caco3_main:
def_sense = true;       % without signal tracking
Can be executed by calling the 2 functions in lysocline_exp.m 
- one for the oxic only model (i.e. lysocline_exp.run_all_lysocline_exp_ox('fickian', 'your_simulation_name')) and 
one for the oxic-anoxic model (lysocline_exp.run_all_lysocline_exp_oxanox('fickian', 'your_simulation_name')). 
Results are saved in the same folder - here 'your_simulation_name' under ../imp_output/matlab/ directory

%%%%%% plotting of results is done with the python script caco3_lys.py in /iMP/plot/ directory
In the script, you need clarify you are plotting matlab results (i.e., matlab = True) and OM degradation model (ox = True or oxanox = True),
and enter your_simulation_name (see the comments on the script or readme in /iMP/plot/ directory)
 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  2) Section 3.2.1:
change properties in caco3_main:
def_reading = true;       	% use input file to specify temporal changes in boundary conditions and proxy signal values
def_nodissolve = true/false; 	% to switch caco3 dissolution on and off
set all other def_xx values false

Prepare input file for the simulation: 
move rectime_EXAMPLE-BIOT.in and imp_input_EXAMPLE-BIOT.in in /input/EXAMPLES/ directory to /input/ directory and rename them as rectime.in and imp_imput.in, respectively.
You can do this in comand line as follows:
'cd ../input' 
'cp EXAMPLES/rectime_EXAMPLE-BIOT.in rectime.in'
'cp EXAMPLES/imp_input_EXAMPLE-BIOT.in imp_input.in'

Execute experiment (with default boundary conditions) by 
run_sig_iso_dtchange(12.0e-5, 0.7, 3.5, 1d8, false, 'fickian', 'biot_sim')
input 'fickian' can be replaced by 'nobio', 'labs' or 'turbo2' to examine effect of different styles of bioturbation
(note that inputs of CaCO3 rain flux, rain tatio, water depth and time step in the above function
are meaningless as they are overwritten by inpuf file data when one uses input file to specify temporal changes of boundary conditions)

%%%%% plotting of results is done with the python script caco3_signals_biotest.py  
In the script, you need clarify you are plotting matlab results (i.e., component of list code = 'matlab')  
and specify simulation name (list simname) as well as subfolder name (list filename)
and plot style (pltstyle = 'diagdep')
(see the comments in the script or readme in /iMP/plot/ directory)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  3) Section 3.2.2:
change properties in caco3_main:
def_reading = true;       	% use input file to specify temporal changes in boundary conditions and proxy signal values
set all other def_xx values false

Prepare input file for the simulation: 
move rectime_EXAMPLE-DIS.in and imp_input_EXAMPLE-DIS-xx.in in /input/EXAMPLES/ directory to /input/ directory and rename them as rectime.in and imp_imput.in, respectively.
You can do this in comand line as follows:
'cd ../input' 
'cp EXAMPLES/rectime_EXAMPLE-DIS.in rectime.in'
'cp EXAMPLES/imp_input_EXAMPLE-DIS-xx.in imp_input.in'

Execute experiment (with default boundary conditions) by 
run_sig_iso_dtchange(12.0e-5, 0.7, 3.5, 1d8, false, 'fickian', 'dis_exp')
input 'fickian' can be replaced by 'nobio' or 'turbo2' to examine effect of different styles of bioturbation
(note that inputs of CaCO3 rain flux, rain tatio, water depth and time step in the above function
are meaningless as they are overwritten by inpuf file data when one uses input file to specify temporal changes of boundary conditions)

%%%%% plotting of results is done with the python script caco3_signals_disall.py  
In the script, you need clarify you are plotting matlab results (i.e., component of list code = 'matlab')  
and specify simulation name (list simname) as well as subfolder name (list filename)
and plot style (pltstyle = 'diagdep')
(see the comments in the script or readme in /iMP/plot/ directory)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  4) Section 3.2.3:
change properties in caco3_main:
def_reading = true;       	% use input file to specify temporal changes in boundary conditions and proxy signal values
def_size = true;            % also track a characteristic 'size' 
set all other def_xx values false

Prepare input file for the simulation: 
move rectime_EXAMPLE-SIZE.in and imp_input_EXAMPLE-SIZE.in in /input/EXAMPLES/ directory to /input/ directory and rename them as rectime.in and imp_imput.in, respectively.
You can do this in command line as follows:
'cd ../input' 
'cp EXAMPLES/rectime_EXAMPLE-SIZE.in rectime.in'
'cp EXAMPLES/imp_input_EXAMPLE-SIZE.in imp_input.in'

Execute experiment (with default boundary conditions) by 
run_sig_iso_dtchange(12.0e-5, 0.7, 3.5, 1d8, false, 'fickian', 'size_exp')
input 'fickian' can be replaced by 'nobio' or 'turbo2' to examine effect of different styles of bioturbation
(note that inputs of CaCO3 rain flux, rain ratio, water depth and time step in the above function
are meaningless as they are overwritten by input file data when one uses input file to specify temporal changes of boundary conditions)

%%%%% plotting of results is done with the python script caco3_signals_size.py  
In the script, you need clarify you are plotting matlab results (i.e., component of list code = 'matlab')  
and specify simulation name (list simname) as well as subfolder name (list filename)
and plot style (pltstyle = 'diagdep')
(see the comments in the script or readme in /iMP/plot/ directory)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  5) Section S1.1.1:
This has not been tested in matlab yet as it takes a very long time already in fortran to run.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  6) Section S1.1.2:
change properties in caco3_main:
def_reading = true;       	% use input file to specify temporal changes in boundary conditions and proxy signal values
def_isotrack = true;            % tracking isotopologues 
def_kie = true/false;   % true to check kinetic isotope effect on clumped isotope
set all other def_xx values false

Prepare input file for the simulation: 
move rectime_EXAMPLE-ISO.in and imp_input_EXAMPLE-ISO.in in /input/EXAMPLES/ directory to /input/ directory and rename them as rectime.in and imp_imput.in, respectively.
You can do this in command line as follows:
'cd ../input' 
'cp EXAMPLES/rectime_EXAMPLE-ISO.in rectime.in'
'cp EXAMPLES/imp_input_EXAMPLE-ISO.in imp_input.in'

Execute experiment (with default boundary conditions) by 
run_sig_iso_dtchange(12.0e-5, 0.7, 3.5, 1d8, false, 'fickian', 'iso_exp')
input 'fickian' can be replaced by 'nobio' or 'turbo2' to examine effect of different styles of bioturbation
(note that inputs of CaCO3 rain flux, rain ratio, water depth and time step in the above function
are meaningless as they are overwritten by input file data when one uses input file to specify temporal changes of boundary conditions)

%%%%% plotting of results is done with the python script caco3_signals_size.py  
In the script, you need clarify you are plotting matlab results (i.e., component of list code = 'matlab')  
and specify simulation name (list simname) as well as subfolder name (list filename)
and plot style (pltstyle = 'diagdep')
(see the comments in the script or readme in /iMP/plot/ directory)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  7) Section S1.2:
change properties in caco3_main:
def_sense = true;       % without signal tracking
def_co2sys = true;      % use CO2SYS
Can be executed by calling the 2 functions in lysocline_exp.m 
- one for the oxic only model (i.e. lysocline_exp.run_all_lysocline_exp_ox('fickian', 'your_simulation_name')) and 
one for the oxic-anoxic model (lysocline_exp.run_all_lysocline_exp_oxanox('fickian', 'your_simulation_name')). 
Results are saved in the same folder - here 'your_simulation_name' under ../imp_output/matlab/ directory

%%%%%% plotting of results is done with the python script caco3_lys.py in /iMP/plot/ directory
In the script, you need clarify you are plotting matlab results (i.e., matlab = True) and OM degradation model (ox = True or oxanox = True),
and enter your_simulation_name (see the comments on the script or readme in /iMP/plot/ directory)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  8) Section S1.3:
Repeat experiments in Section 3.2 with 
def_timetrack = true;
to enable addtional tracking of model time

%%%%% plotting of results is done with the python scripts   
See instructions for experiments in Section 3.2
Note that you can choose a different plot style (e.g., pltstyle = 'time' which plot signals against model time)
(see the comments in the script or readme in /iMP/plot/ directory)