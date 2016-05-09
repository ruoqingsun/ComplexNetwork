M = csvread('/Users/ludai/Desktop/Study/Github/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_statistic.csv',1,0)
X = M(:,1)
Y = M(:,2)
[xData, yData] = prepareCurveData( X, Y )
figure
ax = axes()
bar(X,Y,'y','BaseValue',0)
set(ax, 'Xlim', [-1,14])
set(ax, 'XTick', [-1:14])
set(ax, 'Ylim', [0,3500])
set(ax, 'YTick', [0:300:3500])
title('answers distribution')

hold on

ft = fittype( 'exp1' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Display = 'Off';
opts.StartPoint = [4385.16468087357 -0.953468681261366];

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft, opts );

% Plot fit with data.
h = plot( fitresult, xData, yData );
legend( h, 'questionNum vs. answerNum', 'answer-dis', 'Location', 'NorthEast' );
% Label axes
xlabel('number of answers')
ylabel('number of questions')






% hold on 
% ft = fittype( 'smoothingspline' )
%  
% [fitresult, gof] = fit( xData, yData, ft );
%  
% h = plot( fitresult);
% legend( h, 'questionNum vs. answerNum', 'answer-dis', 'Location', 'NorthEast' );
% % Label axes
% xlabel('number of answers')
% ylabel('number of questions')
% hold off





