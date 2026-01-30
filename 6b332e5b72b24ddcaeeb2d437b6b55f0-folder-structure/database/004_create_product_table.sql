# Epic Title: Add New Product

CREATE TABLE IF NOT EXISTS `backend_product` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL UNIQUE,
    `price` decimal(10,2) NOT NULL,
    `description` text NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;