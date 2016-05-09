M = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/answer_by_view.csv',0,1)
N = M'
low = M(1,:)
mid = M(2,:)
high = M(3,:)
A = 1:13
h = bar(N)
legend('low-level ViewCount','mid-level ViewCount ','high-level ViewCount')
xlabel('Answer-Count')
ylabel('Question Percentage')
title('Answer-count Distribution by View-count Level')
% figure
% hold on
%     h1 = plot(A,low)
%     h2 = plot(A,mid)
%     h3 = plot(A,high)
% hold off