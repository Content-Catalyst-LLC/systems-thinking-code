program recurrence_interdependence_model
  implicit none
  integer :: t
  real :: capacity, stress, resilience

  capacity = 70.0
  stress = 30.0
  resilience = 45.0

  print *, 'period,capacity,stress,resilience'
  do t = 1, 20
     stress = stress + 3.0 + 0.04 * capacity - 0.08 * resilience
     capacity = capacity - 0.05 * stress + 0.03 * resilience
     resilience = resilience + 1.5 - 0.04 * stress
     print '(I0,A,F6.2,A,F6.2,A,F6.2)', t, ',', capacity, ',', stress, ',', resilience
  end do
end program recurrence_interdependence_model
