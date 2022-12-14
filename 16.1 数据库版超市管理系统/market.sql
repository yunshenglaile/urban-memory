/*
 Navicat Premium Data Transfer

 Source Server         : 51
 Source Server Type    : MySQL
 Source Server Version : 50556
 Source Host           : localhost:3306
 Source Schema         : market

 Target Server Type    : MySQL
 Target Server Version : 50556
 File Encoding         : 65001

 Date: 13/12/2022 09:20:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `count` float(255, 0) NULL DEFAULT NULL,
  `amount` float(255, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES (1, '1212', 33, 187.00);
INSERT INTO `orders` VALUES (2, '1204', 33, 179.00);
INSERT INTO `orders` VALUES (3, '1205', 33, 180.00);
INSERT INTO `orders` VALUES (4, '1206', 33, 181.00);
INSERT INTO `orders` VALUES (5, '1207', 33, 182.00);
INSERT INTO `orders` VALUES (6, '1208', 33, 183.00);
INSERT INTO `orders` VALUES (7, '1209', 33, 184.00);
INSERT INTO `orders` VALUES (8, '1210', 33, 185.00);
INSERT INTO `orders` VALUES (9, '1211', 33, 186.00);
INSERT INTO `orders` VALUES (11, '1213', 33, 188.00);
INSERT INTO `orders` VALUES (15, '4879', 200, 196.00);
INSERT INTO `orders` VALUES (17, '8218', 20, 3225.60);
INSERT INTO `orders` VALUES (19, '9649', 10, 1612.80);
INSERT INTO `orders` VALUES (20, '2035', 1, 0.98);
INSERT INTO `orders` VALUES (21, '4538', 5, 130.50);

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `price` float(10, 2) NULL DEFAULT NULL,
  `discount` float(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 36 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of products
-- ----------------------------
INSERT INTO `products` VALUES (3, '1034', '??????', 1.00, 0.98);
INSERT INTO `products` VALUES (4, '1035', '?????????', 168.00, 0.96);
INSERT INTO `products` VALUES (5, '1036', '?????????', 29.00, 0.90);
INSERT INTO `products` VALUES (14, '3808', '??????', 2.60, 0.60);
INSERT INTO `products` VALUES (16, '5881', '??????', 5.00, 0.80);
INSERT INTO `products` VALUES (17, '2772', '?????????', 10.00, 1.00);
INSERT INTO `products` VALUES (18, '9139', '??????sod???', 9.90, 1.00);
INSERT INTO `products` VALUES (19, '8162', '??????', 9.90, 1.00);
INSERT INTO `products` VALUES (20, '6769', '??????', 12.50, 1.00);
INSERT INTO `products` VALUES (21, '7213', '?????????', 2.50, 1.00);
INSERT INTO `products` VALUES (22, '7995', '?????????', 8.50, 1.00);
INSERT INTO `products` VALUES (23, '1893', '?????????', 20.00, 1.00);
INSERT INTO `products` VALUES (24, '1252', '?????????', 200.00, 1.00);
INSERT INTO `products` VALUES (25, '6100', '????????????', 20.00, 1.00);
INSERT INTO `products` VALUES (26, '6180', '????????????', 20.00, 1.00);
INSERT INTO `products` VALUES (27, '2012', '????????????', 19.90, 1.00);
INSERT INTO `products` VALUES (28, '8041', '?????????', 19.90, 1.00);
INSERT INTO `products` VALUES (29, '1271', '?????????', 5.90, 1.00);
INSERT INTO `products` VALUES (30, '3664', 'Rio?????????', 12.90, 1.00);
INSERT INTO `products` VALUES (31, '8666', '????????????', 6.90, 1.00);
INSERT INTO `products` VALUES (32, '6990', '???????????????', 6.90, 1.00);
INSERT INTO `products` VALUES (33, '5600', '???????????????', 6.90, 1.00);
INSERT INTO `products` VALUES (34, '7073', '???????????????2.2???x2???', 1900.00, 1.00);
INSERT INTO `products` VALUES (35, '3758', '????????????60???4K??????????????????', 3999.00, 1.00);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(15) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `password` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  `nickname` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'zhangsan', '123456', '??????');
INSERT INTO `users` VALUES (2, 'lisi', '123456', '??????');
INSERT INTO `users` VALUES (3, 'wangwu', '123456', '??????');
INSERT INTO `users` VALUES (4, 'maliu', '123456', '??????');
INSERT INTO `users` VALUES (5, 'aaa', 'aaa', 'aaa');
INSERT INTO `users` VALUES (6, 'aaa', 'ddddd', 'dddd');
INSERT INTO `users` VALUES (7, 'zhangxiao', '14250514250', '??????');
INSERT INTO `users` VALUES (8, '??????', '14250514250', '????????????');
INSERT INTO `users` VALUES (9, '?????????', '14250514250', '?????????');
INSERT INTO `users` VALUES (10, '??????????????????', '???????????????', '???????????????');
INSERT INTO `users` VALUES (11, 'zhangyunsheng77', 'zhangyunsheng88', '?????????77');

SET FOREIGN_KEY_CHECKS = 1;
