program recurrence_policy_timing_model
  implicit none
  integer :: t
  real :: state, delayed, goal, correction
  state = 0.35
  delayed = 0.35
  goal = 1.0
  correction = 0.45
  do t = 1, 24
     state = state + correction * (goal - delayed)
     delayed = 0.9 * delayed + 0.1 * state
     print *, t, state
  end do
end program recurrence_policy_timing_model
