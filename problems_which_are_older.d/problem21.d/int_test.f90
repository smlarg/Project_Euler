program int_test
 implicit none
 integer :: i,j,k
 

 i = 6
 j = 3
 IF( (i/j)*j -i .eq. 0) THEN
  write(*,*) 'shoup'
 END IF
! write(*,*) k

end program int_test
