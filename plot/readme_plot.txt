Memo for Python scripts used to plot results

/iMP/plot/ directory has Python scripts used to plot simulations results described in model development paper. 

1) caco3_lys.py             : used to plot lysoclines and burial rate as functions of CaCO3 rain, OM/CaCO3 ratio and degree of undersaturation. 
    Here, you need to specify what code you used (fortran, python or matlab) by switching on/off for python and matlab 
    (e.g., python = False and matlab = False when you used fortran codes; python = False and matlab = True when matlab)
    and also simulation names where all lysocline results are stored (you need change addname in script). 
    Also, you need specify the OM degradation model (e.g., org = 'ox' if oxic-only degradation; org = 'oxanox' if oxic and anoxic degradations are enabled).
    Results are in svg and emf (if you have inkscape) files in /res/ directory under the directory with the simulation name 

2) caco3_signals_xx.py      : used to plot signal tracking diagenesis results. xx denotes the type of simulations (xx = biotest, disall, size, track2, isotrack) 
    Here, you need to specify what code you used (fortran, python or matlab), simulations names  and subfolders where results are stored. 
    You put these information in lists 'code', 'simuname' and 'filename', respectively.
    As in model development paper, results assumed here consider only the case where both oxic and anoxic degradation of OM are allowed. 
    You can change this by modifying logical array oxanox 
    (e.g., changing oxanox[:]=True to oxanox[:]=False assuming all results consider the case where only oxic degradation is allowed). 
    Note that in caco3_signals_track2.py, you do not have the option to choose model code (assumes use of Fortran codes)
    because signal tracking method 1 is only practical when using Fortran codes. 
    Output is stored in /imp_output/ directory. 

3) caco3_profiles.py        : used to plot depth profiles of major model outputs 
    As in (2), you need to specify what code you used (fortran, python or matlab), simulations names  and subfolders where results are stored. 
    You put these information in variables 'code', 'simuname' and 'filename', respectively.
    You also need specify OM degradation model: oxanox = False or True when only oxic or both oxic and anoxic degradation of OM is allowed,
    and bioturbation mode (biomode = 'fickian','nobio', 'labs' or 'turbo2').
    Finally you need to change information regarding the numbers of profiles recording, sediment grids and considered CaCO3 classes (nt, nz and nsp, respectively).
    Output is stored in the same directory as plotted data is stored. 
 