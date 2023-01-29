USE inupde;

SELECT * 
FROM inupde.clientes
;

USE world;

/*
Ejercicio 48.
Mostrar los distritos, junto al nombre del país al que pertenecen, 
cuya población total (también listada) no supere los diez mil habitantes. 
(Se esperan 3 columnas y 35 registros). 

Este lo intente, pero no me dio bien (Dejo el query que arme
*/
SELECT 	country.`Name`, 
	city.District, 
	SUM(city.Population) AS 'Poblacion'
FROM country
INNER JOIN city ON country.code=city.countrycode
GROUP BY country.`Name`, 
city.District
-- HAVING 'Poblacion'<10000;
HAVING SUM(city.Population)<10000
;

-- EJERCICIOS DE UPDATE
-- Ejercicio 55. Agregar un cero a la izquierda de todos los DNI con exactamente siete cifras. 
-- (Se esperan 1173 registros afectados).
-- SELECT dni, LPAD(dni, 8, '0') AS Rellenado
SELECT COUNT(1)
FROM clientes
WHERE LENGTH(dni)<=7;

UPDATE `clientes`
SET
dni = LPAD(dni, 8, '0')
WHERE LENGTH(dni)<=7; -- 987 row(s) affected Rows matched: 987  Changed: 987  Warnings: 0

-- Ejercicio 56. Agregar una tilde a todos los clientes llamados 'Nicolas' como único nombre para que el mismo pase a ser 'Nicolás'. (Se esperan 3 registros afectados).

-- Ejercicio 57. Poner en mayúsculas los apellidos de los clientes cuya nacionalidad no sea 'Argentina'. (Se esperan 4450 registros afectados).

