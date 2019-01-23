%---------------------------------  Project 1 -------------------------
%--------------------------- Submitted by Rajib Dey -------------------------
close all
clc
clear all

n = 100;% number of points
B = 2*pi*2000;% 2000 Hz
dw = B/n;
wc = B; % cut off frequency to denormalize the TF
syms s;
H1=1/(s+1)
H1=expand (H1)
% Denormalized 1st order Butterworth filter TF
DenormH1 = 1/((s/wc)+1)
pretty(DenormH1)
s1=0;
s2=0;
for L = 0:1:n-1
H1=1/((1j*L*dw)/(4000*pi) + 1);
absH1 = abs(H1);
s1 = s1 + (dw * absH1^2); % Signal for 1st order
end
ws = 2*pi*8000; % Sampling frequency 8k Hz
N1 = 0;
% Noise formula for both 1st order TFs
for L = 0:1:n-1
H1total=H1;
H1absolute=abs(H1total);
N1=N1+(dw*H1absolute^2);
end
%Antialiasing SNR for 1st order
SNRa1=10*log10(s1/N1)

%--------------------------------------------------------------------------
% Denormalized 5th and 6th order Butterworth filter TF
H5=1/((1+s)*(1+0.618*s+s^2)*(1+1.618*s+s^2)); % normalized 5th order TF
expand(H5)
% Denormalized 5th order Butterworth filter TF
DenH5 = 1/((s/wc)^5 + (809*(s/wc)^4)/250 +(1308981*(s/wc)^3)/250000 + (1308981*(s/wc)^2)/250000 +(809*(s/wc))/250 + 1);
pretty(DenH5)
S6 = 0;
S5 = 0;
% Signal formula for 5th and 6th order TFs
for L = 0:n-1
H_Aw = 1./(2.53942e-25*(1j.*L.*dw).^6+1.23296e-20*(1j.*L.*dw).^5+2.99319e-16*(1j.*L.*dw).^4+4.60671e-12*(1j.*L.*dw).^3+4.72667e-8*(1j.*L.*dw).^2+3.07463e-4*(1j.*L.*dw).^1+1);
H5 = 1./((1j.*L.*dw).^5./(1024000000000000000*pi^5) +(809.*(1j.*L.*dw).^4)./(64000000000000000*pi^4) +(1308981.*(1j.*L.*dw).^3)./(16000000000000000*pi^3) +(1308981.*(1j.*L.*dw).^2)./(4000000000000*pi^2) +(809.*(1j.*L.*dw))./(1000000*pi) + 1);
absH_Aw = abs(H_Aw);
absH5 = abs(H5);
S6 = S6 + (dw * absH_Aw.^2); % Signal for 6th order
S5 = S5 + (dw * absH5.^2); % Signal for 5th order
end
N6 = 0;
N5 = 0;
% Noise formula for both 5th and 6th order TFs
for L = 0:n-1
H6pos1 = 1./(2.53942e-25*(1j.*(L.*dw-ws)).^6+1.23296e-20*(1j.*(L.*dw-ws)).^5+2.99319e-16*(1j.*(L.*dw-ws)).^4+4.60671e-12*(1j.*(L.*dw-ws)).^3+4.72667e-8*(1j.*(L.*dw-ws)).^2+3.07463e-4*(1j.*(L.*dw-ws)).^1+1);
H6neg1 = 1./(2.53942e-25*(1j.*(L.*dw+ws)).^6+1.23296e-20*(1j.*(L.*dw+ws)).^5+2.99319e-16*(1j.*(L.*dw+ws)).^4+4.60671e-12*(1j.*(L.*dw+ws)).^3+4.72667e-8*(1j.*(L.*dw+ws)).^2+3.07463e-4*(1j.*(L.*dw+ws)).^1+1);
H6pos2 = 1./(2.53942e-25*(1j.*(L.*dw-2*ws)).^6+1.23296e-20*(1j.*(L.*dw-2*ws)).^5+2.99319e-16*(1j.*(L.*dw-2*ws)).^4+4.60671e-12*(1j.*(L.*dw-2*ws)).^3+4.72667e-8*(1j.*(L.*dw-2*ws)).^2+3.07463e-4*(1j.*(L.*dw-2*ws)).^1+1);
H6neg2 = 1./(2.53942e-25*(1j.*(L.*dw+2*ws)).^6+1.23296e-20*(1j.*(L.*dw+2*ws)).^5+2.99319e-16*(1j.*(L.*dw+2*ws)).^4+4.60671e-12*(1j.*(L.*dw+2*ws)).^3+4.72667e-8*(1j.*(L.*dw+2*ws)).^2+3.07463e-4*(1j.*(L.*dw+2*ws)).^1+1);
H6pos3 = 1./(2.53942e-25*(1j.*(L.*dw-3*ws)).^6+1.23296e-20*(1j.*(L.*dw-3*ws)).^5+2.99319e-16*(1j.*(L.*dw-3*ws)).^4+4.60671e-12*(1j.*(L.*dw-3*ws)).^3+4.72667e-8*(1j.*(L.*dw-3*ws)).^2+3.07463e-4*(1j.*(L.*dw-3*ws)).^1+1);
H6neg3 = 1./(2.53942e-25*(1j.*(L.*dw+3*ws)).^6+1.23296e-20*(1j.*(L.*dw+3*ws)).^5+2.99319e-16*(1j.*(L.*dw+3*ws)).^4+4.60671e-12*(1j.*(L.*dw+3*ws)).^3+4.72667e-8*(1j.*(L.*dw+3*ws)).^2+3.07463e-4*(1j.*(L.*dw+3*ws)).^1+1);
H6Total = H6pos1+H6neg1+H6pos2+H6neg2+H6pos3+H6neg3;
absH6Total = abs(H6Total);
H51 = 1./((1j.*(L.*dw-ws)).^5./(1024000000000000000*pi^5) + (809.*(1j.*(L.*dw-ws)).^4)./(64000000000000000*pi^4) + (1308981.*(1j.*(L.*dw-ws)).^3)./(16000000000000000*pi^3) + (1308981.*(1j.*(L.*dw-ws)).^2)./(4000000000000*pi^2) + (809.*(1j.*(L.*dw-ws)))./(1000000*pi) + 1);
H5neg1 =1./((1j.*(L.*dw+ws)).^5./(1024000000000000000*pi^5) +(809.*(1j.*(L.*dw+ws)).^4)./(64000000000000000*pi^4) +(1308981.*(1j.*(L.*dw+ws)).^3)./(16000000000000000*pi^3) +(1308981.*(1j.*(L.*dw+ws)).^2)./(4000000000000*pi^2) +(809.*(1j.*(L.*dw+ws)))./(1000000*pi) + 1);
H52 = 1./((1j.*(L.*dw-2*ws)).^5./(1024000000000000000*pi^5) + (809.*(1j.*(L.*dw-2*ws)).^4)./(64000000000000000*pi^4) +(1308981.*(1j.*(L.*dw-2*ws)).^3)./(16000000000000000*pi^3)+ (1308981.*(1j.*(L.*dw-2*ws)).^2)./(4000000000000*pi^2) +(809.*(1j.*(L.*dw-2*ws)))./(1000000*pi) + 1);
H5neg2 =1./((1j.*(L.*dw+2*ws)).^5./(1024000000000000000*pi^5) +(809.*(1j.*(L.*dw+2*ws)).^4)./(64000000000000000*pi^4) +(1308981.*(1j.*(L.*dw+2*ws)).^3)./(16000000000000000*pi^3)+ (1308981.*(1j.*(L.*dw+2*ws)).^2)./(4000000000000*pi^2) +(809.*(1j.*(L.*dw+2*ws)))./(1000000*pi) + 1);
H5Total = H51 + H5neg1 + H52 + H5neg2;
absH5Total = abs(H5Total);
N6 = N6 + (dw * (absH6Total).^2);% Noise for 6th order
N5 = N5 + (dw * (absH5Total).^2);% Noise for 5th order
end
% Signal to noise ratio of 5th order
SNR5 = 10*log10(S5 ./ N5)
% Signal to noise ratio of 6th order
SNR = 10*log10(S6 ./ N6)
disp('TF for the denormalized butterworth low pass filter is:')
normHs=1./(s^6+3.863705*s^5+7.46410*s^4+9.14162*s^3+7.46410*s^2+3.86370*s+1);
simplify(normHs);
pretty(normHs);
denormHs=1./((s/wc)^6+3.863705*(s/wc)^5+7.46410*(s/wc)^4+9.14162*(s/wc)^3+7.46410*(s/wc)^2+3.86370*(s/wc)+1)
denormHs1=expand(denormHs)
simplify(denormHs1);
pretty(denormHs1);
[N,D] = numden(denormHs1)
%-------------------------------------------------------------------
% Problem b (Sketch the spectrum at 2)
% Initialization
f=-20000:100:20000;
w=2*pi*f;
fs=8000;
ws=2*pi*fs;
% Create Butterworth Filter
Butterworth=inline('1./(2.53942e-25*(j*w).^6+1.23296e-20*(j*w).^5+2.99319e-16*(j*w).^4+4.60671e-12*(j*w).^3+4.72667e-8*(j*w).^2+3.07463e-4*(j*w)+1)','w');
figure(1);
plot(f,abs(Butterworth(w)));
title('Magnitude at 2')
xlabel('Frequency(Hz)');
ylabel('Magnititude of the Spectrum');
figure(2);
plot(f,angle(Butterworth(w)));
title('Phase at 2')
xlabel('Frequency(Hz)');
ylabel('Phase of the Spectrum');
%-------------------------------------------------------------------
% Problem c (Sketch the spectrum at 3)
sample_Butterworth=Butterworth(w+2*ws)+Butterworth(w+ws)+Butterworth(w)+Butterworth(w-ws)+Butterworth(w-2*ws);
figure(3);
plot(f,abs(sample_Butterworth));
title('Magnitude at 3')
xlabel('Frequency(Hz)');
ylabel('Magnititude of the Spectrum');
figure(4);
plot(f,angle(sample_Butterworth));
title('Phase at 3')
xlabel('Frequency(Hz)');
ylabel('Phase of the Spectrum');
%-------------------------------------------------------------------
% Problem d (Sketch the spectrum at 4)
M=(1-sawtooth(w/8000,0.5))/2;
output_4=sample_Butterworth.*M;
figure(5);
plot(f,abs(output_4));
title('Magnitude at 4')
xlabel('Frequency(Hz)');
ylabel('Magnititude of the Spectrum');
figure(6);
plot(f,angle(output_4));
title('Phase at 4')
xlabel('Frequency(Hz)');
ylabel('Phase of the Spectrum');
%------------------------------------------------------------------
% Problem e (Sketch the spectrum at 5)
SH=sinc(f/8000);
output_5=output_4.*SH;
figure(7);
plot(f,abs(output_5));
title('Magnitude at 5')
xlabel('Frequency(Hz)');
ylabel('Magnititude of the Spectrum');
figure(8);
plot(f,angle(output_5));
title('Phase at 5')
xlabel('Frequency(Hz)');
ylabel('Phase of the Spectrum');

