% EXAMPLE
%
%   ***********************************************************************
%   *** DEFAULT iMP MODEL PARAMETER SETTINGS ******************************
%   ***********************************************************************
%
%   Edit this file directly (and rename) to change experiment settings
%   NOTE: QUESTIONS HAVE CAN TAKE true OR false AS VALID SETTINGS
%
%   ***********************************************************************

% *********************************************************************** %
% *** USER SETTINGS ***************************************************** %
% *********************************************************************** %
%
% *** specify boundary conditions *************************************** %
%
% PARAMATER = VALUE;        % [DEFAULT VALUE] BRIEF DESCRIPTION [UNITS]
user_cc_rain_flx_in=10.0;   % [11.0] influx of CaCO3 [umol cm-2 yr-1]
user_rainratio_in=1.17;     % [1.17] assumed OM/CaCO3-ratio [dimensionless]
user_dep_in=3.5;            % [3.5] seafloor water depth [km]
user_alk=2412.0;            % [2412.0] seaflood ALK [umol kg-1]
user_dic=2278.0;            % [2278.0] seafloor DIC [umol kg-1]
user_o2=168.0;              % [168.0] seafloor O2 [umol kg-1]
user_ca=10.29;              % [10.29] seafloor Ca [mmol kg-1]
%
% *** specify model configuration *************************************** %
%
user_bioturbation=5;        % [5] bioturbation optoin [0/1/2/3/4/5]
user_oxonly_in=false;       % [false] select 'oxic only' model [true/false]
%
% *** specify model ouput *********************************************** %
%
user_plot=true;             % [true] create summary plots [true/false]
%
% *** time-dependent (signal processing) settings *********************** %
%
user_filename_proxyin='';
%
% *** numerical/model solution settings ********************************* %
%
% PARAMATER = VALUE;   % [DEFAULT VALUE] BRIEF DESCRIPTION [UNITS]
dt_in=1.0E8;           % [1.0E8] time step to start simulation with [yr]
def_disp=false;
def_dispfull=false;
def_disperror=false;
def_dispwarnings=false;
%
% *********************************************************************** %
