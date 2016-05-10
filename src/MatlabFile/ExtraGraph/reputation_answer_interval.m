data = csvread('E:/Documents/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/reputation_answer_interval.csv',1,0);
data=data'
scatter(data(1,:)+1, data(2,:)+1, 1000,'o')

set(gca,'xscale','log');
set(gca,'yscale','log');