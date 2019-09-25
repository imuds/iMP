IMP 
(Implicit model of Multiple Particles diagenesis for proxy signal tracking)

3 standalone codes are available: Fortran, Python and MATLAB.
Details of how to run the codes; see readmes in individual directories. 

General features:
(1) Reactive transport: 
    Solid phase   : multiple CaCO3 classes, OM and clay 
    Aqueous phase : DIC, ALK and O2 
    For bioturbation, 4 options exist:
        Fickian-, homogeneous-, LABS*- or no-mixing
    For OM degradation, one can take 2 extreme scenarios:
        oxic-only or oxic-anoxic (as in Archer, 1991) 
(2) Proxy signal tracking:
    A. Time-stepping method (Fortran, Python**, MATLAB**)
    B. Interpolating method*** (Fortran, Python, MATLAB)
    C. Direct method (Fortran, Python) 
(3) Tracked proxies:
    d13C, d18O, 14C-age, D47, sizes and time 
        Note that 14C-age and D47 are tracked only via direct method (thus limited to Fortran and Python) 
            and time-tracking is explicitly implemented only in Fortran, currently. 
(4) Flexibility in proxy and boundary changes: 
    Currently only Fortran ver. allows reading input files 
        for boundary and proxy changes.  
    Other codes calculate boundary and proxy changes within their own codes ... (to be updated to allow flexible input) 

*   : Mixing caused by benthic automata created by LABS model (Choi et al., 2002). 
**  : Taking too much time so coded but not yet run to complete a simulation ...  
*** : Default method; fast and flexible. 
 
General model switches: 
    Switches exist to allow changes regarding (1)-(4)
        (reaction/transport, signal tracking method, tracked proxies and how to force boundary and proxy changes). 
    Fortran switches are defined in /input/defines.h file. 
    Other codes have their own switches within codes. Python asks about switches when users run it.
    See individual readme.txt for more details.

Input to the model:
    /input directory contains defines.h, a switch file for Fortran code. 
    This directory also need contain time evolutions of boundary and proxy values (imp_input.in) 
        as well as time shedule of sediment profile recording (rectime.in) 
        when Fortran ver. is run with using input files for boundary and proxy changes. 
    Subdirectory /input/EXAMPLES contain those files (imp_input.in and rectime.in) used in simulations shown in manuscript. 
    Users can rename and move EXAMPLE files to /input 
        OR create their own input files of boundaries and proxies by using python script make_input.py. 
    Note that these input files can be used only for Fortran ver., currently 
        (and you must switch on 'reading' in defines.h file; see readme for Fortran for more details). 
        
Output of the model:
    Main output files can be categorized into 4 types:
        (1) flux time records (Fortran, Python) 
            Format is ...flx.txt. E.g., OM fluxes are recorded in omflx.txt files. 
            Flux files include:
                Time, time-change-flux, diffusive flux, advective flux, 
                fluxes related to OM degradation, CaCO3 dissolution and radio-decay, and 
                residual flux of all the above. 
            Note that residual flux must be close to zero for mass balance and 
                one can check the mass balance by looking at residual fluxes. 
        (2) Depth profiles of solid and aqueous phases and proxy signals (Fortran, Python, MATLAB)
            Format is, e.g., omx-015.txt. 
                In this example, 'omx' indicates OM profies and 
                '015' means the number of recording (correspoinding time is recorded in rectime.txt). 
                'omx' in this example can be replaced with: 
                    'ccx', 'ptx', 'o2x', 'sig' or 'bur'
                    corresponding to profiles of CaCO3 system, clay, O2, proxy signals and burial rate.
        (3) Proxy signals at certain depths (Fortran, Python, MATLAB)
            File names are sigmly.txt, sigmlyd.txt and sigbtm.txt, 
                recording signals at mixed layer bottom, doubled depth of mixed layer bottom and sediment bottom, respectively. 
        (4) CaCO3 wt% and burial flux at end of each simulation as function of saturation state (Fortran, Python, MATLAB)
            These results are used to plot lysocline and CaCO3 burial flux. 
        
        The above output is stored in /output directory. 
        And output can be plotted with python scripts in /plot directory.
        Readme therein gives more details. 
