A = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/in_degree_total.csv',1,0)
Q = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/out_degree_total.csv',1,0)
U = csvread('/Users/ludai/Desktop/Study/GitHub/ComplexNetwork/src/StackOverflowCrawler/QuestionCrawler/users_st.csv',1,0)
N_A = zeros(1,5)
N_Q = zeros(1,5)
for i=1:5
    N_A(i) = A(i)/U(i)
    N_Q(i) = Q(i)/U(i)
end

[a_xData, a_yData] = prepareCurveData( 1:5, N_A )
[q_xData, q_yData] = prepareCurveData( 1:5, N_Q )

hold on 
ft = fittype( 'smoothingspline' )
[fitresult_a, gof_a] = fit( a_xData, a_yData, ft )
[fitresult_q, gof_q] = fit( q_xData, q_yData, ft )
h_a=plot( fitresult_a, 'k', a_xData, a_yData, 'kd')
h_q=plot( fitresult_q, 'm', q_xData, q_yData, 'mo')
legend('NormAnswer','answerCurve','NormQuestion','questionCurve','Location','northoutside','Orientation','horizontal')
title('Question & Answer Distribution by User Level')
ax = gca;
ax.XTick = [1 2 3 4 5]
ax.XTickLabel = {'Newbie','Learner','User','Professional','Expert'};
xlabel('User Level');
ylabel('Normalized Question/Answer Number');
hold off


% hold on;
%     mark={'-o','-*'};
%     plot(1:5,N_A(1,1:end),mark{1});
%     plot(1:5,N_Q(1,1:end),mark{2});
%     legend('Answer','Question');
%     title('Question & Answer Distribution by Different User Level')
%     xlabel('User Level');
%     ylabel('Question/Answer Number');
% hold off;