Readme on script/data in input directory

/input/ directory has:

1) labs-mtx.txt     : transition matrix created from a LABS simulation, used in all versions of codes [Fortran, Python, MATLAB]

2) defines.h        : macros where you can modify options for Fortran version of codes

3) make_input.py    : Python script used to create input files (reactime.in and imp_input.in) for all versions of codes [Fortran, Python, MATLAB]
    
    a) reactime.in  : listing model time at which simulated depth profiles are recorded
    
    b) imp_input.in : recording time changes of boundary conditions and input proxy signal values 
        (where the columns present the different parameters one wants to change and 
        the lines are the time-slices; see make_input.py for the list of default parameters)
    
    The above two input files used for simulations in model development paper are saved in /input/EXAMPLES/ directory,
        named as reactime_EXAMPLE-xxx.in and inp_input_EXAMPLE-xxx.in, respectively, and can be used by moving to /input/ directory
        and re-naming them as rectime.in and imp_input.in respectively. 
        E.g., in command line,             
            'cd ../input' 
            'cp EXAMPLES/rectime_EXAMPLE-xxx.in rectime.in'
            'cp EXAMPLES/imp_input_EXAMPLE-xxx.in imp_input.in'
    
    You can run make_input.py by typing 'python make_input.py'. 
    You are asked how you would like to create the new input files: 
        a) Use default backgroud values for input parameters 
            a-1) if no, you are asked to choose the parameters you want to change from the default and specify their values
        b) Use default temporal changes of input parameter values 
            b-1) if no, you are asked to enter the duration of the simulation, and start and end time of signal/parameter change event
                Then, you are asked to choose parameters you want to specify the time evolution, and 
                    to specify time and proxy/parameter values at several points. 
                    E.g., when you want to simulate a d18O spike (from 1 to -1 permil) between 20 and 30 kyr with total simulation duration 50 kyr, 
                        you first choose 'd18O' and then enter '0 1', '20e3 1', '25e3 -1', '30e3 1', '50e3 1' line by line. 
                        (You are instructed how to enter these values when you run the script.) 
            b-2) if yes, you are asked to specify the type of simulation you want ('biot', 'diss', 'size', 'iso', corresponding example simulations in model development paper).
        c) Plot temporal changes of input parameter values
            a-1) if yes, you will need module matplotlib. You can check immediately temporal changes of input parameters graphically. 
                Plots are stored in /input/ directory in pdf and svg formats (imp_input.pdf and imp_input.svg). 
    
