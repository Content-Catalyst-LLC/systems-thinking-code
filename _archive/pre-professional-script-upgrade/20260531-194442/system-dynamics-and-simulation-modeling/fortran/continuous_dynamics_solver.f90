program continuous_dynamics_solver
  implicit none
  integer :: t
  real :: stock, inflow, outflow, dt

  stock = 100.0
  inflow = 12.0
  dt = 0.1

  print *, 'time,stock,inflow,outflow'
  do t = 0, 240
     outflow = 0.05 * stock
     if (mod(t, 10) == 0) then
        print *, real(t) * dt, stock, inflow, outflow
     end if
     stock = max(0.0, stock + dt * (inflow - outflow))
  end do
end program continuous_dynamics_solver
