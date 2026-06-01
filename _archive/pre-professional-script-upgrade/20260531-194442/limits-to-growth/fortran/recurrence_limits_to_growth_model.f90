program recurrence_limits_to_growth_model
  implicit none
  integer :: year
  real :: scale, rate, capacity
  scale = 100.0
  rate = 0.13
  capacity = 260.0
  do year = 0, 25
     print *, year, scale, scale / capacity
     scale = scale + rate * scale * (1.0 - scale / capacity)
  end do
end program recurrence_limits_to_growth_model
