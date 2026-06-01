program recurrence_overshoot_model
  implicit none
  integer :: period
  real :: resource, consumption, regeneration

  resource = 82.0

  print *, "period,resource_stock,consumption,regeneration"
  do period = 0, 36
     consumption = max(0.0, min(100.0, 0.62 * 9.0 + max(0.0, 70.0 - resource) * 0.04))
     regeneration = max(0.0, min(100.0, 0.50 * 6.0 + 2.5))
     print '(I0,A,F6.3,A,F6.3,A,F6.3)', period, ",", resource, ",", consumption, ",", regeneration
     resource = max(0.0, min(100.0, resource - consumption + regeneration))
  end do
end program recurrence_overshoot_model
