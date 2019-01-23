%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% EEL 5513 Applications of DSP
% Project 5
% Submitted by Rajib Dey
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
% Code for Qu. no. 1---------------------------------------

% Initializing
clear;
clc;
c=[1,2,3];

% for n=100
n=100;
x=randn(1,n);
d=conv(x,c);
d=d(1:n);

% Generating R & P Matrix
for k=1:3
    x_temp=[zeros(1,k-1),x(1:n-k+1)];
    r(k)=x*x_temp'/n;
    P(k)=d*x_temp'/n;
end

for i=1:3
    for j=1:3
        R(i,j)=r(abs(i-j)+1);
    end
end
% Displaying the result
display('the result of Problem1 for n=100');
w_Problem1=inv(R)*P'
% for n=1000
n=1000;
x=randn(1,n);
d=conv(x,c);
d=d(1:n);
% Generating R & P Matrix
for k=1:3
x_temp=[zeros(1,k-1),x(1:n-k+1)];
r(k)=x*x_temp'/n;
P(k)=d*x_temp'/n;
end
for i=1:3
for j=1:3
R(i,j)=r(abs(i-j)+1);
end
end
% Displaying the result
display('the result of Problem1 for n=1000');
w_Problem1=inv(R)*P'

% Code for Qu. no. 2---------------------------------------
clear;
c=[1,2,3];
% Initializing for n=150
n=150;
x=randn(1,n);
d=conv(x,c);
d=d(1:n);

mu=0.02;
w0(1)=0;
w1(1)=0;
w2(1)=0;
w0(2)=0;
w1(2)=0;
w2(2)=0;
w0(3)=0;
w1(3)=0;
w2(3)=0;

% LMS Algorithm
for k=3:n
    y(k)=w0(k)*x(k)+w1(k)*x(k-1)+w2(k)*x(k-2);
    e(k)=d(k)-y(k);
    
    w0(k+1)=w0(k)+2*mu*e(k)*x(k);
    w1(k+1)=w1(k)+2*mu*e(k)*x(k-1);
    w2(k+1)=w2(k)+2*mu*e(k)*x(k-2);
end

% Plot
i=1:n;
figure;
plot(i,w0(i),'-.',i,w1(i),'.',i,w2(i),'-');
legend('w0(n)','w1(n)','w2(n)');
xlabel('Iteration');
title('Problem 2');
grid on;
grid minor;
% Displaying the result
display('the result of Problem1 for n=150');
w_Problem2=[w0(k+1),w1(k+1),w2(k+1)]

% Code for Qu. no. 3---------------------------------------
clear;
c=[1,2,3];
% Initializing for n=150
n=150;
x=randn(1,n);
d=conv(x,c);
d=d(1:n);
mu=0.02;
w0(1)=0;
w1(1)=0;
w2(1)=0;
w0(2)=0;
w1(2)=0;
w2(2)=0;
w0(3)=0;
w1(3)=0;
w2(3)=0;

% HA Algorithm
for k=3:n
    y(k)=w0(k)*x(k)+w1(k)*x(k-1)+w2(k)*x(k-2);
    e(k)=d(k)-y(k);
    mu=1/(2*(x(k)^2+x(k-1)^2+x(k-2)^2));
    
    w0(k+1)=w0(k)+2*mu*e(k)*x(k);
    w1(k+1)=w1(k)+2*mu*e(k)*x(k-1);
    w2(k+1)=w2(k)+2*mu*e(k)*x(k-2);
end

% Plotting
i=1:n;
figure;
plot(i,w0(i),'-.',i,w1(i),'.',i,w2(i),'-');
legend('w0(n)','w1(n)','w2(n)');
xlabel('Iteration');
title('Problem 3: HA Algorithm');
grid on;
grid minor;
% Displaying the result
display('the result of Problem1 for n=150');
w_Problem3=[w0(k+1),w1(k+1),w2(k+1)]

% Code for Qu. no. 4---------------------------------------
clear;
c=[1,2,3];
% Initializing for n=150
n=150;
x=randn(1,n);
d=conv(x,c);
d=d(1:n);
mu=0.02;
w0(1)=0;
w1(1)=0;
w2(1)=0;
w0(2)=0;
w1(2)=0;
w2(2)=0;
w0(3)=0;
w1(3)=0;
w2(3)=0;
% LMS Algorithm
for k=3:n
    y(k)=w0(k)*x(k)+w1(k)*x(k-1)+w2(k)*x(k-2);
    eta(k)=0.2*sin(2*pi*k/16);
    e(k)=d(k)+eta(k)-y(k);
    
    w0(k+1)=w0(k)+2*mu*e(k)*x(k);
    w1(k+1)=w1(k)+2*mu*e(k)*x(k-1);
    w2(k+1)=w2(k)+2*mu*e(k)*x(k-2);
end
% Plotting
i=1:n;
figure;
plot(i,w0(i),'-.',i,w1(i),'.',i,w2(i),'-');
legend('w0(n)','w1(n)','w2(n)');
xlabel('Iteration');
title('Problem 4');
figure;
plot (e(i))
xlabel ('n');
title('e(n) as a function of n');
grid on;
grid minor;
% Displaying the result
display('the result of Problem1 for n=150');
w_Problem4=[w0(k+1),w1(k+1),w2(k+1)]
