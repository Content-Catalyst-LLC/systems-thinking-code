program recurrence_policy_resistance_model
  implicit none
  integer :: t
  real :: y, policy, compensation, offset
  y = 50.0
  policy = 0.7
  compensation = 0.4
  do t = 1, 12
    offset = compensation * max(0.0, y - 50.0) / 50.0
    y = y + 3.0 * policy - 2.0 * offset
    print *, t, y
  end do
end program recurrence_policy_resistance_model
