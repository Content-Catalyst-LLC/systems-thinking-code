program recurrence_repair_capacity_model
  implicit none
  integer :: period
  real :: accountability, repair, harm

  accountability = 42.0
  repair = 28.0
  harm = 60.0

  print *, "period,accountability_index,repair_stock,cumulative_harm"
  do period = 0, 36
     print '(I0,A,F6.3,A,F6.3,A,F6.3)', period, ",", accountability, ",", repair, ",", harm
     accountability = max(0.0, min(100.0, accountability + 2.1))
     repair = max(0.0, min(100.0, repair + 1.8))
     harm = max(0.0, min(100.0, harm - 0.08 * repair + 0.02 * (100.0 - accountability)))
  end do
end program recurrence_repair_capacity_model
