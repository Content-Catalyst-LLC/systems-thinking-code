program recurrence_systems_readiness_model
  implicit none
  integer :: period
  real :: readiness, harm, learning

  readiness = 34.0
  harm = 62.0
  learning = 36.0

  print *, "period,readiness,harm,learning"
  do period = 0, 36
     print '(I0,A,F6.3,A,F6.3,A,F6.3)', period, ",", readiness, ",", harm, ",", learning
     learning = max(0.0, min(100.0, learning + 2.0 - harm * 0.01))
     readiness = max(0.0, min(100.0, readiness + learning * 0.05 - harm * 0.03))
     harm = max(0.0, min(100.0, harm - readiness * 0.04 + 0.8))
  end do
end program recurrence_systems_readiness_model
