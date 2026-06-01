program recurrence_cascade_model
  implicit none
  real :: load, threshold
  integer :: failures
  load = 0.70
  threshold = 0.50
  failures = 0
  if (load > threshold) failures = failures + 1
  print *, "recurrence cascade model failures=", failures
end program recurrence_cascade_model
