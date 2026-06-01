program recurrence_dynamic_systems
  implicit none
  integer :: period
  real :: stock, inflow, outflow_rate, outflow

  stock = 100.0
  inflow = 12.0
  outflow_rate = 0.08

  print *, 'period,stock,inflow,outflow'
  do period = 1, 24
     outflow = stock * outflow_rate
     stock = stock + inflow - outflow
     print *, period, stock, inflow, outflow
  end do
end program recurrence_dynamic_systems
