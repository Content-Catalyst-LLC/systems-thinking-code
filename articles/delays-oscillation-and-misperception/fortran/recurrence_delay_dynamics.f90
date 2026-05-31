program recurrence_delay_dynamics
  implicit none
  integer :: t
  real :: x
  x = 80.0
  do t = 1, 10
     x = x + 0.2 * (50.0 - x)
     print *, t, x
  end do
end program recurrence_delay_dynamics
