M = csvread('/Users/ludai/Desktop/Study/Github/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/accpet_answer_time_st.csv',1,0)
X = M(:,1)
Y = M(:,2)
figure
plot(X,Y)
title('Time for getting an accepted answer distribution')
xlabel('time for getting accepted answer')
ylabel('number of questions')