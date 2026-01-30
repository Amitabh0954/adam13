# Epic Title: Password Recovery

CREATE TABLE IF NOT EXISTS `account_passwordresettoken` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL,
    `token` varchar(36) NOT NULL,
    `created_at` datetime NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `token` (`token`),
    KEY `user_id` (`user_id`),
    CONSTRAINT `account_passwordresettoken_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `account_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;