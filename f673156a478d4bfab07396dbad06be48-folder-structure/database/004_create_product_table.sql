# Epic Title: Add New Product

CREATE TABLE IF NOT EXISTS `catalog_product` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL UNIQUE,
    `description` text NOT NULL,
    `price` decimal(10, 2) NOT NULL,
    `category_id` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`category_id`) REFERENCES `catalog_category` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;