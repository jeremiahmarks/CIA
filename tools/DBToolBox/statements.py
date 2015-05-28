#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-05-27 22:09:50
# @Last Modified 2015-05-27
# @Last Modified time: 2015-05-27 23:21:23


class stmts(object):
    def _addtab(self, tablename, cols, cursor):
        stmt="""CREATE TABLE %s (""" %(tablename)
        for colDiscriptor in cols:
            stmt+=" ?,"
        stmt=stmt[:-1] + ");"
        cursor.execute(stmt,cols)
        cursor.commit()
    # def _drptab():

    #     stmt=stmt[:-1] + ");"
    #     cursor.execute(stmt,cols)
    #     cursor.commit()
    def _update():

        stmt=stmt[:-1] + ");"
        cursor.execute(stmt,cols)
        cursor.commit()
    def _insert():

        stmt=stmt[:-1] + ");"
        cursor.execute(stmt,cols)
        cursor.commit()
    def _select():
        pass