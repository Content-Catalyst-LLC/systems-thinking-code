program recurrence_learning_stock_model
  implicit none
  integer :: period
  real :: learning, defensiveness, learning_flow, forgetting

  learning = 34.0
  defensiveness = 42.0

  print *, "period,learning_stock,defensive_routines"
  do period = 0, 36
     print '(I0,A,F6.3,A,F6.3)', period, ",", learning, ",", defensiveness
     learning_flow = 0.70 * 4.5 + 0.68 * 3.8 - defensiveness * 0.035
     forgetting = defensiveness * 0.025
     learning = max(0.0, min(100.0, learning + learning_flow - forgetting))
     defensiveness = max(0.0, min(100.0, defensiveness + 1.0 - 0.68 * 2.4))
  end do
end program recurrence_learning_stock_model
