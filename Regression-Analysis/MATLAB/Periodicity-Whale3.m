%To find a livescript from the MATLAB help pages, type whalefile. 
%Find Regions of Interest in Whale Song Example
%or look up Fourier Transforms

whaleFile = fullfile(matlabroot,'examples','matlab','data','bluewhale.au');
[x,fs] = audioread(whaleFile);%convert to data

%[w,fs] = audioread(whaleFile);
%whale = timetable(seconds((0:length(w)-1)'/fs),w);
%soundsc(w,fs)
% To hear, type soundsc(w,fs)
figure(1)
clf
%length(x)
%count=1:length(x);
%plot(count,x)
plot(x)
%If Y is a vector, then the x-axis scale ranges from 1 to length(Y).
xlabel('Sample Number/time in seconds')
ylabel('Amplitude')
title('Blue whale data');


moan1 = x(2.45e4:3.10e4);
t1 = 10*(0:1/fs:(length(moan1)-1)/fs);
figure(2)
clf
plot(t1,moan1)
xlabel('Time (seconds)')
ylabel('Amplitude')
title('First moan - blue whale data');

xlim([0 t1(end)])

m1 = length(moan1);
n = pow2(nextpow2(m1));
y1 = fft(moan1,n);

f1 = (0:n-1)*(fs/n)/10;
power1 = abs(y1).^2/n;

figure(3)
clf
plot(f1(1:floor(n/2)),power1(1:floor(n/2)))
xlabel('Frequency (Hz)')
ylabel('Power')
title('First moan - blue whale data');


moan2 = x(4.45e4:5.40e4);
t2 = 10*(0:1/fs:(length(moan2)-1)/fs);

figure(4)
clf
plot(t2,moan2)
xlabel('Time (seconds)')
ylabel('Amplitude')
xlim([0 t2(end)])
title('Second moan - blue whale data');


m2 = length(moan2);
n = pow2(nextpow2(m2));
y2 = fft(moan2,n);

f2= (0:n-1)*(fs/n)/10;
power2 = abs(y2).^2/n;

figure(5)
clf
hold on
plot(f2(1:floor(n/2)),power2(1:floor(n/2)))
xlabel('Frequency (Hz)')
ylabel('Power')
title('Second moan - blue whale data');

trill = x(0.4e4:1.34e4);
t3 = 10*(0:1/fs:(length(trill)-1)/fs);
figure(6)
clf
plot(t3,trill)
xlabel('Time (seconds)')
ylabel('Amplitude')
xlim([0 t3(end)])
title('Trill - blue whale data');

m3 = length(trill);
n = pow2(nextpow2(m3));
y3 = fft(trill,n);

f3 = (0:n-1)*(fs/n)/10;
power3 = abs(y3).^2/n;

figure(7)
clf
plot(f3(1:floor(n/2)),power3(1:floor(n/2)))
xlabel('Frequency (Hz)')
ylabel('Power')
title('Trill - blue whale data');