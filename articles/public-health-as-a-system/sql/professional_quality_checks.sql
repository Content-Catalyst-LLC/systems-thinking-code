-- Quality checks for public health systems tables.

SELECT * FROM public_health_timeseries
WHERE susceptible < 0 OR infected < 0 OR recovered < 0;

SELECT * FROM public_health_timeseries
WHERE public_trust < 0 OR public_trust > 100;

SELECT * FROM public_health_timeseries
WHERE care_capacity <= 0;
