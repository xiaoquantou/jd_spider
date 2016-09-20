/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50621
Source Host           : 127.0.0.1:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2016-09-20 19:05:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jd_goods
-- ----------------------------
DROP TABLE IF EXISTS `jd_goods`;
CREATE TABLE `jd_goods` (
  `ID` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `comment_num` varchar(255) DEFAULT NULL,
  `shop_name` varchar(255) DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `commentVersion` varchar(255) DEFAULT NULL,
  `score1count` varchar(255) DEFAULT NULL,
  `score2count` varchar(255) DEFAULT NULL,
  `score3count` varchar(255) DEFAULT NULL,
  `score4count` varchar(255) DEFAULT NULL,
  `score5count` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jd_goods
-- ----------------------------
