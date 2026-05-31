program recurrence_goal_dynamics
  implicit none
  integer :: t
  real :: state, goal, correction, error

  state = 0.25
  goal = 0.80
  correction = 0.30

  do t = 1, 12
     error = goal - state
     state = state + correction * error
     if (state < 0.0) state = 0.0
     if (state > 1.0) state = 1.0
     print *, t, state
  end do
end program recurrence_goal_dynamics
