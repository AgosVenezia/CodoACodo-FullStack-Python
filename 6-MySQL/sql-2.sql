/* 5. Listar el nombre, la cantidad de habitantes, la superficie y una columna llamada 'Densidad' 
con el resultado de la densidad poblacional de todos los países. (Se esperan 4 columnas y 239 registros).
*/
USE world;

SELECT `Name`,
    `country`.`SurfaceArea`,
    `country`.`Population`,
    Population/SurfaceArea AS Densidad -- Campo calculado
FROM `country`;

/*
10. Listar nombre y continente de los cien países con mayor expectativa de vida. 
Si hubiera países que tengan la misma expectativa de vida, mostrar primero a los de menor 
superficie. (Se esperan 2 columnas y 100 registros). (ORDENAR)
*/

SELECT `Name`,
	Continent -- ,
--    LifeExpectancy,
--    `country`.`SurfaceArea`
FROM `country`
ORDER BY LifeExpectancy DESC,
SurfaceArea ASC
LIMIT 100 -- 100 registros
;

/*
12. Listar todos los datos de los países cuya expectativa de vida supere los setenta y cinco años, 
ordenados bajo este concepto de forma ascendente. (Se esperan 15 columnas y 62 registros).
*/
SELECT *
FROM `country`
WHERE LifeExpectancy > 75
-- ORDER BY LifeExpectancy ASC
ORDER BY LifeExpectancy
;

/*
12(bis). Listar todos los datos de los países cuya expectativa de vida supere los setenta y cinco años, 
ordenados bajo este concepto de forma ascendente. (Se esperan 15 columnas y 62 registros).
Agrego: de Sudamérica (4 registros)/que NO sean de Sudamérica (58 reg.)/El nombre del país comience con A (7 reg.)
*/
SELECT *
FROM `country`
WHERE LifeExpectancy > 75
-- AND Continent LIKE 'South America'
-- AND Continent NOT LIKE 'South America'
AND `Name` LIKE 'A%'
-- ORDER BY LifeExpectancy ASC
ORDER BY LifeExpectancy
;

/*
17. Listar todos los datos de los países situados en Europa, Asia o Sudamérica. 
(Se esperan 15 columnas y 111 registros).
*/
SELECT *
FROM `country`
WHERE Continent IN ('Europe', 'Asia', 'South America') -- IN
-- WHERE Continent LIKE 'Europe'
-- OR Continent LIKE 'Asia'
-- OR Continent LIKE 'South America' -- OR
;

/*
20. Listar todos los datos de las ciudades de entre 125 mil y 130 mil habitantes. 
(Se esperan 5 columnas y 138 registros).
*/
SELECT `city`.`ID`,
    `city`.`Name`,
    `city`.`CountryCode`,
    `city`.`District`,
    `city`.`Population`
FROM city
-- WHERE Population >= 125000 AND Population <= 130000
WHERE Population BETWEEN 125000 AND 130000
;

-- JOIN
/* 26. Listar los nombres de los países sudamericanos junto a los nombres (alias 'Capital') 
de sus capitales. (Se esperan 2 columnas y 14 registros).
*/
SELECT country.`Name` AS Pais, -- ALIAS
city.`Name` AS Capital, -- Error Code: 1052. Column 'Name' in field list is ambiguous
CountryCode
FROM `country`, city -- Error Code: 1054. Unknown column 'CountryCode' in 'field list'
WHERE Continent LIKE 'South America'
-- AND `Code` = CountryCode -- NO cumple con la consigna (me trae TODAS las ciudades de cada país)
AND Capital = city.ID
;
-- SoloLearn: MySQL

-- INNER JOIN (ídem 26)

-- GROUP BY (HAVING)
