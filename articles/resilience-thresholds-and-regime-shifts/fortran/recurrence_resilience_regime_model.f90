program recurrence_resilience_regime_model
  implicit none
  integer :: year
  real :: resilience, pressure, margin
  character(len=20) :: regime

  resilience = 78.0
  pressure = 35.0

  do year = 0, 20
     pressure = pressure + 2.3
     resilience = max(0.0, min(100.0, resilience + 1.3 - 2.1 - pressure * 0.02))
     margin = resilience - pressure
     if (margin <= 0.0) then
        regime = "shifted"
     else if (margin <= 10.0) then
        regime = "near_threshold"
     else
        regime = "recoverable"
     end if
     write(*,'(I3,A,F6.2,A,F6.2,A,F6.2,A,A)') year, ",", resilience, ",", pressure, ",", margin, ",", trim(regime)
  end do
end program recurrence_resilience_regime_model
