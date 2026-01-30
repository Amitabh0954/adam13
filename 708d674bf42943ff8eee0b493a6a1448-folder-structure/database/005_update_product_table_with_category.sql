# Epic Title: Product Categorization

ALTER TABLE `catalog_product`
ADD COLUMN `category_id` int(11) NOT NULL AFTER `description`,
ADD CONSTRAINT `fk_category` FOREIGN KEY (`category_id`) REFERENCES `catalog_category`(`id`);