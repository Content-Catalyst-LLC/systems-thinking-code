program recurrence_public_health_model
  implicit none
  integer :: week
  real :: susceptible, infected, recovered, population, beta, gamma, prevention
  real :: effective_beta, new_infections, recoveries

  susceptible = 99820.0
  infected = 180.0
  recovered = 0.0
  population = 100000.0
  beta = 0.39
  gamma = 0.20
  prevention = 0.42

  do week = 0, 52
    effective_beta = beta * (1.0 - prevention)
    new_infections = effective_beta * susceptible * infected / population
    if (new_infections > susceptible) new_infections = susceptible
    recoveries = gamma * infected
    if (recoveries > infected) recoveries = infected
    susceptible = susceptible - new_infections
    infected = infected + new_infections - recoveries
    recovered = recovered + recoveries
  end do

  print *, "Final infected:", infected, "recovered:", recovered
end program recurrence_public_health_model
