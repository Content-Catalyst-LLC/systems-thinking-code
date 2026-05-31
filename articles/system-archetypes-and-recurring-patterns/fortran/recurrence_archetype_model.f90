program recurrence_archetype_model
  implicit none
  integer :: t
  real :: x, r, k

  x = 8.0
  r = 0.32
  k = 100.0

  print *, "time,state"
  do t = 0, 30
     print '(I0,A,F8.4)', t, ",", x
     x = x + r * x * (1.0 - x / k)
  end do
end program recurrence_archetype_model
