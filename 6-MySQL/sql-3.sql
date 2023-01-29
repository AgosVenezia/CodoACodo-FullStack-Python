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
SELECT country.`Name` AS Pais,
	city.`Name` AS Capital,
	CountryCode
FROM `country`
INNER JOIN city ON Capital = city.ID
WHERE Continent LIKE 'South America'
;
-- to-do: AGREGAR EL LENGUAJE OFICIAL DEL PAÍS

/*
24. Listar todos los datos de los países cuyo nombre sea compuesto 
 (más de una palabra). (Se esperan 15 columnas y 66 registros).
*/ 
SELECT * 
FROM world.country
WHERE `Name` LIKE '% %'
-- WHERE RTRIM(`Name`) LIKE '% '
-- WHERE `Name` LIKE '% ' -- EL CAMPO TIENE QUE SER VARCHAR
;

/*
29. Listar los lenguajes oficiales, junto al nombre de sus respectivos países, 
donde la cantidad de habitantes de dicho país esté entre un millón y tres millones. 
(Se esperan 2 columnas y 14 registros).
*/
SELECT `Language` AS lenguaje, 
co.`Name` AS pais
-- co.Population AS poblacion
FROM countrylanguage
INNER JOIN country co ON countrylanguage.CountryCode = co.`Code`
WHERE co.Population BETWEEN 1000000 AND 3000000
AND IsOfficial = 'T'
;

/*
29bis. Mostrar todos los países del lado izquierdo. 

*/
-- LEFT JOIN
SELECT co.`Name` AS pais,
`Language` AS lenguaje, 
Code
FROM country co
LEFT JOIN countrylanguage ON countrylanguage.CountryCode = co.`Code`
-- WHERE co.Population BETWEEN 1000000 AND 3000000
-- AND IsOfficial = 'T'
;

-- GROUP BY (HAVING)
/*37.
37. Mostrar según la tabla de países, la cantidad total de población, 
la población máxima, la población mínima y el promedio de población, 
por cada continente. 
(Se esperan 5 columnas y 7 registros).
37bis. Contar la cantidad de países por continente.
*/
SELECT Continent, 
COUNT(*) AS cantidad,
SUM(Population) AS poblacion,
MAX(Population),
MIN(Population),
AVG(Population)
FROM country
GROUP BY Continent
-- ORDER BY Continent
ORDER BY COUNT(*) DESC
;

/*
48. Mostrar los distritos, junto al nombre del país al que pertenecen, 
cuya población total (también listada) no supere los diez mil habitantes. 
(Se esperan 3 columnas y 35 registros).
*/
SELECT co.Name AS Pais, 
ci.District AS Distrito,
SUM(ci.Population) AS Poblacion
FROM city ci
INNER JOIN country co ON ci.CountryCode=co.Code
WHERE ci.Population >=100 -- 48bis (no considerar países con población menor a 100)
GROUP BY co.Name, ci.District
HAVING SUM(ci.Population)<=10000
ORDER BY ci.District
;