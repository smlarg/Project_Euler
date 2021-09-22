program whole_divisors_count
 implicit none
 integer :: n,i,count_temp,count_total,n_highest
 n = 1
 i = 1
 count_temp = 0
 count_total = 0
 n_highest = 0
 n_loop : DO
  IF ( n > 10000) EXIT n_loop
  count_temp = 0
  i = 1
  i_loop : DO
   IF (i > n) EXIT i_loop
   IF ((n - (n/i)*i) .eq. 0 ) THEN
    count_temp = count_temp + 1
!    write(*,*) "huzzah"
!    write(*,*) i
!    write(*,*) count_temp
   END IF
   i = i+1
  END DO i_loop
  IF (count_temp > count_total) THEN
   count_total = count_temp
   n_highest = n
  END IF
  n = n + 1
 END DO n_loop
 write(*,*) count_total
 write(*,*) n_highest
END PROGRAM whole_divisors_count
