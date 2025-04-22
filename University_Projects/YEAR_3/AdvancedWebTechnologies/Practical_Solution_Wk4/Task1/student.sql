CREATE TABLE `student` (
  `sunumber` int(11) NOT NULL,
  `StudentID` varchar(10) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `student` (`sunumber`, `StudentID`, `Name`, `Address`, `email`) VALUES
(1, 'e70d3', 'Joe Bloggs 2', '2 The Road', '2@2.com'),
(2, 'e70d4', 'Joe Bloggs 3', '3 The Road', '3@2.com'),
(3, 'u8eg4', 'Joe Bloggs', '1 The Road', '1@2.com');

ALTER TABLE `student`
  ADD PRIMARY KEY (`StudentID`);
