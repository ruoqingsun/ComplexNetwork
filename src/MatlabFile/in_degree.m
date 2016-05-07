N = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/in_degree_group.csv',1,0)
U = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/users_st.csv',1,0)
M = zeros(5,5)
for j=1:5
    for i=1:5
        M(i,j) = N(i,j)/U(j)
    end
end
h=area(M,'LineStyle',':')
ax = gca
ax.XTick = [1 2 3 4 5]
ax.YTick = [0 0.5 1 1.5 2 2.5]
ax.YTickLabel = {'0%','50%','100%','150%','200%','250%'};
xlabel('Answer Number')
ylabel('Answerer Number Proportion')
legend('Newbie','Learner','User','Professional','Expert','Location','northoutside','Orientation','horizontal')
title('Answer Distribution By User Level')


