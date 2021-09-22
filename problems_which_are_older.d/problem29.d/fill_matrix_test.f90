program matrix_fill_test
 implicit none
 integer :: a
 integer, dimension (4,4) :: numer, denom

 do a = 0,4*4-1
  numer(mod(a,4)+1,a/4 + 1) = mod(a,4)+2
  denom(mod(a,4)+1,a/4 + 1) = a/4 +2
 end do

 write(*,*) numer
 write(*,*) denom

end program matrix_fill_test
