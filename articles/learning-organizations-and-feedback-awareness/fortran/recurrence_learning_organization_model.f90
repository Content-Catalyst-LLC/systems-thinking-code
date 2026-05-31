program recurrence_learning_organization_model
  implicit none
  integer :: t
  real :: learning
  learning = 0.25
  do t = 1, 8
     learning = learning + 0.10 * (1.0 - learning)
     print *, t, learning
  end do
end program recurrence_learning_organization_model
