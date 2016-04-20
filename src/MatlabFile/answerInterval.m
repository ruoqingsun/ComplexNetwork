M = csvread('/Users/ludai/Desktop/Study/Github/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_intervals_statistic.csv',1,0)
X = M(:,1)
Y = M(:,2)
figure
plot(X,Y,'-o')
title('time interval for answers')
xlabel('time interval (day)')
ylabel('number of answers')