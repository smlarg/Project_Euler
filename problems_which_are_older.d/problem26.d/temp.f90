program exp_17
 implicit none
 integer :: n,i,j,k,l,m,o
 integer, dimension(1000) :: monkey
 integer, dimension(1000) :: robot

 n = 1
 j = 1
 m = 0
 o = 0
n_loop : do n = 1, 10
 i_loop : do i = 1, 1000
  k = j / n
  robot(i) = k
  j = (j - k*n)*10
  if (j == 0) exit n_loop !! j should only equal zero if the series terminates
  do l = 1, i
   if (monkey(l) == j) then
    monkey(i) = j
    exit i_loop
   end if
  end do
  monkey(i) = j
 end do i_loop
 if 
end do n_loop

 other_i_loop : do i = 1, 1000
  write(*,*) monkey(i), robot(i)
  if(monkey(i) == 0) exit other_i_loop
 end do other_i_loop

end program exp_17
