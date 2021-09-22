program abundant_numbers_count
 implicit none
 integer :: n,i,j,total
 logical, allocatable, dimension(:) :: a_list, can_sum_list
 
 total = 0
 n = 30000
 allocate(a_list(n))
 allocate(can_sum_list(n))
 a_list = abundant_list(n)
 can_sum_list = .false.

 i_loop : do i = 1,n
  j_loop : do j = 1,i-1
   if(a_list(j) .and. a_list(i-j)) then
    can_sum_list(i) = .true.
    exit j_loop
   end if
  end do j_loop
 end do i_loop

 do i = 1,n
  if(.not. can_sum_list(i)) total = total + i
 end do

 write(*,*) 

 write(*,*) total

contains

function abundant_list(n)
 implicit none
 logical, allocatable, dimension(:) :: abundant_list
 integer, intent(in) :: n
 integer :: i,a

 allocate(abundant_list(n))
 abundant_list = .false.

 do i = 1, n
  a = divisor_sum(i)
  if ( a .gt. i ) then
   abundant_list(i) = .true.
  end if
 end do


end function abundant_list



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

END PROGRAM abundant_numbers_count

