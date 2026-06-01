program recurrence_commons_model
  implicit none
  integer :: year
  real :: stock, capacity, regen_rate, annual_use, regeneration
  stock = 1000.0
  capacity = 1400.0
  regen_rate = 0.22
  annual_use = 120.0
  do year = 1, 25
    regeneration = regen_rate * stock * max(0.0, 1.0 - stock / capacity)
    stock = max(0.0, stock + regeneration - annual_use)
  end do
  print *, 'Final synthetic commons stock:', stock
end program recurrence_commons_model
