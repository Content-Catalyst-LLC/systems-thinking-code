program recurrence_burden_shift_model
  implicit none
  integer :: t
  real :: pressure, capacity, dependency, relief, repair

  pressure = 80.0
  capacity = 55.0
  dependency = 0.30

  print *, "period,pressure,capacity,dependency"
  do t = 0, 9
     relief = 35.0 - 2.0 * t
     if (relief < 8.0) relief = 8.0
     repair = 8.0 + 4.0 * t
     capacity = max(0.0, capacity + 0.65 * repair - 0.22 * relief)
     dependency = max(0.0, dependency + 0.012 * relief - 0.014 * repair)
     pressure = max(0.0, pressure + 4.0 - 0.35 * relief - 0.20 * capacity)
     print *, t, pressure, capacity, dependency
  end do
end program recurrence_burden_shift_model
