SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE IF NOT EXISTS `CountriesAJAX` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '',
  `class` varchar(10) NOT NULL DEFAULT '',
  `mark` int(3) NOT NULL DEFAULT '0',
  `sex` varchar(6) NOT NULL DEFAULT 'male',
  `city` varchar(35) NOT NULL DEFAULT '',
  `country` varchar(3) NOT NULL DEFAULT '',
  `state` varchar(20) NOT NULL DEFAULT '',
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=36 ;


INSERT INTO `CountriesAJAX` (`id`, `name`, `class`, `mark`, `sex`, `city`, `country`, `state`) VALUES
(1, 'John Deo', 'Four', 75, 'female', 'London', 'GBR', 'England'),
(2, 'Max Ruin', 'Three', 85, 'male', 'Hyderabad', 'IND', 'Andhra Pradesh'),
(3, 'Krish Star', 'Four', 60, 'female', 'Sheffield', 'GBR', 'England'),
(4, 'John Mike', 'Four', 60, 'female', 'Vishakhapatnam', 'IND', 'Andhra Pradesh'),
(5, 'My John Rob', 'Fifth', 78, 'male', 'Los Angeles', 'USA', 'California'),
(6, 'Asruid', 'Five', 85, 'male', 'Birmingham', 'GBR', 'England'),
(7, 'Tes Qry', 'Six', 78, 'male', 'Madurai', 'IND', 'Tamil Nadu'),
(8, 'Ronald', 'Six', 89, 'female', 'San Diego', 'USA', 'California'),
(9, 'Recky', 'Six', 94, 'female', 'Ajmer', 'IND', 'Rajasthan'),
(10, 'Kty', 'Seven', 88, 'female', 'Surendranagar', 'IND', 'Gujarat'),
(11, 'Bigy', 'Seven', 88, 'female', 'Houston', 'USA', 'Texas'),
(12, 'Tade Row', 'Four', 88, 'male', 'Beawar', 'IND', 'Rajasthan'),
(13, 'Gimmy', 'Four', 88, 'male', 'Glasgow', 'GBR', 'Scotland'),
(14, 'Tinny', 'Nine', 18, 'male', 'Gondiya', 'IND', 'Maharashtra'),
(15, 'Jackly', 'Nine', 65, 'female', 'San Jose', 'USA', 'California'),
(16, 'Babby John', 'Four', 69, 'female', 'Ahmedabad', 'IND', 'Gujarat'),
(17, 'Herod', 'Eight', 79, 'male', 'Bhind', 'IND', 'Madhya Pradesh'),
(18, 'Tiddy Now', 'Seven', 78, 'male', 'Liverpool', 'GBR', 'England'),
(19, 'Giff Tow', 'Seven', 88, 'male', 'Pune', 'IND', 'Maharashtra'),
(20, 'Big Nose', 'Three', 81, 'female', 'Jacksonville', 'USA', 'Florida'),
(21, 'Rojj Base', 'Seven', 86, 'female', 'Surat', 'IND', 'Gujarat'),
(22, 'Tess Played', 'Seven', 55, 'male', 'Cleveland', 'USA', 'Ohio'),
(23, 'Reppy Red', 'Six', 79, 'female', 'Seattle', 'USA', 'Washington'),
(24, 'Binn Rott', 'Seven', 90, 'female', 'Edinburgh', 'GBR', 'Scotland'),
(25, 'Kenn Rein', 'Six', 96, 'female', 'Kalyan', 'IND', 'Maharashtra'),
(26, 'Gain Toe', 'Seven', 69, 'male', 'Tucson', 'USA', 'Arizona'),
(27, 'Rows Noump', 'Six', 88, 'female', 'Jaipur', 'IND', 'Rajasthan');

