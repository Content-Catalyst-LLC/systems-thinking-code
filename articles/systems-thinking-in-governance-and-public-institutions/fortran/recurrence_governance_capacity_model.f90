program recurrence_governance_capacity_model
  implicit none
  integer :: t
  real :: capacity, trust, feedback
  capacity = 0.52
  trust = 0.48
  feedback = 0.31
  do t = 1, 6
     capacity = min(1.0, max(0.0, capacity + 0.05 * feedback + 0.03 * trust - 0.02))
     trust = min(1.0, max(0.0, trust + 0.04 * capacity - 0.015))
     feedback = min(1.0, max(0.0, feedback + 0.06))
     print *, 'period=', t, ' capacity=', capacity, ' trust=', trust, ' feedback=', feedback
  end do
end program recurrence_governance_capacity_model
