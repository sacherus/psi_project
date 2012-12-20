
function Y = newton(A)
n=size(A)
n=n(1)
matrixx=zeros(n,n+1)

for i=1:n
  matrixx(i,1) = A(i,1)
  matrixx(i,2) = A(i,2)
end  

for i=3:(n+1)
  for j=1:(n-i+2)
    matrixx(j,i) = (matrixx(j+1,i-1) - matrixx(j,i-1))/(matrixx(i+j-2,1)-matrixx(j,1))
  end  
end  
Y = matrixx

endfunction