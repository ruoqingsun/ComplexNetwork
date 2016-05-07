N = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/out_degree_group.csv',1,0)
U = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/users_st.csv',1,0)
M = zeros(4,5)
for j=1:5
    for i=1:4
        M(i,j) = N(i,j)/U(j)
    end
end
h=area(M,'LineStyle',':')
ax = gca
ax.XTick = [1 2 3 4]
ax.YTick = [0 0.5 1 1.5 2 2.5]
ax.YTickLabel = {'0%','50%','100%','150%','200%','250%'};
xlabel('Question Number')
ylabel('Questioner Number Proportion')
legend('Newbie','Learner','User','Professional','Expert','Location','northoutside','Orientation','horizontal')
title('Question Distribution By User Level')
% hold on;
%     mark={'-b','-c','-m','-r','-k'};
%     for i=1:5
%        plot(1:4,M(1:end,i),mark{i});
%     end
%     legend('Newbie','Learner','User','Professional','Expert');
%     
%     
% hold off;