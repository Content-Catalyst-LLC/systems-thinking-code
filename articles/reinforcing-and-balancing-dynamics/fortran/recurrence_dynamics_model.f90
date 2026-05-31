program recurrence_dynamics_model
  implicit none
  integer :: t
  real :: x, r
  x = 10.0
  r = 0.12
  do t = 1, 20
     x = x + r * x
     print *, t, x
  end do
end program recurrence_dynamics_model
