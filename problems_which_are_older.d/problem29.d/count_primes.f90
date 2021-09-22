program prime_list
 implicit none
 integer :: i,j,n,a,b,aa,bb,ii,sum
 logical, allocatable, dimension(:) :: list


 n = 100
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
 
 j = 0
 do i=1,n
  if(list(i)) then
   write(*,*) i 
   j = j + 1
  end if
 end do

 write(*,*)"there are ", j, "primes below ", n

end program prime_list
