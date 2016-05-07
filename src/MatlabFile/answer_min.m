N = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_min.csv',0,0)
N = N'
h = area(N,'LineStyle',':')
h(1).FaceColor = [0 0.75 0.75];
ax = gca
ax.XTick = [1:60:1440]
ax.XTickLabel = [1:24]
xlabel('Hour')
ylabel('Number of Answers')
title('New Answers Every Hour in March 1st')

