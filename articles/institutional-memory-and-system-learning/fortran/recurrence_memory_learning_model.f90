program recurrence_memory_learning_model
  implicit none
  integer :: t
  real :: memory, learning, documentation, turnover_loss, forgetting
  memory = 0.52
  do t = 1, 8
     learning = 0.055 + 0.01 * t
     documentation = 0.045 + 0.005 * t
     turnover_loss = 0.025
     if (t == 2 .or. t == 5 .or. t == 7) turnover_loss = 0.05
     forgetting = 0.028
     memory = max(0.0, min(1.0, memory + learning + documentation + 0.035 - turnover_loss - forgetting - 0.018))
     print *, 'period=', t, ' memory=', memory
  end do
end program recurrence_memory_learning_model
