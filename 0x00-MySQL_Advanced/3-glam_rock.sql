-- Write a SQL script that lists all bands with Glam rock as their main style,
-- ranked by their longevity
-- Requirements:
--     Import this table dump: metal_bands.sql.zip
--     Column names must be: band_name and lifespan (in years)
--     You should use attributes formed and split for computing the lifespan
--     Your script can be executed on any database


-- Lists all bands with Glam rock as their style,
-- ranked by their longevity
-- Column names must be: band_name & lifespan

SELECT band_name, ifnull(split, 2020)-ifnull(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC