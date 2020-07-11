
with open("bibleplan.csv", "r") as bible_read: # open the input file for reading
    with open("RGC-Bible_Reading_Plan-2020-NT.xml","w") as bible_write: # open the output file for writing

        bible_write.write("""<plan>\n""") # initial tag in XML file
        bible_write.write("""<title></title>\n""") # initial tag in XML file

        while True:

            read_line = bible_read.readline()
            day, book = tuple(read_line.split(",")) # assuming CSV file
            day = day.strip(" ")
            bible_write.write("<reading>\n")
            bible_write.write("<day>{}</day>\n".format(int(day.split(" ")[1])))

            if(len(book) == 1) : # empty book label
                book = "PRAISE THE LORD"

            bible_write.write("<passage>{}</passage>".format(book)) # passage tag
            bible_write.write("</reading>")
            if("365" in day): # end of file
                break
        bible_write.write("</plan>")
