nodes = csvread('E:/Documents/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/digraph_weights_combination.csv',1,0);
nodes = nodes';

outdeg = nodes(1, :);
indeg = nodes(2, :);
sizes = log(nodes(3, :)+1)*25;

% [fitresult, gof, xData, yData]=in_and_out_degree_distribution(indeg, outdeg, sizes)
scatter(outdeg,indeg,sizes)