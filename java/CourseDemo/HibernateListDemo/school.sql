/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50525
Source Host           : localhost:3306
Source Database       : hibernate

Target Server Type    : MYSQL
Target Server Version : 50525
File Encoding         : 65001

Date: 2012-07-21 15:32:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `school`
-- ----------------------------
DROP TABLE IF EXISTS `school`;
CREATE TABLE `school` (
  `person_id` int(11) NOT NULL,
  `school_name` varchar(20) DEFAULT NULL,
  `list_order` int(11) NOT NULL,
  KEY `FKC9E15B74E6260A9B` (`person_id`),
  CONSTRAINT `FKC9E15B74E6260A9B` FOREIGN KEY (`person_id`) REFERENCES `person_inf` (`person_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of school
-- ----------------------------
INSERT INTO `school` VALUES ('4', '小学', '0');
INSERT INTO `school` VALUES ('4', '中学', '1');
