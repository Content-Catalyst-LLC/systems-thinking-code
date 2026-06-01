program recurrence_adaptive_system_model
  implicit none
  integer, parameter :: agents = 40
  integer :: i, t, left_idx, right_idx
  real(8) :: states(agents), next_states(agents), local, total

  do i = 1, agents
    states(i) = dble(mod(i * 17, 100)) / 100.0d0
  end do

  do t = 1, 20
    do i = 1, agents
      left_idx = i - 1
      if (left_idx < 1) left_idx = agents
      right_idx = i + 1
      if (right_idx > agents) right_idx = 1
      local = (states(left_idx) + states(right_idx)) / 2.0d0
      next_states(i) = max(0.0d0, min(1.0d0, states(i) + 0.18d0 * (local - states(i))))
    end do
    states = next_states
  end do

  total = sum(states)
  print *, 'Fortran adaptive recurrence final mean:', total / agents
end program recurrence_adaptive_system_model
