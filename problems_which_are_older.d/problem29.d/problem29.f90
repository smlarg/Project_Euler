program problem29
 implicit none
! integer, dimension(99,99,2) :: pairs
 logical, dimension(99,99) :: unique
 integer, dimension(2) :: first_v, second_v
 integer :: first, second, a, b, x, y

! do a = 2, 100
!  do b = 2, 100
!   pairs(a,b,1) = a
!   pairs(a,b,2) = b
!  end do
! end do

 do first = 0, 99*99
  first_v = vectorize(first)
  do second = first+1, 99*99
   second_v = vectorize(second)
   if( exponent_test_equality( first_v, second_v ) ) then
    
   
        

  end do
 end do


contains

function power_ex(a,b) !delete this
 integer, intent(in) :: a,b,i,j
 integer, allocatable, dimension(:) :: power_ex

 allocate(power_ex(b))
 
 i = 1
 j = 1
 do_loop : do
  if(is_prime(i)) then
   power_ex(j)
   j = j + 1
   if (j .gt. b) exit do_loop
  end if
  i = i + 1
 end do do_loop

end function power_ex



