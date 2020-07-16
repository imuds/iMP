function p80 = dep2pres(dpth,xlat)
    % p80(dpth,xlat)

    % Compute Pressure from depth using Saunder's (1981) formula with eos80.

    % Reference:
    % Saunders, Peter M. (1981) Practical conversion of pressure
    % to depth, J. Phys. Ooceanogr., 11, 573-574, (1981)

    % Coded by:
    % R. Millard
    % March 9, 1983
    % check value: p80=7500.004 dbars at lat=30 deg., depth=7321.45 meters

    % Modified (slight format changes + added ref. details):
    % J. Orr, 16 April 2009
    
    % Converted from fortran (mocsy/src/p80.f90) to MATLAB by Y. Kanzaki, 2019
  
    pi=3.141592654;
    plat = abs(xlat*pi/180.);
    d  = sin(plat);
    c1 = 5.92e-3+d^2 * 5.25e-3;
    p80 = ((1-c1)-sqrt(((1-c1)^2)-(8.84e-6*dpth))) / 4.42e-6;  % return db
end 