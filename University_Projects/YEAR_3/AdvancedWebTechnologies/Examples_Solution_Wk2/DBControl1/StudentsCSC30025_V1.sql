-- These kinds of tables are stuff one imports into the phpAdminSQL DB interface

CREATE TABLE `StudentsCSC30025_V1`
(
    `suNumber` int(11) NOT NULL,
    `StudentID` varchar(10) NOT NULL,
    `FName` varchar(50) DEFAULT NULL,
    `LName` varchar(50) DEFAULT NULL,
    `Address` varchar(100) DEFAULT NULL,
    `Email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `StudentsCSC30025_V1`
(   `suNumber`, `StudentID`, `FName`, `LName`,
    `Address`, `Email`
)
VALUES
(1, 'x7e30', 'Ebenezer', 'Ayo-Metibemu', 'The Oaks', 'x7e30@students.keele.ac.uk'),
(2, 'e70d4', 'Bernard', 'Hackwell', 'The Coffee Shop', 'bernardthecoffemaker@gmail.com'),
(3, 'u8eg4', 'Yan', 'Chrernikov','The Hazel Estate, Walnut District', 'yanyan@gmail.com');

ALTER TABLE `StudentsCSC30025_V1` ADD PRIMARY KEY (`StudentID`);