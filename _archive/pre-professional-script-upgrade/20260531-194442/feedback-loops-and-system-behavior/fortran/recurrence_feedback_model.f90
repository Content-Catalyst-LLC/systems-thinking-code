program recurrence_feedback_model
  implicit none
  integer :: period
  real :: x, rate

  x = 10.0
  rate = 0.10

  print *, 'period,value'
  do period = 1, 20
     x = x * (1.0 + rate)
     print '(I0,A,F8.3)', period, ',', x
  end do
end program recurrence_feedback_model
