with open("bibleplan.xml", "w") as bible:
    day = 1
    bible.write("""<plan>\n""")
    bible.write("""<title></title>\n""")
    while True:
        book = input("Which book do you want to add? ")
        if(book.upper() == "QUIT"):
            break

        chapter = input("Which chapters? ")
        if(chapter.upper() == "QUIT"):
            break
        elif len(chapter) == 1 :
            verse = input("Which verses? ")
            if(verse.upper() == "QUIT"):
                break

        if("-" in chapter):
            chapters = chapter.split("-")
            for j in range(int(chapters[0]), int(chapters[1]) + 1):
                bible.write("<reading>\n")
                bible.write("<day>{}</day>\n".format(day))
                bible.write("<passage>{} {}</passage>\n".format(book,j))
                bible.write("</reading>\n")
                day += 1
        else:
            bible.write("<reading>\n")
            bible.write("<day>{}</day>\n".format(day))
            bible.write("<passage>{} {}</passage>\n".format(book,chapter))
            bible.write("</reading>\n")
        day += 1
    bible.write("</plan>")
