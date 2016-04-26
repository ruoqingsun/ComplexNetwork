M = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/out_degree_group.csv',1,0)
hold on;
    mark={'-b','-c','-m','-r','-k'};
    for i=1:5
       plot(1:4,M(1:end,i),mark{i});
    end
    legend('Newbie','Learner','User','Professional','Expert');
    title('Question Distribution By different Level of user')
    xlabel('Question Number');
    ylabel('Questioner Number');
hold off;