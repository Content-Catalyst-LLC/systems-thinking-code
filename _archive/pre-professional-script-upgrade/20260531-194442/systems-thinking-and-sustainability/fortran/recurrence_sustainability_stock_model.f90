program sustainability_stock
  implicit none
  integer :: year
  real :: stock
  stock = 100.0
  do year = 2026, 2035
     stock = max(0.0, stock + 3.5 - 2.8 - 0.4)
     print *, year, stock
  end do
end program sustainability_stock
