-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema reseñas_musica
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema reseñas_musica
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `reseñas_musica` DEFAULT CHARACTER SET utf8 ;
USE `reseñas_musica` ;

-- -----------------------------------------------------
-- Table `reseñas_musica`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reseñas_musica`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(245) NULL,
  `password` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `reseñas_musica`.`bandas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reseñas_musica`.`bandas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `genero` VARCHAR(200) NULL,
  `nombre` VARCHAR(200) NULL,
  `release_date` DATE NULL,
  `comentarios` TEXT NULL,
  `pais_banda` VARCHAR(200) NULL,
  `estrellas` INT(5) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_bandas_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_bandas_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `reseñas_musica`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
