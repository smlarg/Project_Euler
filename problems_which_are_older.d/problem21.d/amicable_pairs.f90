program amicable_pairs
 implicit none
 integer :: n,a,b,total

 total = 0
 do n = 1, 10000
  a = divisor_sum(n)
  b = divisor_sum(a)
  if ( (b .eq. n) .and. (a .ne. n) ) then
   total = total + n
   write(*,*) n,a
  end if
 end do
 write(*,*) total

contains

integer function divisor_sum(n)

 implicit none
 integer, intent(in) :: n
 integer :: i,j,k
 integer, dimension(100) :: divisor_list

 j = 1
 divisor_list = 0
 i_loop : DO i = 1,n-1
  IF ((n - (n/i)*i) .eq. 0 ) THEN
   divisor_list(j) = i
   j = j + 1
  END IF
 END DO i_loop
 divisor_sum = 0
 DO k = 1, 100
  divisor_sum = divisor_sum + divisor_list(k)
 END DO

end function divisor_sum

END PROGRAM amicable_pairs

