% ------- Applications of DSP ----------------
% ------------Project 3 ----------------------
%------------Submitted by---------------------
%-------------Rajib Dey ----------------------
clear;
close all;
clc;
% Definition of the ideal filter
H_low=inline('sinc(2*fc*ts.*n)*2*fc*ts','fc','ts','n');
H_band=inline('sinc(2*fh*ts.*n)*2*fh*ts-sinc(2*fl*ts.*n)*2*fl*ts','fh','fl','ts','n');
H_hil=inline('(1-cos(n*pi))./(n*pi)','n');
H_dif=inline('cos(n.*pi)./(n.*pi)','n');
w_hamming=inline('0.54+0.46*cos(2*pi.*n/L)','L','n');
w_blackman=inline('0.42+0.5*cos(2*pi.*n/L)+0.08*cos(4*pi.*n/L)','n','L');
w_kaiser=inline('besseli(0,b)./besseli(0,a)','a','b');
% -------------------Code for Problem 1-------------------
fs=48000;
f1=9200;
fp=5200;
L=40;
ts=1/fs;
fc=(f1+fp)/2;
n=-1*L/2:L/2;
H_n=H_low(fc,ts,n);
H=H_low(fc,ts,n).*w_hamming(L,n)
% -------------------Plot for the spectrum of the filter-------------------
for i=1:1000
w(i)=pi*fs*i/1000;
z=exp(j*w(i)*ts);
H_final(i)=z^(-1*L/2)*sum(H.*z.^(-n));
end
figure(1);
subplot(2,1,1);
plot(w/(2*pi),abs(H_final));
xlabel('frequency (Hz)');
ylabel('|H(w)|');
title('Magnitude Spectrum');
grid on;
grid minor;
subplot(2,1,2);
plot(w/(2*pi),angle(H_final));
xlabel('frequency(Hz)');
ylabel('phase');
title('Phase Spectrum');
grid on;
grid minor;
% -------------------Code for Problem 2-------------------
9
fs=2000;
fh=550;
fl=250;
L=109;
ts=1/fs;
n=-1*L/2:L/2;
H_n=H_band(fh,fl,ts,n);
H=H_band(fh,fl,ts,n).*w_blackman(n,L)
% -------------------Plot for the spectrum of the filter-------------------
for i=1:1000
w(i)=pi*fs*i/1000;
z=exp(j*w(i)*ts);
H_final(i)=z^(-1*L/2)*sum(H.*z.^(-n));
end
figure(2);
subplot(2,1,1);
plot(w/(2*pi),abs(H_final));
xlabel('frequency(Hz)');
ylabel('|H(w)|');
title('Magnitude Spectrum');
grid on;
grid minor;
subplot(2,1,2);
plot(w/(2*pi),angle(H_final));
xlabel('frequency(Hz)');
ylabel('Phase');
title('Phase Spectrum');
grid on;
grid minor;
% -------------------Code for Problem 3-------------------
fs=10/(2*pi);
a=3;
L=80;
ts=1/fs;
n1=-L/2:-1;
b1=a.*(1-(2.*n1./L).^2).^0.5;
H1=H_hil(n1).*w_kaiser(a,b1);
n2=1:L/2;
b2=a.*(1-(2.*n2./L).^2).^0.5;
H2=H_hil(n2).*w_kaiser(a,b2);
%------------------- Plot for the spectrum of the filter-----------------
for i=1:1000
w(i)=pi*fs*i/1000;
z=exp(j*w(i)*ts);
H_final(i)=z^(-1*L/2)*(sum(H1.*z.^(-n1))+sum(H2.*z.^(-n2)));
end
figure(3);
subplot(2,1,1);
plot(w,abs(H_final));
xlabel('frequency(Hz)');
ylabel('|H(w)|');
title('Magnitude Spectrum');
grid on;
grid minor;
subplot(2,1,2);
plot(w,angle(H_final));
xlabel('frequency(Hz)');
ylabel('Phase');
title('Phase Spectrum');
grid on;
grid minor;
% -------------------Code for Problem 4-------------------
fs=1;
ws=2*pi;
L=20;
ts=1/fs;
n1=-L/2:-1;
H1=H_dif(n1)
n2=1:L/2;
H2=H_dif(n2)
% -------------------Plot the spectrum of the filter-------------------
for i=1:2001
w(i)=pi*fs*(i-1001)/1000;
z=exp(j*w(i)*ts);
H_i(i)=j*w(i)./ws;
H_final(i)=z.^(-1*L/2).*(sum(H1.*z.^(-n1))+sum(H2.*z.^(-n2)));
H_ham(i)=z.^(-1*L/2).*(sum(H1.*w_hamming(L,n1).*z.^(-n1))+sum(H2.*w_hamming(L,n2).*z.^(-n2)));
end
figure(4);
subplot(3,2,1);
plot(w/(2*pi),abs(H_i));
axis([-0.6 0.6 0 1]);
xlabel('frequency(Hz)');
ylabel('|H(w)|');
title('Magnitude Spectrum');
grid on;
grid minor;
subplot(3,2,2);
plot(w/(2*pi),angle(H_i));
axis([-0.6 0.6 -2 4]);
xlabel('f(Hz)');
ylabel('Phase');
title('Phase Spectrum');
grid on;
grid minor;
subplot(3,2,3);
plot(w/(2*pi),abs(H_final));
xlabel('frequency(Hz)');
ylabel('|H(w)|');
title('Magnitude Spectrum');
grid on;
grid minor;
subplot(3,2,4);
plot(w/(2*pi),angle(H_final));
xlabel('frequency(Hz)');
ylabel('Phase');
title('Phase Spectrum');
grid on;
grid minor;
subplot(3,2,5);
plot(w/(2*pi),abs(H_ham));
xlabel('frequency(Hz)');
ylabel('|H(w)|');
title('Magnitude Spectrum');
grid on;
grid minor;
subplot(3,2,6);
plot(w/(2*pi),angle(H_ham));
xlabel('frequency(Hz)');
ylabel('Phase');
title('Phase Spectrum');
grid on;
grid minor;
%-------------------End of the Program-------------------%

