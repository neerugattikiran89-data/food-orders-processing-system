USE food_delivery;

SELECT
    City,
    COUNT(*) AS total_orders,
    ROUND(AVG(`Time_taken(min)`), 2) AS avg_delivery_time
FROM food_orders
GROUP BY City
ORDER BY avg_delivery_time DESC;



SELECT
    Road_traffic_density,
    COUNT(*) AS total_orders,
    ROUND(AVG(`Time_taken(min)`), 2) AS avg_delivery_time
FROM food_orders
GROUP BY Road_traffic_density
ORDER BY avg_delivery_time DESC;



SELECT
    Weatherconditions,
    COUNT(*) AS total_orders,
    ROUND(AVG(`Time_taken(min)`), 2) AS avg_delivery_time
FROM food_orders
GROUP BY Weatherconditions
ORDER BY avg_delivery_time DESC;



SELECT
    Type_of_vehicle,
    COUNT(*) AS total_orders,
    ROUND(AVG(`Time_taken(min)`), 2) AS avg_delivery_time
FROM food_orders
GROUP BY Type_of_vehicle
ORDER BY avg_delivery_time DESC;

SELECT
    Festival,
    COUNT(*) AS total_orders,
    ROUND(AVG(`Time_taken(min)`), 2) AS avg_delivery_time
FROM food_orders
GROUP BY Festival
ORDER BY avg_delivery_time DESC;


SELECT
    multiple_deliveries,
    COUNT(*) AS total_orders,
    ROUND(AVG(`Time_taken(min)`), 2) AS avg_delivery_time
FROM food_orders
GROUP BY multiple_deliveries
ORDER BY multiple_deliveries;



SELECT
    Type_of_order,
    COUNT(*) AS total_orders,
    ROUND(AVG(`Time_taken(min)`), 2) AS avg_delivery_time
FROM food_orders
GROUP BY Type_of_order
ORDER BY avg_delivery_time DESC;