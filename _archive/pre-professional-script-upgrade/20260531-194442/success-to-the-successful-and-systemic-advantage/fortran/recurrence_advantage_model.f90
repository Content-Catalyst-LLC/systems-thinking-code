program recurrence_advantage_model
  implicit none
  integer :: t
  real :: advantage
  advantage = 30.0
  do t = 1, 12
     advantage = advantage + 0.04 * advantage + 1.5
  end do
  print *, 'final_advantage=', advantage
end program recurrence_advantage_model
