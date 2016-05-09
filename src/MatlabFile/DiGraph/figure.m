x = 1:1:24
y1 = level_1 / 196
y2 = level_2 /45
y3 = level_3/41
y4 = level_4/20
y5 = level_5/33

A = zeros(24,5)
A(:,1) = y1
A(:,2) = y2
A(:,3) = y3
A(:,4) = y4
A(:,5) = y5
S = sum(A,1)
% plot the loglog scale figure
% loglog(x,y1,x,y2,x,y3,x,y4,x,y5)

%plot the PDF figure
% [f1,x1] = ksdensity(y1);
% [f2,x2] = ksdensity(y2);
% [f3,x3] = ksdensity(y3);
% [f4,x4] = ksdensity(y4);
% [f5,x5] = ksdensity(y5);
% plot(x1,f1,'b',x2,f2,'g',x3,f3,'r',x4,f4,'c',x5,f5,'m')

% plot(x,y1,'b',x,y2,'g',x,y3,'r',x,y4,'c',x,y5,'m')

% plot bar figure of different answer time intervals
bar3(A)
% hold on
% bar3(x,y2,'g')
% hold on
% bar3(x,y3,'r')
% hold on
% bar3(x,y4,'c')
% hold on
% bar3(x,y5,'m')



legend('Newbie','Learner','User','Professional','Expert')
title('Time interval from question to the accepted answer(Normalized)')
ylabel('Hours')
xlabel('Levels')