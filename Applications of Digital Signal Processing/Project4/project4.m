%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% EEL 5513 Applications of DSP
% Project 4
% Submitted by Rajib Dey
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Code for Qu. no. 1---------------------------------------
N=16;
n=1:N;
x1=cos(2.*pi.*n./16)+2.*cos(4.*pi.*n./16);
x2=sin(2.*pi.*n./16)+2.*sin(4.*pi.*n./16);
DFT_x1 = []; DFT_x2 = [];
IDFT_X1 = []; IDFT_X2 = [];
for k=1:N
X1(k)=sum(x1(n).*exp(-j.*(2.*pi./N).*k.*n));
X2(k)=sum(x2(n).*exp(-j.*(2.*pi./N).*k.*n));
x1_IDFT(k)=sum(x1(n).*exp(j.*(2.*pi./N).*k.*n));
x2_IDFT(k)=sum(x2(n).*exp(j.*(2.*pi./N).*k.*n));
end
figure(1)
subplot(2,1,1);
plot(abs(X1));
xlabel('k');
ylabel('Amplitude of DFT for x1');
subplot(2,1,2);
plot(angle(X1));
xlabel('k');
ylabel('Phase of DFT for x1');
figure(2)
subplot(2,1,1);
plot(abs(X2));
xlabel('k');
ylabel('Amplitude of DFT for x2');
subplot(2,1,2);
plot(angle(X2));
xlabel('k');
ylabel('Phase of DFT for x2');
figure(3)
subplot(2,1,1);
plot(abs(x1_IDFT));
xlabel('k');
ylabel('Amplitude of IDFT for x1');
subplot(2,1,2);
plot(angle(x1_IDFT));
xlabel('k');
ylabel('Phase of IDFT for x1');
figure(4)
subplot(2,1,1);
plot(abs(x2_IDFT));
xlabel('k');
ylabel('Amplitude of IDFT for x2');
subplot(2,1,2);
plot(angle(x2_IDFT));
xlabel('k');
ylabel('Phase of IDFT for x2');
% Code for Qu. no. 2a---------------------------------------
for n=0:15;
x(n+1)=4.*sin(2.*pi.*n./8);
if n-1<0
t1=0;
else
t1=x(n);
end
if n-2<0
t2=0;
else
t2=x(n-1);
end
if n-3<0
t3=0;
else
t3=x(n-2);
end
y(n+1)=x(n+1)+0.5*t1+0.5^2*t2+0.5^3*t3;
end

figure('Name','Using Difference Equation','NumberTitle','off','Position',[100 100 1000 600]);
plot(0:1:15,y);
grid on;
grid minor;
xlabel('n','FontSize',12,'FontWeight','bold');
ylabel('y(n)','FontWeight','bold');
title('Using Difference Equation');
% Code for Qu. no. 2b---------------------------------------
i=0:3;
h=0.5.^i;
for n=0:15;
x(n+1)=4.*sin(2.*pi.*n./8);
if n-1<0
t1=0;
else
t1=x(n);
end
if n-2<0
t2=0;
else
t2=x(n-1);
end
if n-3<0
t3=0;
else
t3=x(n-2);
end
y(n+1)=h*[x(n+1);t1;t2;t3];
end

figure('Name','Using Convolution Summation','NumberTitle','off','Position',[100 100 1000 600]);
plot(0:1:15,y);
grid on;
grid minor;
xlabel('n','FontSize',12,'FontWeight','bold');
ylabel('y(n)','FontWeight','bold');
title('Using Convolution Summation');
% Code for Qu. no. 2c---------------------------------------
i = 0:1:3;
h = 0.5.^i;
n = 0:1:15;
h=[h,zeros(1,12)];
x(n+1) = 4.*sin(2.*pi.*n./8);
X=fft16(x);
H=fft16(h);
y=ifft16(1/16.*X.*H);

