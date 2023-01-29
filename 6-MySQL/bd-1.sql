-- Seleccionar un esquema
USE com1122;

-- Creo la BD
CREATE SCHEMA `com1122` ;

-- Creo una tabla
CREATE TABLE `com1122`.`alumnos` (
  `id` INT UNSIGNED NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `fecha_nacimiento` DATE NULL,
  PRIMARY KEY (`id`));

-- Elimino una tabla
-- DROP TABLE `com1122`.`alumnos`;

-- Modifico una tabla
/*
ALTER TABLE `com1122`.`alumnos` 
ADD COLUMN `edad` SMALLINT UNSIGNED NULL AFTER `apellido`;
*/

-- Consultar todos los registros
SELECT * FROM com1122.alumnos;
-- TRUNCATE com1122.alumnos;

-- Agregar/Eliminar/Actualizar un registro
INSERT INTO `com1122`.`alumnos` (`id`, `nombre`, `apellido`, `edad`, `fecha_nacimiento`) 
VALUES ('1', 'Ramiro', 'Escalante Leiva', '40', '19810101');
INSERT INTO `com1122`.`alumnos` (`id`, `nombre`, `apellido`) 
VALUES ('2', 'Juan', 'Perez'); -- Error Code: 1136. Column count doesn't match value count at row 1

-- DELETE FROM `com1122`.`alumnos`; -- WHERE `id`='2'; -- 2 row(s) affected

UPDATE alumnos SET edad=21, fecha_nacimiento='20000101' WHERE id=2;
