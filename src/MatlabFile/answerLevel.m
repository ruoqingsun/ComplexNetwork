M = csvread('E:/Documents/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_level.csv',1,0)
% M = csvread('E:/Documents/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_accepted_level.csv',1,0)
M = M'
S = sum(M,1)
for i = 1:size(M,1)
    for j = 1:size(M,2)
        Percent(i,j) = M(i,j)/S(j)*100
    end
end
        
figure
plot(Percent)
title('Helpers Knowledge Level Distribution For All Answers')
xlabel('Answerer Knowledge Level')
ylabel('Group Counts')
legend('Newbie','Learner','User','Professional','Expert')

yticks = [get(gca,'ytick')]';
percentsy = repmat('%', length(yticks),1);
yticklabel = [num2str(yticks) percentsy];
set(gca,'yticklabel',yticklabel)%
xticklabel = {'Newbie','','Learner','','User','','Professional','','Expert'};
set(gca,'xticklabel',xticklabel)
