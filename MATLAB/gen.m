function [a b c d]=gen(A)
a=det(A)
b=inv(A)
c=rank(A)
d=A'