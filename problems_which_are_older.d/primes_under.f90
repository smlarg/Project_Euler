program primes_under_10_carrot_8

 integer(8) :: k = 0
 integer(8) :: j = 0
 integer(8) :: large = 10
 !....
 large = large**8
 do j = 2, large
  if (is_prime(j)) then
   k = k+1
  endif
 enddo
 
 print * , k


 contains
 
 logical function is_prime(i)
  integer(8), intent(in) :: i
  
  integer(8) :: l,m
  !....
  m = int(i**.5,8) + 1
  do l = 2, m
   if (mod(i,l) .eq. 0)  then
    is_prime = .false.
    return
   endif
  end do
  is_prime = .true.
  return
 end function is_prime

end program primes_under_10_carrot_8
