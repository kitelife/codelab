/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50525
Source Host           : localhost:3306
Source Database       : hibernate

Target Server Type    : MYSQL
Target Server Version : 50525
File Encoding         : 65001

Date: 2012-07-21 15:31:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `person_inf`
-- ----------------------------
DROP TABLE IF EXISTS `person_inf`;
CREATE TABLE `person_inf` (
  `person_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  PRIMARY KEY (`person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of person_inf
-- ----------------------------
INSERT INTO `person_inf` VALUES ('1', 'crazyit.org', '29');
INSERT INTO `person_inf` VALUES ('2', 'crazyit.org', '29');
INSERT INTO `person_inf` VALUES ('4', 'crazyit.org', '29');
