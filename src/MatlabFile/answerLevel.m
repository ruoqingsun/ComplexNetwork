M = csvread('E:/Documents/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_level.csv',1,0)
M = M'
S = sum(M,1)
for i = 1:size(M,1)
    for j = 1:size(M,2)
        Percent(i,j) = M(i,j)/S(j)
    end
end
        
figure
plot(Percent)
title('Time for getting an accepted answer distribution')
xlabel('Questioner Level')
ylabel('Answer Level')
legend('Newbie','Learner','User','Professional','Export')