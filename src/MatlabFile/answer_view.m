%R_V = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_view.csv',1,0)
V = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/view_count.csv',0,0)
%A = log(R_V(:,2))
v = V/7135
%x =max(V)
x =log(V)
%scatter(V,A,10)
y = sum(V)
figure
h = area(v)
h(1).FaceColor = [1 0.4 0.4];
axis([0 250 0 0.03])
ax = gca
ax.XTick = [1:20:250]
ax.XTickLabel = [1:20:250]
ax.YTick = [0:0.005:0.03]
ax.YTickLabel = {'0%','0.5%','1%','1.5%','2%','2.5%','3%'}
%set(gca,'xscale','log')
%set(gca,'yscale','log')
xlabel('View-Count')
ylabel('Question Percentage')
title('View-Count Distribution')
