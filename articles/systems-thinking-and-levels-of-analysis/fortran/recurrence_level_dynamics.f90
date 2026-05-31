program recurrence_level_dynamics
  implicit none
  integer :: t
  real :: micro_burden, meso_capacity, macro_stress

  micro_burden = 60.0
  meso_capacity = 65.0
  macro_stress = 70.0

  print *, 'period,micro_burden,meso_capacity,macro_stress'
  do t = 1, 12
     micro_burden = micro_burden + 0.05 * macro_stress - 0.03 * meso_capacity
     meso_capacity = meso_capacity + 0.02 * (100.0 - micro_burden) - 0.01 * macro_stress
     macro_stress = macro_stress + 0.5 - 0.01 * meso_capacity
     print *, t, micro_burden, meso_capacity, macro_stress
  end do
end program recurrence_level_dynamics
