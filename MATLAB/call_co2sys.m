%% function to call co2sys 
%% this code is developed by modifiyng an example file in co2sys

% This is an example of the use of CO2SYS. Have a look at the code

% Changes in v1.01:
% - fixed a silly bug that prevented the resulting figures to be drawn.
%
% Steven van Heuven. svheuven@gmail.com
function [co2,hco3,co3,ph,omega,domega_ddic,domega_dalk] = call_co2sys(n,alk,dic,tempi,depi,sali)
% expecting alk and dic in mol/cm3, tempi in C, depi in km and sali in g/kg 
xlat = 0;
presi = dep2pres(depi*1e3,xlat); % presi in db while depi in km   
% presi = depi*1e3;
rho = densatp(sali,tempi,presi); % g/cm3

% disp(' ')
% disp('This is an example of the use of CO2SYS.m')
% disp('that uses its ability to process vectors of data.')
% disp(' ')
% disp('We will generate a figure that shows the sensitivity of pH and pCO2')
% disp(' to changes in DIC, while keeping everything else constant')
% disp(' ')
% disp('(Addional info: alk=2400, si=50, po4=2, dissociation constats: Mehrbach Refit)')
% disp(' ')
%%% alk conversion from mol/cm3 to umol/kgSW  
par1type =    1; % The first parameter supplied is of type "1", which is "alkalinity"
% par1     = 2295; % value of the first parameter
par1     = alk./rho * 1e3*1e6; % value of the first parameter
% par1     = [2000:100:2500]; % value of the first parameter
par2type =    2; % The first parameter supplied is of type "1", which is "DIC"
% par2     = 2154; % value of the second parameter, which is a long vector of different DIC's!
par2     = dic./rho * 1e6*1e3; % value of the second parameter, which is a long vector of different DIC's!
% par2     = [2000:100:2500]; % value of the second parameter, which is a long vector of different DIC's!
% sal      =   35; % Salinity of the sample
sal      =   sali; % Salinity of the sample
tempin   =    tempi; % Temperature at input conditions
presin   =presi; % Pressure    at input conditions
tempout  =    tempi; % Temperature at output conditions - doesn't matter in this example
presout  =presi; % Pressure    at output conditions - doesn't matter in this example
sil      =    0; % Concentration of silicate  in the sample (in umol/kg)
po4      =    0; % Concentration of phosphate in the sample (in umol/kg)
pHscale  =    1; % pH scale at which the input pH is reported ("1" means "Total Scale")  - doesn't matter in this example
k1k2c    =    10; % Choice of H2CO3 and HCO3- dissociation constants K1 and K2 ("4" means "Mehrbach refit")
kso4c    =    3; % Choice of HSO4- dissociation constants KSO4 ("1" means "Dickson")

% addpath (pwd)
% addpath (strcat(pwd,'\CO2SYS-MATLAB\src'))
% Do the calculation. See CO2SYS's help for syntax and output format
A=CO2SYS(par1,par2,par1type,par2type,sal,tempin,tempout,presin,presout,sil,po4,pHscale,k1k2c,kso4c);
% B=derivnum('par1',par1,par2,par1type,par2type,sal,tempin,tempout,presin,presout,sil,po4,pHscale,k1k2c,kso4c); % ALK derivative

% "ph,    pCO2,    fCO2,    CO2,    HCO3,    CO3,    OmegaAr,    OmegaCc,    rho            (umol/kgSW, uatm)"
% for i=1:n
    % fprintf ("%e  %e  %e  %e  %e  %e  %e  %e\n" ...
        % , A(i,18), A(i,19), A(i,20),A(i,23),A(i,21),A(i,22), A(i,31),A(i,30),rho);
% end 

ph = A(1:n,18);
co2 = A(1:n,23);
hco3 = A(1:n,21);
co3 = A(1:n,22);
omega = A(1:n,30);

ph = 10.^(-ph);
co2 = co2*1e-6/1e3*rho; % umol/kg --> mol/g --> mol/cm3
hco3 = hco3*1e-9*rho;
co3 = co3*1e-9*rho;

dev = 1e-8;
par1 = alk /rho * 1e3*1e6 * (1. + dev); 
A=CO2SYS(par1,par2,par1type,par2type,sal,tempin,tempout,presin,presout,sil,po4,pHscale,k1k2c,kso4c);
domega = (A(1:n,30) - omega(:));
dalk = transpose(par1 - alk/rho * 1e3*1e6);

domega_dalk = domega ./ dalk * 1e3*1e6/rho ; 

par1 = alk./rho * 1e3*1e6;
par2 = dic./rho * 1e3*1e6 * (1. + dev); 
A=CO2SYS(par1,par2,par1type,par2type,sal,tempin,tempout,presin,presout,sil,po4,pHscale,k1k2c,kso4c);
domega = (A(1:n,30) - omega(:));
ddic = transpose(par2 - dic/rho * 1e3*1e6);
domega_ddic = domega ./ ddic * 1e3*1e6/rho ;  

ph = transpose(ph);
co2 = transpose(co2);
hco3 = transpose(hco3);
co3 = transpose(co3);
omega = transpose(omega);
domega_ddic = transpose(domega_ddic);
domega_dalk = transpose(domega_dalk);
% figure; clf
% subplot(1,2,1)
% plot(par2,A(:,4),'r.-') % The calculated pCO2's are in the 4th column of the output A of CO2SYS
% xlabel('DIC'); ylabel('pCO2 [uatm]')
% subplot(1,2,2)
% plot(par2,A(:,3),'r.-') % The calculated pH's are in the 3th column of the output A of CO2SYS
% xlabel('DIC'); ylabel('pH')

% disp('DONE!')
% disp(' ')
% disp('Type "edit CO2SYSexample1" to see what the syntax for this calculation was.')
% disp(' ')

end 