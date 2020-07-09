%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%   Memo for MATLAB version of the model   %%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

1) The function to run the model can be found in the file run_sig_iso_dtchange.m and can be executed via:

run_sig_iso_dtchange(cc_rain_flx_in, rainratio_in, dep_in, dt_in, oxonly_in, folder) 

and example call would be: run_sig_iso_dtchange(6.0e-5, 1.5, 0.24, 1d8, true, '1207_test')


2) To run the lysocline experiments (i.e., Section 3.1 in the manuscript) execuet the functions in the file lysocline_exp.m


3) Subroutines of the main code can be found in caco3_main.m


4) CaCO3 therdomynamic subroutines & functions are in caco3_therm.m 


5) Test functions used during model development can be found in caco3_test.m 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% Boundary/initial conditions and  model options

Boundary/initial conditions can be changed in caco3_main.caco3_set_boundary_cond(), such as bottom water concentrations/fluxes

Global properties such as depth of simulated sediment column, grid numbers, densities, threshold values, rate constants and model options (e.g. OM degradation method, type of mixing to be used, enable signal tracking?)
are defined under properties of the class caco3_main. 



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% Plotting of the results is curently possible with the following python scripts (folder of model results and number of CaCO3 classes has to be specified in these python scripts):

1) matlab_caco3_profiles_sum_multi_v3.py	:	plots the geochemical profiles, e.g. as in Fig. 3 of the masnuscript

2) matlab_caco3_lys_oxanox_sum_v3.py		:	plots the lysocline results for oxic-only and oxic-anoxic OM degradation model, e.g. as in 								Figs. 5+6 of the masnuscript

3) matlab_caco3_signals.py			:	plots the time change of the proxy signals, e.g. as in Fig. 8 of the masnuscript



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%			  GMD manuscript experiments				%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  Figure 3:
change properties in caco3_main:
def_sense = true;       % without signal tracking
set default boundary conditions as in Table 1
execute as:
run_sig_iso_dtchange(12.0e-5, 0.7, 3.5, 1d8, true, '2207_Fig3')

%%%%%% plotting of profiles is done with the python script matlab_caco3_profiles_sum_multi_v3.py using data from the following files:
below XX =  total recording time of sediment profiles (e.g. 01 - 15)

matlab_ptx-0XX.txt: contains clay data. Columns: depth (cm), age(yr), clay wt%, sld sediment density (g cm-3), sld vol. fraction (cm3 cm-3), burial velocity (cm yr-1)
matlab_ccx-0XX.txt: contains caco3 data. Columns: depth (cm), age(yr), CaCO3 wt%, DIC (M), ALK (M), capdelta-CO3 (M), dissolution rate,  pH
matlab_omx-0XX.txt: contains OM data. Columns: depth (cm), age(yr), OM wt%
matlab_o2-0XX.txt: contains O2 data. Columns: depth (cm), age(yr), O2 (M), oxic degradation rate (mol cm-3 yr-1), anoxic degradation rate (mol cm-3 yr-1)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  Figure 4:
This is the depth profiles of dissolution exp. #2. (see Fig. 10 instruction)

%%%%%% plotting of profiles is done with the python script matlab_caco3_profiles_sum_multi_v3.py using data from the following files:
below XX =  total recording time of sediment profiles (e.g. 01 - 15)

matlab_ptx-0XX.txt: contains clay data. Columns: depth (cm), age(yr), clay wt%, sld sediment density (g cm-3), sld vol. fraction (cm3 cm-3), burial velocity (cm yr-1)
matlab_ccx-0XX.txt: contains caco3 data. Columns: depth (cm), age(yr), CaCO3 wt%, DIC (M), ALK (M), capdelta-CO3 (M), dissolution rate,  pH
matlab_omx-0XX.txt: contains OM data. Columns: depth (cm), age(yr), OM wt%
matlab_o2-0XX.txt: contains O2 data. Columns: depth (cm), age(yr), O2 (M), oxic degradation rate (mol cm-3 yr-1), anoxic degradation rate (mol cm-3 yr-1)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  Figures 5 + 6:
change properties in caco3_main:
def_sense = true;       % without signal tracking
Can be executed by calling the 2 functions in lysocline_exp.m - one for the oxic only model (i.e. lysocline_exp.run_all_lysocline_exp_ox('000_test')) and one for the oxic-anoxic model (lysocline_exp.run_all_lysocline_exp_ox('000_test')). Results are saved in the same folder - here 000_test for plotting purposes

