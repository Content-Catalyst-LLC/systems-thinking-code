program recurrence_fixes_that_fail_model
  implicit none
  integer :: t
  real :: problem, fix, delayed_harm
  real, dimension(3) :: delay
  problem = 100.0
  delay = 0.0
  do t = 1, 12
     fix = min(1.0, problem / 140.0)
     delayed_harm = delay(1) * 20.0
     delay(1) = delay(2)
     delay(2) = delay(3)
     delay(3) = fix
     problem = max(0.0, problem + 7.0 - 25.0 * fix + delayed_harm)
     print *, t, problem, fix, delayed_harm
  end do
end program recurrence_fixes_that_fail_model
