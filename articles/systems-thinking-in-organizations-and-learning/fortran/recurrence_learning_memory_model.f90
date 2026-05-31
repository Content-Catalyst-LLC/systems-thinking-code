program recurrence_learning_memory_model
  implicit none
  real :: memory, learning, forgetting
  memory = 0.52
  learning = 0.08
  forgetting = 0.05
  memory = memory + learning - forgetting
  print *, "memory_next=", memory
end program recurrence_learning_memory_model
