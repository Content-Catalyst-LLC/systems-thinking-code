program recurrence_loop_dynamics
  implicit none
  integer :: t
  real :: x
  x = 10.0
  print *, 'Reinforcing recurrence example'
  do t = 1, 12
     x = x + 0.08 * x
     print *, t, x
  end do
end program recurrence_loop_dynamics
