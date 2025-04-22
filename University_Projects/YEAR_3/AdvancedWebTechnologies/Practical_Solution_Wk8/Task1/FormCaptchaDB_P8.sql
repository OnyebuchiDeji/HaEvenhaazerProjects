create table FormCaptchaDB_P8(
    `id` int auto_increment NOT NULL primary key,
    `captcha_image_filename` varchar(40) NOT NULL ,
    `captcha_image_characters` varchar(30) NOT NULL 
    );


INSERT INTO `FormCaptchaDB_P8` (`id`, `captcha_image_filename`, `captcha_image_characters`) VALUES
(1, 'image1.jpg', 'Aeik2'),
(2, 'image2.jpg', 'ecb4f'),
(3, 'image3.jpg', '7PlBJ8'),
(4, 'image4.jpg', '24quz');