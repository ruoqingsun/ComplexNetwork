edges = csvread('E:/Documents/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/digraph_edges.csv',1,0);
edges = edges';
G = digraph(edges(1, :), edges(2, :), edges(3, :));

outdeg = outdegree(G);
indeg = indegree(G);

scatter(outdeg,indeg,25,'filled')