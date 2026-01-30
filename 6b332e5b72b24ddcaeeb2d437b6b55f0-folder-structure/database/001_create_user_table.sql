# Epic Title: User Registration

CREATE TABLE IF NOT EXISTS `backend_user` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `password` varchar(128) NOT NULL,
    `last_login` datetime(6) DEFAULT NULL,
    `is_superuser` tinyint(1) NOT NULL,
    `username` varchar(150) NOT NULL UNIQUE,
    `email` varchar(254) NOT NULL UNIQUE,
    `is_staff` tinyint(1) NOT NULL,
    `is_active` tinyint(1) NOT NULL,
    `date_joined` datetime(6) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;