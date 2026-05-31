program recurrence_boundary_model
  implicit none

  integer :: t
  real :: external_cost, internal_cost, value, score

  value = 220000.0
  internal_cost = 90000.0
  external_cost = 280000.0

  print *, "period", "score"

  do t = 1, 10
     external_cost = external_cost * 1.03
     internal_cost = internal_cost * 1.01
     score = value - internal_cost - external_cost
     print *, t, score
  end do

end program recurrence_boundary_model
