CREATE TABLE `Practical3` ( 
 `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, 
 `username` varchar(255) NOT NULL, 
 `password` varchar(255) NOT NULL, 
 `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
) 
