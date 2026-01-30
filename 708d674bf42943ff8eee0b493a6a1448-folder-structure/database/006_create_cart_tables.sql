# Epic Title: Add Product to Shopping Cart

CREATE TABLE IF NOT EXISTS `cart_cart` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `user_id` int(11) DEFAULT NULL,
    `session_id` varchar(255) DEFAULT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `cart_cartitem` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `cart_id` int(11) NOT NULL,
    `product_id` int(11) NOT NULL,
    `quantity` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`cart_id`) REFERENCES `cart_cart` (`id`),
    FOREIGN KEY (`product_id`) REFERENCES `catalog_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;