program policy_feedback
  implicit none
  integer :: year
  real :: outcome
  outcome = 42.0
  do year = 0, 10
     outcome = min(100.0, max(0.0, outcome + 0.2 * 35.0 - 0.25 * 24.0 + 0.1 * 55.0))
     print *, year, outcome
  end do
end program policy_feedback
