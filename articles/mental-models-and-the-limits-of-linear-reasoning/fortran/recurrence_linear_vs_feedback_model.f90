program recurrence_linear_vs_feedback_model
  implicit none
  integer :: t
  real :: state, delayed
  state = 50.0
  delayed = 0.0
  do t = 1, 12
     state = state + 5.0 - 0.45 * delayed
     delayed = 5.0
     print *, 'period=', t, 'state=', state
  end do
end program recurrence_linear_vs_feedback_model
