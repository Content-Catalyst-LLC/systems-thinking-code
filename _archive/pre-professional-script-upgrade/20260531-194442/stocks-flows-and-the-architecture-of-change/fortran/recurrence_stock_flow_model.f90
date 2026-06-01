program recurrence_stock_flow_model
  implicit none
  integer :: t
  real :: stock, inflow, outflow
  stock = 55.0
  inflow = 4.0
  outflow = 5.0
  do t = 1, 10
     print *, t, stock
     stock = stock + inflow - outflow
  end do
end program recurrence_stock_flow_model
