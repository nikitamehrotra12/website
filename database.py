import sqlite3
import os

def clone_pairs(connection,  users, current_userid):
    c = connection.cursor()
    start_index = users[current_userid]
    clones_per_user = 85
    print(start_index)
    query = "select * from CLONE_PAIRS where id >= "+str(start_index)+" and id < " + str(start_index+clones_per_user)
    cur = c.execute(query)
    # connection.close()
    return cur.fetchall()


def java_content(current_clone_no, clone_pairs):
    row = clone_pairs[current_clone_no-1]
    functionality_id = row[1]
    code_file_1 = row[2]
    code_file_2 = row[5]
    info = [code_file_1,code_file_2,functionality_id]
    print(code_file_1)
    dir_path = "C:/Users/navdh/Desktop/project/bcb_reduced/" + str(functionality_id)
    folders = ["/default","/selected","/sample"]
    contents = ""
    contents1 = ""
    for folder in folders:
        dir_path1 = dir_path + folder
        files = os.listdir(dir_path1)
        for f in files:
            if (f == code_file_1):
                fd = open(dir_path1+'/'+f,'r')
                print("yes1")
                contents = fd.read()
            if (f == code_file_2):
                fd = open(dir_path1+'/'+f,'r')
                print("yes2")
                contents1 = fd.read()
    return contents, contents1, info


def update_true(current_userid, current_clone_no, users):
    connection = sqlite3.connect("clones.db")
    print("entered")
    c = connection.cursor()
    index = users[current_userid] + current_clone_no - 1
    length = len(current_userid)
    participant = current_userid[length-1]
    query = 'UPDATE CLONE_PAIRS SET participant_'+participant+ '= 1 WHERE id = ' + str(index)
    print(query)
    c.execute(query)
    connection.commit()
    # connection.close()

def update_false(current_userid, current_clone_no, users):
    connection = sqlite3.connect("clones1.db")
    c = connection.cursor()
    index = users[current_userid] + current_clone_no - 1
    length = len(current_userid)
    participant = current_userid[length-1]
    query = 'UPDATE CLONE_PAIRS SET participant_'+participant+ '= 0 WHERE id = ' + str(index)
    c.execute(query)
    connection.commit()
    # connection.close()



# content, content1 = java_content(sqlite3.connect("clones.db"))
# print(len(content1))



