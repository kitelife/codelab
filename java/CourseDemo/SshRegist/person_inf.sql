/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50525
Source Host           : localhost:3306
Source Database       : javaee

Target Server Type    : MYSQL
Target Server Version : 50525
File Encoding         : 65001

Date: 2012-07-29 14:31:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `person_inf`
-- ----------------------------
DROP TABLE IF EXISTS `person_inf`;
CREATE TABLE `person_inf` (
  `name` varchar(50) DEFAULT NULL,
  `age` int(5) DEFAULT NULL,
  `person_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of person_inf
-- ----------------------------
INSERT INTO `person_inf` VALUES ('linux', '100', '1');
INSERT INTO `person_inf` VALUES ('xiayf', '25', '2');
