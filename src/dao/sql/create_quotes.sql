CREATE TABLE IF NOT EXISTS `quotes` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `quote` varchar(255) COLLATE utf8_bin NOT NULL,
    `author` varchar(255) COLLATE utf8_bin NOT NULL,
    `tags` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1;