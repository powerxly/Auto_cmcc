#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com


# 创建ketest数据库sql语句
create_database = 'CREATE DATABASE IF NOT EXISTS test_elements DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'
 
# 创建testdata表
drop_table = """drop table if exists testdata;"""
create_table = """
CREATE TABLE testdata(
  id int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  kename varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '课程名称',
  teacher varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '老师',
  test_result varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (id) USING BTREE,
  UNIQUE INDEX kenam(kename) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '测试数据表' ROW_FORMAT = Dynamic;
"""
