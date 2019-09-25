# IMP 
###### **I**mplicit model of **M**ultiple **P**articles diagenesis for proxy signal tracking

## 3 standalone codes are available: Fortran, Python and MATLAB.
## Details of how to run the codes; see readmes in individual directories. 

## General features:
(1) Reactive transport: 
    Solid phase   : multiple CaCO3 classes, OM and clay 
    Aqueous phase : DIC, ALK and O2 
    For bioturbation, 4 options exist:
        Fickian-, homogeneous-, LABS- or no-mixing
    For OM degradation, one can take 2 extreme scenarios:
        oxic-only or oxic-anoxic (as in Archer, 1991) 
(2) Proxy signal tracking:
    A. Time-stepping method (Fortran, Python\[^1], MATLAB\[^1])
    B. Interpolating method\[^2] (Fortran, Python, MATLAB)
    C. Direct method (Fortran, Python) 
(3) Tracked proxies:
    d13C, d18O, sizes and time (time-tracking is explicitly implemented only in Fortran, currently)
(4) Flexibility in proxy and boundary changes: 
    Currently only Fortran ver. allows reading input files 
        for boundary and proxy changes.  
    Other codes calculate boundary and proxy changes within their own codes ... (to be updated to allow flexible input) 
     
\[^1]: taking too much time so coded but not yet run to complete a simulation ...  
\[^2]: Default method; fast and flexible 
 
## General model switches: 
    Regarding the above features (1)-(4), 
    switches exist to allow changes regarding (1)-(4)
        (reaction/transport, signal tracking method, tracked proxyes and how to force boundary and proxy changes). 
    Fortran switches are defined in /input/defines.h file. 
    Other codes have their own switches within codes. Python asks about switches when when users run it.
    See individual readme.txt for more details.

## Input to the model:
    /input directory contains defines.h, a switch file for Fortran code. 
    This directory also need contain time evolutions of boundary and proxy values (imp_input.in) 
        as well as time shedule of sediment profile recording (rectime.in) 
        when Fortran ver. is run with using input files for boundary and proxy changes. 
    Subdirectory /input/EXAMPLES contain those files (imp_input.in and rectime.in) used in simulations shown in manuscript. 
    Users can rename and move EXAMPLE files to /input 
        **or** create their own input files of boundaries and proxies by using python script make_input.py. 
    Note that these input files can be used only for Fortran ver., currently 
        (and you must switch on 'reading' in defines.h file; see readme for Fortran for more details). 
        
## Output of the model:
    Main output files can be categolized into 4 types:
        (1) flux time records (Fortran, Python) 
            Format is ...flx.txt. E.g., OM fluxes are recorded in omflx.txt files. 
            Flux files include:
                Time, time-change-flux, diffusive flux, advective flux, 
                fluxes related to OM degradation, CaCO3 dissoluton and radio-decay, and 
                residual flux of all the above. 
            Note that residual flux must be close to zero for mass balance and one can check mass balance by looking at residual fluxes. 
        (2) Depth profiles of solid and aqueous phases and proxy signals (Fortran, Python, MATLAB)
            Format is, e.g., omx-015.txt. 
                In this example, 'omx' indicates OM profies and 
                '015' means the number of recording (correspoinding time is recorded in rectime.txt). 
                'omx' in this example can be replaced with: 
                    'ccx', 'ptx', 'o2x', 'sig' or 'bur'
                    corresponding to profiles of CaCO3 system, clay, O2, proxy signals and burial rate.
        (3) Proxy signals at certain depths
            File names are sigmly.txt, sigmlyd.txt and sigbtm.txt, 
                recording signals at mixed layer bottom, doubled depth of mixed layer bottom and sediment bottom, respectively. 
        (4) CaCO3 wt% and burial flux at end of each simulation as function of saturation state
            These results are used to plot lysocline and CaCO3 burial flux. 
        
        /plot directory contains python scripts plotting the above output.
        Readme therein gives more details. 
