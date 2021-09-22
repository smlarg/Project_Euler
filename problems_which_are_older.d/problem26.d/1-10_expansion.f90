program exp_1_10
 implicit none
 integer :: n,i,j,k,l,m,o,p
 integer, dimension(1000) :: monkey
 integer, dimension(1000) :: robot

 j = 1
 m = 0
 o = 0
 p = 0

 n_loop : do n = 1, 10
  j = 1
  monkey=0
  robot=0
  i_loop : do i = 1, 1000
   k = j / n
   robot(i) = k
   j = (j - k*n)*10
!   if (j == 0) exit i_loop
   !j=0 is I think the condition for finite fraction
   !m should equal zero still, so o and p shouldn't increment
   do l = 1, i
    if (monkey(l) == j) then
     monkey(i) = j ! catch the last digit
     !this is the number of repeating digits, ignoring leading non-repeating ones:
     m = i - l
     exit i_loop
    end if
   end do
   monkey(i) = j
  end do i_loop

  write(*,*) m, n
  if (m .gt. o) then
   o = m
   p = n
  end if

 end do n_loop

 write(*,*) o, p


end program exp_1_10
