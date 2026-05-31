program recurrence_behavior_model
  implicit none
  integer :: t
  real :: x
  x = 10.0
  print *, 'time,value'
  do t = 1, 12
     x = 1.10 * x
     print *, t, x
  end do
end program recurrence_behavior_model
