program prime_factors

 integer :: n = 2 ! total number of prime factors so far (1 and 2 count for 1 each)
 integer :: m = 0 ! number of prime factors for this integer
 integer, dimension(5761454) :: primes ! array of primes found so far
 real, dimension(5761454) :: primes_as_reals !this didn't help very much
 integer :: p = 1 ! total number of primes found so far
 integer :: i,j,k !iteration counters
 real :: root_i !square root of current number, upper bound for smallest factor
 integer, parameter :: X = 10**8 ! number to count up to
 
 !----------------------------
 
 primes(1) = 2
 primes_as_reals(1) = 2.0**.5
 
 loopname: do i = 3, X
  if (mod(i,10**6) .eq. 0) print *, i
  k = i
  root_i = (real(i)+1.0)**.5 !to avoid any roundoff errors
  m = 0
  otherloopname: do j = 1, p
   if ((primes_as_reals(j) .gt. root_i) .and. (m .eq. 0)) exit otherloopname
   if ( mod(k,primes(j)) .eq. 0) then
    m = m + 1
    do while (mod(k,primes(j)) .eq. 0)
     k = k/primes(j)
     if (k .eq. 1) exit otherloopname
    enddo
   endif
  enddo otherloopname
  n = n + m
  if (m .eq. 0) then
   n = n + 1
   p =  p + 1
   primes(p) = i
   primes_as_reals(p) = real(i)
  endif
 enddo loopname

 
 print *, p
 print *, n
 
end program prime_factors
    