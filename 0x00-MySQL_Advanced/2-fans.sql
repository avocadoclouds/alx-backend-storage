-- Write a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
-- Requirements:
--     Import table dump: metal_bands.sql
--     Column names must be: origin and nb_fans
--     Your script can be executed on any database
-- Context: Calculate/compute something is always power intensive…
-- better to distribute the load!


SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;