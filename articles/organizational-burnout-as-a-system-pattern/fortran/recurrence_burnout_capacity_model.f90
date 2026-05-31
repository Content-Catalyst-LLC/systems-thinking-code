program recurrence_burnout_capacity_model
  implicit none
  integer :: t
  real :: capacity, workload, recovery, depletion
  capacity = 80.0
  do t = 1, 8
     workload = 55.0 + 4.0 * t
     recovery = 10.0 - 0.4 * t
     depletion = max(0.0, workload / 12.0 - recovery / 4.0)
     capacity = capacity + recovery * 0.5 - depletion * 1.5
     print *, 'period=', t, ' capacity=', capacity
  end do
end program recurrence_burnout_capacity_model
