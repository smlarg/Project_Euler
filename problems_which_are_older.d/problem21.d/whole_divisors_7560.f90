program whole_divisors_7560
 implicit none
 integer :: n,i,j
 real :: n_real
 integer, dimension(33) :: divisor_list


 n = 7560
 i = 1
 j = 1
 divisor_list = 0
 n_loop : DO
  n_real =  n
  IF ( n > 7560) EXIT n_loop
  i = 1
  j = 1
  i_loop : DO
   IF (i > sqrt(n_real)) EXIT i_loop
   IF ((n - (n/i)*i) .eq. 0 ) THEN
    divisor_list(j) = i
    j = j + 1
   END IF
   i = i+1
  END DO i_loop
  IF ( n/divisor_list(j-1) > divisor_list(j-1) ) THEN
   divisor_list(j) = n/divisor_list(j-1)
  END IF
  n = n + 1
 END DO n_loop
 write(*,*) divisor_list
END PROGRAM whole_divisors_7560
