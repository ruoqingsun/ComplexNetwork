I = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/in_degree_total.csv',1,0)
O = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/out_degree_total.csv',1,0)
hold on;
    mark={'-r','-g'};
    plot(1:5,I(1,1:end),mark{1});
    plot(1:5,O(1,1:end),mark{2});
    legend('Answer','Question');
    title('Question & Answer Distribution by Different User Level')
    xlabel('User Level');
    ylabel('Question/Answer Number');
hold off;