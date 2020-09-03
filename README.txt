IMP [Implicit model of Multiple Particles diagenesis for proxy signal tracking]

3 versions of the code are available: Fortran, Python and MATLAB vers.
For details of how to run the code of the different versions, see readmes in individual directories. 

<<< General features >>>
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
    C. Direct method (Fortran, Python, MATLAB) 
(3) Tracked proxies:
    d13C, d18O, 14C-age, D47, sizes and time 
        Note that 14C-age and D47 are tracked only via direct method  
            and one can track model time as an additional proxy to provide age models (choose option of 'timetrack'). 
(4) Flexibility in proxy and boundary-condition changes: 
    One can choose the option to use input files for boundary-condition and proxy changes (choose option of 'reading'). 
        --- With this option, you can change the imposed boundary-condition and proxy changes as you wish 
        in directory /iMP/input/ using a Python script make_input.py (see also below).   
    One can alternatively choose options to calculate boundary-condition and proxy changes within their own codes that are used in model development paper. 

*   : Mixing caused by benthic automata created by LABS model (Choi et al., 2002; see also our extended LABS code at: https://github.com/imuds/iLABS). 
**  : Taking too much time so coded but not yet run to complete a simulation ...  
*** : Default method; fast and flexible. 
 
<<< General model switches >>> 
    Switches exist to allow changes regarding (1)-(4)
        (reaction/transport, signal tracking method, tracked proxies and how to force boundary-condition and proxy changes). 
    Fortran switches are defined in /input/defines.h file. 
    Python asks about switches when users run it.
    MATLAB code provides switches within a code. 
    See individual readme.txt for more details.

<<< Input to the model >>>
    The directory /input is used by all three version of the model and contains:
    - defines.h, a switch file for the Fortran code. 
    - When the 'reading' option is selected for any version of the code (Fortran, Python and MATLAB): 
        It needs to contain files specifying the time evolution of boundary-conditions and proxy-values (imp_input.in), 
        and the time-slice specification file of the sediment profile recording (rectime.in). 
     The subdirectory /input/EXAMPLES contains the files (imp_input.in and rectime.in) used in simulations shown in the model development paper (Kanzaki et al., 2020, GMD). 
    Users can rename and move EXAMPLE files to /input to recreate the GMD results 
        OR create their own input files of boundaries and proxies by using python script make_input.py. 
    Note that you must switch on 'reading' to use the created files (see readmes for individual versions of the code for more details). 
    Readme in /iMP/input/ directory gives more details. 
        
<<< Output of the model >>>
    The main output files can be categorized into 4 types:
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
                '015' means the number of recording (corresponding time is recorded in rectime.txt). 
                'omx' in this example can be replaced with: 
                    'ccx', 'ptx', 'o2x', 'sig' or 'bur'
                    corresponding to profiles of CaCO3 system, clay, O2, proxy signals and burial rate.
        (3) Proxy signals at certain depths (Fortran, Python, MATLAB)
            File names are sigmly.txt, sigmlyd.txt and sigbtm.txt, 
                recording signals at mixed layer bottom, doubled depth of mixed layer bottom and sediment bottom, respectively. 
                (These depths are recorded in recz.txt.)
        (4) CaCO3 wt% and burial flux at end of each simulation as function of saturation state (Fortran, Python, MATLAB)
            These results are used to plot lysocline and CaCO3 burial flux. 
        
    The above output is stored in the directory iMP/imp_output/ (created at the same location where iMP is downloaded/cloned).  
        The model output can be plotted with python scripts located in the directory iMP/plot.
        The Readme therein gives more details. 
