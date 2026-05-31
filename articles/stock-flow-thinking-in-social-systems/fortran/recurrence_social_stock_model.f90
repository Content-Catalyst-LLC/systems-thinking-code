program recurrence_social_stock_model
  implicit none
  integer :: month
  real :: trust
  trust = 42.0
  do month = 0, 24
     print *, month, trust
     trust = min(100.0, max(0.0, trust + 3.2 - 2.6))
  end do
end program recurrence_social_stock_model
