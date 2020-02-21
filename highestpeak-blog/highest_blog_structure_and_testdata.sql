/*
 Navicat Premium Data Transfer

 Source Server         : localMySQL
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : highest_blog

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 15/02/2020 17:02:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` char(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
  `star_send_num` int(11) NULL DEFAULT NULL,
  `stars` float(11, 0) NULL DEFAULT NULL,
  `create_time` datetime(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES (1, 'flask博客构建之路', '一片测试文章', 'nothing here', 10, 2, '2020-02-06 15:28:14');
INSERT INTO `article` VALUES (2, 'java后端', '文章测试', 'nothing here', 10, 3, '2020-02-15 15:29:07');
INSERT INTO `article` VALUES (4, 'java后端1', '文章测试', 'nothing here', 2, 5, '2020-02-15 15:29:07');
INSERT INTO `article` VALUES (6, 'java后端2', '文章测试', 'nothing here', 2, 5, '2020-02-15 15:29:07');
INSERT INTO `article` VALUES (7, 'java后端3', '文章测试', 'nothing here', 2, 4, '2020-02-15 15:29:07');
INSERT INTO `article` VALUES (8, 'java后端4', '文章测试', 'nothing here', 2, 3, '2020-02-15 15:29:07');

-- ----------------------------
-- Table structure for article_tags
-- ----------------------------
DROP TABLE IF EXISTS `article_tags`;
CREATE TABLE `article_tags`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) NULL DEFAULT NULL,
  `article_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tag_id`(`tag_id`) USING BTREE,
  INDEX `article_id`(`article_id`) USING BTREE,
  CONSTRAINT `article_tags_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `article_tags_ibfk_2` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of article_tags
-- ----------------------------
INSERT INTO `article_tags` VALUES (1, 1, 1);
INSERT INTO `article_tags` VALUES (2, 2, 1);
INSERT INTO `article_tags` VALUES (3, 3, 1);
INSERT INTO `article_tags` VALUES (4, 2, 7);
INSERT INTO `article_tags` VALUES (5, 3, 7);
INSERT INTO `article_tags` VALUES (6, 2, 6);
INSERT INTO `article_tags` VALUES (7, 4, 1);
INSERT INTO `article_tags` VALUES (8, 4, 7);

-- ----------------------------
-- Table structure for repo
-- ----------------------------
DROP TABLE IF EXISTS `repo`;
CREATE TABLE `repo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `repourl` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
  `create_time` datetime(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of repo
-- ----------------------------
INSERT INTO `repo` VALUES (1, 'https://api.github.com/repos/highestpeak/Highest-Blog', '2020-02-05 16:24:40');
INSERT INTO `repo` VALUES (2, 'https://api.github.com/repos/highestpeak/BlogArticle', '2020-02-12 16:24:51');
INSERT INTO `repo` VALUES (3, 'https://api.github.com/repos/highestpeak/ChannelChart', '2020-02-11 16:25:04');

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
  `create_time` datetime(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES (1, 'java', NULL, '2020-02-15 15:31:05');
INSERT INTO `tag` VALUES (2, 'python', NULL, '2020-02-04 15:31:15');
INSERT INTO `tag` VALUES (3, '后端', NULL, '2020-02-05 15:31:29');
INSERT INTO `tag` VALUES (4, '前端', NULL, '2020-01-28 15:31:39');

SET FOREIGN_KEY_CHECKS = 1;
