/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50621
Source Host           : 127.0.0.1:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2016-09-20 19:05:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jd_comment
-- ----------------------------
DROP TABLE IF EXISTS `jd_comment`;
CREATE TABLE `jd_comment` (
  `user_name` varchar(255) DEFAULT NULL,
  `user_ID` varchar(255) DEFAULT NULL,
  `userProvince` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `good_ID` varchar(255) DEFAULT NULL,
  `good_name` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `replyCount` varchar(255) DEFAULT NULL,
  `score` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `userRegisterTime` varchar(255) DEFAULT NULL,
  `productColor` varchar(255) DEFAULT NULL,
  `productSize` varchar(255) DEFAULT NULL,
  `userLevelName` varchar(255) DEFAULT NULL,
  `isMobile` varchar(255) DEFAULT NULL,
  `days` varchar(255) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jd_comment
-- ----------------------------
