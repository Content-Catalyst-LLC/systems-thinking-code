program recurrence_feedback_control_model
  implicit none
  integer :: period
  real :: state, goal, error_signal, control_action, direction

  state = 46.0
  goal = 70.0

  print *, "period,system_state,error_signal,control_action"
  do period = 0, 36
     error_signal = goal - state
     control_action = max(0.0, min(100.0, abs(error_signal) * 0.42))
     if (error_signal >= 0.0) then
        direction = 1.0
     else
        direction = -1.0
     end if
     print '(I0,A,F6.3,A,F6.3,A,F6.3)', period, ",", state, ",", error_signal, ",", control_action
     state = max(0.0, min(100.0, state + direction * control_action * 0.18 - 1.2))
  end do
end program recurrence_feedback_control_model
