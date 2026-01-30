# Epic Title: Product Categorization

CREATE TABLE IF NOT EXISTS `catalog_category` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `parent_category_id` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`parent_category_id`) REFERENCES `catalog_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;