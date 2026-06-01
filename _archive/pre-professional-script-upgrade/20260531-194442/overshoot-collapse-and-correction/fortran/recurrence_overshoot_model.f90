program recurrence_overshoot_model
  implicit none
  integer :: month
  real :: pressure, stock, limit, overshoot
  pressure = 0.40
  stock = 0.78
  limit = 0.60
  do month = 0, 24
     overshoot = max(0.0, pressure - limit)
     stock = max(0.0, min(1.0, stock - overshoot * 0.08 + 0.015))
     pressure = max(0.0, min(1.2, pressure + 0.07 * pressure - overshoot * 0.25))
     if (mod(month, 6) == 0) print *, month, pressure, stock, overshoot
  end do
end program recurrence_overshoot_model
