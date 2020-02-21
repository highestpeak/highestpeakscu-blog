import sqlite3
from config import sqllitePath

conn = sqlite3.connect(sqllitePath)
cursor = conn.cursor()


def createDB():
    cursor.execute(('CREATE TABLE "fileinfo" ('
                    '"id" NOT NULL PRIMARY KEY AUTOINCREMENT,'
                    '"filename" text,'
                    '"title" text NOT NULL,'
                    '"description" text,'
                    '"tags" text,'
                    '"createtime" text,'
                    '"cnblogid" text,'
                    ')'))


def closeDB():
    cursor.close()
    conn.close()


def rename(renameList):
    for name in renameList:
        cursor.execute('UPDATE fileinfo SET filename=? where filename=?',
                       (name[1], name[0]))
    conn.commit()


def getFileNameTitle(filename):
    cursor.execute('select title from fileinfo where filename=?', (filename,))
    values = cursor.fetchall()
    if values is None or len(values) < 1 or len(values[0]) < 1:
        return None
    return values[0][0]


def getFileTitleCnID(fileTitle):
    cursor.execute('select cnblogid from fileinfo where title=?', (fileTitle,))
    values = cursor.fetchall()
    if values is None or len(values) < 1 or len(values[0]) < 1:
        return None
    return values[0][0]


def isTitleIn(title):
    cursor.execute('select cnblogid from fileinfo where title=?', (title,))
    values = cursor.fetchall()
    if values is None or len(values) == 0:
        return False
    else:
        return True


def isFileNameIn(filename):
    cursor.execute('select cnblogid from fileinfo where filename=?', (filename,))
    values = cursor.fetchall()
    if values is None or len(values) == 0:
        return False
    else:
        return True


def isFileInfoChanged(md):
    cursor.execute('select description,tags,createtime from fileinfo where title=?', (md["title"],))
    values = cursor.fetchall()
    changed = False
    if values is None or len(values) == 0:
        changed = False
    else:
        changed = True if changed or values[0][0] != md["description"] else False
        changed = True if changed or values[0][1] != ",".join(md["tags"]) else False
        changed = True if changed or values[0][2] != md["create_time"] else False
    return changed


def writeFileInfo(fileRows):
    for file in fileRows:
        # 首次添加
        # 修改
        # 删除
        if file["type"] == "update":
            if isTitleIn(file["title"]):
                cursor.execute('UPDATE fileinfo SET filename=?,description=?,tags=?,createtime=?,cnblogid=? where title=?',
                               (file["filename"], file["description"], ",".join(file["tags"]), file["createtime"],
                                file["cnblogid"],
                                file["title"]))
            elif isFileNameIn(file["filename"]):
                cursor.execute('UPDATE fileinfo SET title=?,description=?,tags=?,createtime=?,cnblogid=? where filename=?',
                               (file["title"], file["description"], ",".join(file["tags"]), file["createtime"],
                                file["cnblogid"],
                                file["filename"]))
        elif file["type"] == "delete":
            cursor.execute('DELETE FROM fileinfo WHERE title = ?', (file["title"],))
        elif file["type"] == "post":
            cursor.execute(
                'INSERT INTO "fileinfo"("filename", "title", "description", "tags", "createtime", "cnblogid")'
                'VALUES (?,?,?,?,?,?)',
                (file["filename"], file["title"], file["description"],
                 ",".join(file["tags"]), file["createtime"], file["cnblogid"]))
        conn.commit()


if __name__ == '__main__':
    pass
