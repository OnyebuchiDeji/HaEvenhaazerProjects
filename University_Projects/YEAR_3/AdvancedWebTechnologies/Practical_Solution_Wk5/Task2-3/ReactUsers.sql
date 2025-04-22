SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE IF NOT EXISTS `ReactUsers` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL DEFAULT '',
  `phone` varchar(14) NOT NULL DEFAULT '0',
  `email` varchar(30) NOT NULL DEFAULT '',
  `comment` varchar(500) NOT NULL DEFAULT '',
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=36 ;


INSERT INTO `ReactUsers` (`id`, `username`, `phone`, `email`, `comment`) VALUES
(1, 'DeoJo', '2432423423', 'ethilsun@gmail.com', 'The goated!'),
(2, 'RuiMx', '0902382947', 'ruithehim@gmail.com', "Whos here in 2075?");