figure('Name','Using FFT','NumberTitle','off','Position',[100 100 1000 600]);
plot(y);
grid on;
grid minor;
xlabel('n','FontSize',12,'FontWeight','bold');
ylabel('y(n)','FontWeight','bold');
title('Using FFT');
% Code for Qu. no. 3---------------------------------------
figure('Name','Compute and Compare Engery using 8 point DFT in Time & Freq.Domain','NumberTitle','off','Position',[100 100 1000 600]);
n = 0:1:7;
subplot(1,2,1);
x_3 = 3*sin(6*pi*n/16);
plot(0:1:7,x_3,'b-');
hold on;
x_3_sq = x_3.^2;
plot(0:1:7,x_3_sq,'b--');
hold on;
E_t = sum(x_3_sq);
plot(0:0.001:7,E_t,'r.');
hold off;
grid on;
grid minor;
xlabel('n','FontSize',12,'FontWeight','bold');
ylabel('Values','FontWeight','bold');
title('Energy in Time Domain');
legend('\chi(n)','\chi^2(n)','E(\chi(n))','Location','Best');
subplot(1,2,2);
X_3 = fft(x_3,8);
plot(0:1:7,abs(X_3),'b-');
hold on;
X_3_sq = abs(X_3.^2);
plot(0:1:7,X_3_sq,'b--');
hold on;
E_f = 1/8*sum(X_3_sq);
plot(0:0.001:7,E_f,'r.');
hold off;
grid on;
grid minor;
xlabel('k','FontSize',16,'FontWeight','bold');
ylabel('Values','FontWeight','bold');
title('Energy in Frequency Domain');
legend('X(k)','X^2(k)','E(X(k))','Location','Best');
% Code for Qu. no. 4---------------------------------------
figure('Name','Fourier Coefficients using Exact','NumberTitle','off','Position',[100 100 1000 600]);
k = 1:1:10;
X_k_a = -(1-cos(k.*pi))./(k.*pi).^2;

subplot(2,1,1);
plot(0:1:9,abs(X_k_a));
grid on;
grid minor;
xlabel('k','FontSize',16,'FontWeight','bold');
ylabel('|X_e(k)|','FontWeight','bold');
title('Magnitude plot of FFT when \chi(n) \rightarrow X_e(k)');
subplot(2,1,2);
plot(0:1:9,angle(X_k_a));
grid on;
grid minor;
xlabel('k','FontSize',16,'FontWeight','bold');
ylabel('Angle of X_e(k)','FontWeight','bold');
title('Phase plot of FFT when \chi(n) \rightarrow X_e(k)');
figure('Name','Fourier Coefficients using 64 FFT','NumberTitle','off','Position',[100 100 1000 600]);
n = 0:1:63;
x_3_b = 1-abs(1-n./32);
X_3_b = fft(x_3_b)/64;
subplot(2,1,1);
plot(0:1:63,abs(X_3_b));
grid on;
grid minor;
xlabel('k','FontSize',16,'FontWeight','bold');
ylabel('|X_6_4(k)|','FontWeight','bold');
title('Magnitude plot of 64-FFT');
subplot(2,1,2);
plot(0:1:63,angle(X_3_b));
grid on;
grid minor;
xlabel('k','FontSize',16,'FontWeight','bold');
ylabel('Angle of X_6_4(k)','FontWeight','bold');
title('Phase plot of 64-FFT');
figure('Name','Fourier Coefficients using 256 FFT','NumberTitle','off','Position',[100 100 1000 600]);
n = 0:1:255;
x_3_256b = 1-abs(1-n./128);
X_3_256b = fft(x_3_256b)/256;

subplot(2,1,1);
plot(0:1:255,abs(X_3_256b));
grid on;
grid minor;
xlabel('k','FontSize',16,'FontWeight','bold');
ylabel('|X_2_5_6(k)|','FontWeight','bold');
title('Magnitude plot of 256-FFT');
subplot(2,1,2);
plot(0:1:255,angle(X_3_256b));
grid on;
grid minor;
xlabel('k','FontSize',16,'FontWeight','bold');
ylabel('Angle of X_2_5_6(k)','FontWeight','bold');
title('Phase plot of 256-FFT ');
