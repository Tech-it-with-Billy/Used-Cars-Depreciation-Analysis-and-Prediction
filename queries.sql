-- 1. What is the resale value of a specific car brands and models in Kenya?
SELECT make, model, year, AVG(price)
FROM listings
GROUP BY 1, 2, 3
HAVING make like 'Mercedes-Benz' and model like 'E250'
ORDER BY 3;



-- 2. What are the most in-demand cars in specific regions?
SELECT make, model, city, state, COUNT(model)
FROM listings 
GROUP BY 1, 2, 3, 4
ORDER BY 5 DESC;



-- 3. Is there a preferred price range that buyers are targeting?
SELECT CASE WHEN price < 1000000 THEN 'under 1million'
            WHEN price >= 1000000 AND price < 2000000 THEN 'between 1 and 2 million'
            WHEN price >= 2000000 AND price < 3000000 THEN 'between 2 and 3 million'
            WHEN price >= 3000000 AND price < 4000000 THEN 'between 3 and 4 million'
            WHEN price >= 4000000 AND price < 5000000 THEN 'between 4 and 5 million'
            WHEN price >= 5000000 AND price < 6000000 THEN 'between 5 and 6 million'
            WHEN price >= 6000000 AND price < 7000000 THEN 'between 6 and 7 million'
            WHEN price >= 7000000 AND price < 8000000 THEN 'between 7 and 8 million'
            WHEN price >= 8000000 AND price < 10000000 THEN 'between 8 and 10 million'
            WHEN price >= 10000000 AND price < 15000000 THEN 'between 10 and 15 million'
            WHEN price > 15000000  THEN 'above 15million' END AS price_categories,
COUNT(*)
FROM listings 
GROUP BY 1
ORDER BY 2 DESC



-- 4. What regions or cities have the highest and lowest average car prices for a specific model?
SELECT make, city , previous_ownership, COUNT(*) no_of_vehicles, AVG(price) av_price
FROM listings
GROUP BY 1, 2, 3
HAVING Make in ('Toyota') and previous_ownership like 'Foreign Used'
ORDER BY 1, 1 DESC;



-- 5. What are the most and least listed car brands and models?
SELECT make, COUNT(*)
FROM listings
GROUP BY 1
ORDER BY 2 DESC

SELECT make, model, COUNT(*)
FROM listings
GROUP BY 1, 2
ORDER BY 3 DESC



-- 6. Which color variants are most common and do they influence car pricing?#
SELECT color, COUNT(*), AVG(price)
FROM listings
GROUP BY 1
ORDER BY 2 DESC