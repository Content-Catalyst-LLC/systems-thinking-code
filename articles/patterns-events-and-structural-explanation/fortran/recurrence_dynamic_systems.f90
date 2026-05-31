program recurrence_dynamic_systems
  implicit none
  integer :: period
  real :: trust, risk

  trust = 62.0
  risk = 52.0

  print *, 'period,trust,risk'
  do period = 1, 20
     risk = risk + (0.04 * risk * (1.0 + max(0.0, 60.0 - trust) / 60.0)) - 1.0
     trust = trust - (0.03 * risk) + 0.4
     print '(I0,A,F6.2,A,F6.2)', period, ',', trust, ',', risk
  end do
end program recurrence_dynamic_systems
