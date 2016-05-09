R_V = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/ques_view.csv',1,0)
R = R_V(:,1)
V = R_V(:,2)
scatter(R,V,4)