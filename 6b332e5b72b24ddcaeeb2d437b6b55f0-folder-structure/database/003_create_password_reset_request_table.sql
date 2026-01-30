# Epic Title: Password Recovery

CREATE TABLE IF NOT EXISTS `backend_passwordresetrequest` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) NOT NULL,
    `token` varchar(36) NOT NULL UNIQUE,
    `created_at` datetime(6) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `backend_user`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;