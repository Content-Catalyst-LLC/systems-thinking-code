program recurrence_signed_feedback
  implicit none
  integer :: t
  real :: x
  real, parameter :: influence = 0.10
  x = 1.0
  do t = 1, 10
     x = x + influence * x
     print *, t, x
  end do
end program recurrence_signed_feedback
