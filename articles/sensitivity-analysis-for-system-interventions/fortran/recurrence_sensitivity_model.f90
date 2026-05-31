program recurrence_sensitivity_model
  implicit none
  integer :: t
  real :: stock, repair, harm
  stock = 0.50
  repair = 0.08
  harm = 0.05
  do t = 1, 24
     stock = max(0.0, min(1.0, stock + repair - harm))
     print *, t, stock
  end do
end program recurrence_sensitivity_model
