-- Quality checks for public health systems tables.

-- Population stocks should never be negative.
SELECT *
FROM public_health_timeseries
WHERE susceptible < 0 OR infected < 0 OR recovered < 0;

-- Trust index should remain within 0 to 100.
SELECT *
FROM public_health_timeseries
WHERE public_trust < 0 OR public_trust > 100;

-- Care capacity should remain positive.
SELECT *
FROM public_health_timeseries
WHERE care_capacity <= 0;
