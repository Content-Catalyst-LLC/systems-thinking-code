program recurrence_nexus_stock_model
  implicit none
  integer :: year
  real :: groundwater, recharge, withdrawal
  groundwater = 1000.0
  recharge = 28.0
  withdrawal = 55.0 * 1.18
  print *, 'year,groundwater'
  do year = 0, 30
    groundwater = groundwater + recharge - withdrawal
    if (groundwater < 0.0) groundwater = 0.0
    print *, year, groundwater
  end do
end program recurrence_nexus_stock_model
