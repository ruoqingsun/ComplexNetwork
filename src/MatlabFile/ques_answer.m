R_V = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/ques_answer.csv',1,0)
R = R_V(:,1)
V = R_V(:,2)


scatter(R,V)
set(gca,'xscale','log')
set(gca,'yscale','log')
xlabel('Qestioner Reputation')
ylabel('Answer Reputation')
