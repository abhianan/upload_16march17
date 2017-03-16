clc;
clear all;
i=input('Enter a number : ');
j=input('Enter a number : ');
A=zeros(i);
for k=1:i
    for m=1:j
        if k>m
            A(k,m)=k+m;
        elseif k==m
            A(k,m)=k*m;
        elseif k<m
            A(k,m)=k-m;
        end
    end
end