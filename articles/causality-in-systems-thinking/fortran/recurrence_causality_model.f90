program recurrence_causality_model
  implicit none
  integer :: period
  real :: trust, capacity, demand, delay

  trust = 64.0
  capacity = 58.0
  demand = 70.0

  print *, 'period,trust,capacity,demand,delay'
  do period = 1, 20
     delay = (demand / max(capacity, 1.0)) * 10.0
     trust = trust + capacity / 140.0 - delay / 18.0
     capacity = capacity + trust / 120.0 - demand / 180.0
     if (65.0 - trust > 0.0) then
        demand = demand + (65.0 - trust) * 0.05
     end if
     print '(I0,A,F6.2,A,F6.2,A,F6.2,A,F6.2)', period, ',', trust, ',', capacity, ',', demand, ',', delay
  end do
end program recurrence_causality_model
