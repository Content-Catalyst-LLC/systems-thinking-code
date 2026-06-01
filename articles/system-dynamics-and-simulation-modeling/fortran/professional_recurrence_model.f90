! Professional recurrence model for System Dynamics and Simulation Modeling
program professional_recurrence_model
  implicit none
  integer :: year
  real :: stock, capacity, burden, pressure, risk
  stock = 82; capacity = 51; burden = 34
  print *, 'year,stock,capacity,burden,risk'
  do year = 0, 30
     pressure = 4.3 + 2.0 * real(year) * 0.45
     burden = max(0.0, min(100.0, burden + pressure * 0.08 - 1.2 * 0.35))
     capacity = max(0.0, min(100.0, capacity + 1.2 - burden * 0.015))
     stock = max(0.0, min(120.0, stock + stock * 0.027 - pressure - burden * 0.035 + capacity * 0.025))
     risk = max(0.0, min(100.0, 100.0 - (0.45 * stock + 0.35 * capacity - 0.20 * burden)))
     write(*,'(I0,A,F6.2,A,F6.2,A,F6.2,A,F6.2)') year, ',', stock, ',', capacity, ',', burden, ',', risk
  end do
end program professional_recurrence_model
