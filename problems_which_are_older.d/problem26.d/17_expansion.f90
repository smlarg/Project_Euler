program exp_17
 implicit none
 integer :: n,i,j,k,l,m
 integer, dimension(1000) :: monkey
 integer, dimension(1000) :: robot

 n = 8
 j = 1
 m = 0 

 i_loop : do i = 1, 1000
  k = j / n
  robot(i) = k
  j = (j - k*n)*10
  do l = 1, i
   if (monkey(l) == j) then
    monkey(i) = j
    m = i - l
    exit i_loop
   end if
  end do
  monkey(i) = j
 end do i_loop

 write(*,*) m

 other_i_loop : do i = 1, 1000
  write(*,*) monkey(i), robot(i)
  if(monkey(i) == 0) exit other_i_loop
 end do other_i_loop

end program exp_17
