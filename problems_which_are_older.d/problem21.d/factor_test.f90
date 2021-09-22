program factor_test
 implicit none
 integer :: n, i
 real :: n_real

 n = 100
 i = 1
 n_real = n

 i_loop : do
  if ( i > sqrt(n_real)) exit
  if ((n -(n/i)*i) .eq. 0 ) then
   write (*,*) i
  end if
  i = i + 1
 end do i_loop

end program factor_test



