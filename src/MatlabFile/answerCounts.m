M = csvread('/Users/ludai/Desktop/Study/Github/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_statistic.csv',1,0)
X = M(:,1)
Y = M(:,2)
figure
plot(X,Y)
title('number of answers distribution')
xlabel('number of answers')
ylabel('number of questions')