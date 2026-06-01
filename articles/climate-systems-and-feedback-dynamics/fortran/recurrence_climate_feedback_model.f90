program recurrence_climate_feedback_model
  implicit none
  integer :: year
  real(8) :: co2, emissions, temp, heat, feedback, f, target

  co2 = 420.0d0
  emissions = 40.0d0
  temp = 1.2d0
  heat = 0.0d0
  feedback = 1.28d0

  do year = 0, 80
    emissions = emissions * 0.96d0
    co2 = co2 + (emissions / 7.8d0) * 0.55d0
    f = 5.35d0 * log(co2 / 280.0d0)
    heat = heat + f * 0.035d0
    target = 0.78d0 * f * feedback
    temp = temp + 0.10d0 * (target - temp) + heat * 0.006d0
  end do

  print *, 'Final synthetic CO2 ppm:', co2
  print *, 'Final synthetic temperature anomaly C:', temp
end program recurrence_climate_feedback_model
