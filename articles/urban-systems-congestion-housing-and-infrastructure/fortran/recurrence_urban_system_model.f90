program recurrence_urban_system_model
  implicit none
  integer :: year
  real :: congestion, affordability, infrastructure, displacement, resilience
  congestion = 50.0
  affordability = 44.0
  infrastructure = 60.0
  displacement = 42.0
  do year = 0, 30
     congestion = clamp(congestion + 0.60 + displacement * 0.008 - affordability * 0.004)
     affordability = clamp(affordability + 0.35 - congestion * 0.010 - displacement * 0.006)
     infrastructure = clamp(infrastructure + 0.50 - 1.10 - congestion * 0.008)
     displacement = clamp(displacement + congestion * 0.006 - affordability * 0.004)
  end do
  resilience = clamp((100.0 - congestion) * 0.25 + affordability * 0.25 + infrastructure * 0.30 + (100.0 - displacement) * 0.20)
  print *, 'Urban Fortran recurrence resilience=', resilience
contains
  real function clamp(x)
    real, intent(in) :: x
    clamp = max(0.0, min(100.0, x))
  end function clamp
end program recurrence_urban_system_model
