program recurrence_leverage_model
  implicit none
  integer :: t
  real :: x, goal, k
  x = 80.0
  goal = 50.0
  k = 0.2
  do t = 1, 12
     x = x + k * (goal - x)
     print *, t, x
  end do
end program recurrence_leverage_model
