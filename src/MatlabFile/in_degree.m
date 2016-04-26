M = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/in_degree_group.csv',1,0)
hold on;
    mark={'-b','-c','-m','-r','-k'};
    for i=1:5
       plot(1:5,M(1:end,i),mark{i});
    end
    legend('Newbie','Learner','User','Professional','Expert');
    title('Answer Distribution By different Level of user')
    xlabel('Answer Number');
    ylabel('Answerer Number');
hold off;

