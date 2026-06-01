program recurrence_stock_flow_model
  implicit none
  integer :: period
  real :: backlog, capacity, service

  backlog = 58.0
  capacity = 46.0

  print *, "period,backlog"
  do period = 0, 24
     print '(I0,A,F6.3)', period, ",", backlog
     service = capacity * 0.42
     backlog = max(0.0, min(200.0, backlog + 3.2 - service))
  end do
end program recurrence_stock_flow_model
