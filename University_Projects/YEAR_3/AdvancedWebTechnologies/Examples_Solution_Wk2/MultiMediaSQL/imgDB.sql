--
-- Table structure for table `l10_files`
--  was uploaded to phpmyadmin to create the Table `P2Imgs`
--

CREATE TABLE `P2Imgs` (
  `id` int(11) NOT NULL auto_increment primary key,
  `filename` varchar(40) NOT NULL,
  `filepath` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
