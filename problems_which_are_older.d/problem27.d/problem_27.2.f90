program prime_list
 implicit none
 integer :: i,j,n,a,b,aa,bb,ii,sum
 logical, allocatable, dimension(:) :: list


 n = 2000
 allocate(list(n))
 list=.true.
 list(1) = .false.

 do i=2, n
  j = 2
  da_loop : do
   if(j*j .gt. i) exit da_loop
   if(mod(i,j) .eq. 0) then
    list(i) = .false.
    exit da_loop
   end if
   j = j+1
  end do da_loop
 end do
 
! do i=1,n
!  if(list(i)) write(*,*) i
! end do

 ii = 0

 do a = -1000,1000
  do b = 2,1000
   if (.not. list(b) ) cycle
   this_loop : do i = 0,80
    sum = i*i + a*i + b
    if((sum .lt. 0) .or. (.not. list( sum ) )) exit this_loop
   end do this_loop
   if(i .gt. ii) then
    ii = i
    aa = a
    bb = b
   end if
  end do
 end do

 write(*,*) ii, aa, bb

end program prime_list