CaCO3 wt% and burial results are stored in lys_sense_cc-xx_rr-yy.txt and ccbur_sense_cc-xx_rr-yy.txt files, respectively,
   where xx and yy are CaCO3 rain flux and OM/CaCO3 rain ratio, respectively

%%%%%% plotting of results is done with the python script matlab_caco3_lys_oxanox_sum_v3.py using data from the following files lys_sense_cc-xx_rr-yy.txt and ccbur_sense_cc-xx_rr-yy.txt
matlab_lys_sense_cc-xx_rr-yy.txt: contains caco3 and sld sediment vol. frac. data. Columns: DCO3 (uM), CaCO3 wt% (surface), sld sed. vol. frac. (surface),CaCO3 wt% (mixed layer), sld sed. vol. frac. (mixed layer), CaCO3 wt% (bottom), sld sed. vol. frac. (bottom) 
matlab_ccbur_sense_cc-xx_rr-yy.txt: contains caco3 burial flux and sld sediment vol. frac. data. Columns: DCO3 (uM), CaCO3 burial fulx 
(xx and yy are CaCO3 rain flux and OM/CaCO3 rain ratio)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  Figures 8 (Section 3.2.1):
change properties in caco3_main:
def_sense = false;       	% with signal tracking
def_biotest = true;   		% testing 5kyr signal change event
def_nodissolve = true/false; 	% to switch caco3 dissolution on and off
TO SET DIFFERENT MIXING STYLES SET ONE OF THE FOLLOWING TO 'TRUE' - OR ALL 'FALSE' FOR FICKIAN MIXING:
def_allnobio = false;       	% without bioturbation?
def_allturbo2 = false;      	% all turbo2 mixing
def_alllabs = false;        	% all labs mixing
def_allnonlocal = false; 	% ON if assuming non-local mixing (i.e., if labs or turbo2 is ON)

Execute experiment (with default boundary conditions) by 
run_sig_iso_dtchange(12.0e-5, 0.7, 3.5, 1d8, true, '2207_Fig8')

%%%%% plotting of results is done with the python script matlab_caco3_signals.py using data from the following files 
matlab_rectime.txt	% includes the year when sediment profiles are recorded
matlab_sigmly.txt	% includes signal values at mixed layer bottom: relative time (yr), d13C, d18O, CaCO3 wt%, clay wt%
matlab_bound.txt	% includes boundary fluxes: time(yr), d13C, d18O, CaCO3 flux (mol cm-2 yr-1), temperature (C),  depth (km),  salinity (permil), DIC (uM),  ALK(uM)  O2(uM)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  Figures 10 (Section 3.2.2):
change properties in caco3_main:
def_sense = false;       	% with signal tracking
def_biotest = false;   		% 50 kyr experiment not the 5kyr signal change event
TO SET DIFFERENT MIXING STYLES SET ONE OF THE FOLLOWING TO 'TRUE' - OR ALL 'FALSE' FOR FICKIAN MIXING:
def_allnobio = false;       	% without bioturbation?
def_allturbo2 = false;      	% all turbo2 mixing
def_allnonlocal = false; 	% ON if assuming non-local mixing (i.e., if labs or turbo2 is ON)
change the maximum depth in the actual code in run_sig_iso_dtchange() line 25, e.g.:
dep_max = 5.0d0;    %   max depth to be changed to during the experiment

Execute experiment (with default boundary conditions) by 
run_sig_iso_dtchange(12.0e-5, 0.7, 3.5, 1d8, true, '2207_Fig10')

%%%%% plotting of results is done - as for Fig. 8 - with the python script matlab_caco3_signals.py using data from the following files 
matlab_rectime.txt	% includes the year when sediment profiles are recorded
matlab_sigmly.txt	% includes signal values at mixed layer bottom: relative time (yr), d13C, d18O, CaCO3 wt%, clay wt%
matlab_bound.txt	% includes boundary fluxes: time(yr), d13C, d18O, CaCO3 flux (mol cm-2 yr-1), temperature (C),  depth (km),  salinity (permil), DIC (uM),  ALK(uM)  O2(uM)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%  Figures 12 (Section 3.2.3):
This has not been tested in matlab yet as it takes a very long time already in fortran to run.