%-------------------------------------------------------------------
% Problem f ( Finding the maximum tau ( worst case analysis )
syms tau;
Tsignal = 1/2000;
taumax = solve(10*log10(0.038*Tsignal^2/tau^2)>=60,tau); % From SNRjitter expression
disp('MaxTau = ')
pretty (2*taumax)
%-------------------------------------------------------------------
% Problem g ( Compute SNR quantiz in dB)
n=14;
disp('SNRquantize in dB = ')
SNRquantize = 20*n*log10(2)
SNRquantfinal=6*n
%-------------------------------------------------------------------
% Problem h ( Sketch HRw )
for i = -200:1:200
j = i+201;
f(j) = 100*i;
if i<=-20
HRw(j) = 0;
elseif i >= 20
HRw(j) = 0;
else
HRw(j) = 1 ./ sinc(f(j)./8000);% 8000 refers to 1/taw,taw = 125micro
end
end
figure(9)
plot(f,abs(HRw))
title('Magnitude of HR(w)')
xlabel('Frequency (Hz)')
ylabel('Magnitude')
grid on
grid minor
%-------------------------------------------------------------------
% Problem i ( Sketch spectrum at 6 )
output_6=output_5.*HRw;
figure(10);
plot(f,abs(output_6));
title('Magnitude at 6')
xlabel('Frequency(Hz)');
ylabel('Magnitude of the Spectrum');
figure(11);
plot(f,angle(output_6));
title('Phase at 6')
xlabel('Frequency(Hz)');
ylabel('Phase of the Spectrum');
