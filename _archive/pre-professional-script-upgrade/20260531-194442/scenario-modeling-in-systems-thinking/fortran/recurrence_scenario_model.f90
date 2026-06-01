program recurrence_scenario_model
  implicit none
  integer :: year
  real :: capacity, demand, capacity_growth, demand_growth

  capacity = 100.0
  demand = 95.0
  capacity_growth = 0.03
  demand_growth = 0.025

  do year = 0, 10
     print *, year, capacity, demand, demand - capacity
     capacity = capacity * (1.0 + capacity_growth)
     demand = demand * (1.0 + demand_growth)
  end do
end program recurrence_scenario_model
