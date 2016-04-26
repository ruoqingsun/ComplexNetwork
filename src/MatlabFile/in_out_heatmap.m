M = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/in_out.csv',1,0)

colormap('hot');
imagesc(M);
colorbar;
title('Answerer Heatmap')
%axis([0 1 0 1]);
%gca.XTick = min(pca_num):10:max(pca_num);
xlabel('Feature Size (Using PCA)');
ylabel('Test Error');
xlabel('Answer Number');
ylabel('Question Level');