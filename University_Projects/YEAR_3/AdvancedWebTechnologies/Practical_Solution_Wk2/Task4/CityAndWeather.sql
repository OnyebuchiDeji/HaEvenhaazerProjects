-- These kinds of tables are stuff one imports into the phpAdminSQL DB interface
-- No comma should be at the end of the last parameter of the table column specification

CREATE TABLE `CityAndWeather`
(
    `City` varchar(100) NOT NULL,
    `Time` varchar(100) NOT NULL,
    `Temperature` varchar(100) DEFAULT NULL  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;