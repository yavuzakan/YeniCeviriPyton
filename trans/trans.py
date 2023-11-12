from googletrans import Translator
import sqlite3


def down(id,trans):

    detector = Translator()

    dec_lan = detector.detect(trans)

   # print(dec_lan)

    translation = detector.translate(trans, dest="tr")
    #print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    #print(translation.origin)
    
    #print(translation.text)
    veri2 = translation.text
    update(id,veri2)

def update(id, veri2):

    try:
        conn = sqlite3.connect('deneme.db')
        cursor = conn.cursor()
        sql = "Update data set veri2 = ? where id = ?"
        data = (veri2, id)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
      
    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)





try:
  
    conn = sqlite3.connect('deneme.db')
    cursor = conn.cursor()
    
    query = "select * FROM data where veri2 IS NULL "
    cursor.execute(query)
   
    records = cursor.fetchall()
    #print("Total rows are:  ", len(records))
    for row in records:
       # print("Start...")
      
        down(row[0],row[1])

    cursor.close()    
    


except sqlite3.Error as error:
    print(error)    






