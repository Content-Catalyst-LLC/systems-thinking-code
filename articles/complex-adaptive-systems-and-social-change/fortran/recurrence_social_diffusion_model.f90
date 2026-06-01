program recurrence_social_diffusion_model
  implicit none
  integer :: period
  real :: adoption, diffusion, learning, resistance

  adoption = 18.0

  print *, "period,adoption"
  do period = 0, 24
     print '(I0,A,F6.3)', period, ",", adoption
     diffusion = 0.70 * adoption * (100.0 - adoption) / 100.0 * 0.08
     learning = 0.82 * 1.5
     resistance = 0.34 * adoption * 0.025
     adoption = max(0.0, min(100.0, adoption + diffusion + learning - resistance))
  end do
end program recurrence_social_diffusion_model
