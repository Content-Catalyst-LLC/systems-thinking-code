program stock_flow_model
  implicit none

  integer, parameter :: steps = 20
  real :: stock(steps)
  real :: inflow, outflow
  integer :: t

  stock(1) = 50.0
  inflow = 5.0
  outflow = 3.5

  do t = 2, steps
     stock(t) = max(0.0, stock(t - 1) + inflow - outflow)
  end do

  print *, "Stock-flow simulation"

  do t = 1, steps
     print *, t, stock(t)
  end do

end program stock_flow_model
