program recurrence_ai_feedback_model
  implicit none
  integer :: t
  real :: risk, governance
  risk = 32.0
  governance = 48.0
  print *, 'period,risk,governance'
  do t = 0, 12
    print '(I0,A,F6.3,A,F6.3)', t, ',', risk, ',', governance
    risk = max(0.0, min(100.0, risk + 2.0 - governance * 0.03))
    governance = max(0.0, min(100.0, governance + 1.25))
  end do
end program recurrence_ai_feedback_model
