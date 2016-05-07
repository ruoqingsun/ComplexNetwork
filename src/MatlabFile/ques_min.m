N = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/ques_min.csv',0,0)
N = N'
area(N,'LineStyle',':')
ax = gca
ax.XTick = [1:60:1440]
ax.XTickLabel = [1:24]
xlabel('Hour')
ylabel('Number of Questions')
%legend('Newbie','Learner','User','Professional','Expert','Location','northoutside','Orientation','horizontal')
title('New Questions Every Hour in March 1st')
%max = max(N)
