program recurrence_asset_deterioration_model
  implicit none
  integer :: year
  real :: condition, climate_stress, maintenance_strength, deterioration, maintenance

  condition = 64.0
  climate_stress = 0.55
  maintenance_strength = 0.70

  print *, "year,condition"
  do year = 0, 20
     print '(I0,A,F6.3)', year, ",", condition
     deterioration = 1.8 + climate_stress * (100.0 - condition) * 0.025
     maintenance = maintenance_strength * 2.2
     condition = max(0.0, min(100.0, condition - deterioration + maintenance))
  end do
end program recurrence_asset_deterioration_model
