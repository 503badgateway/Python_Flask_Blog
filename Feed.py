import os, json
Header = "<?xml version=\"1.0\"?><rss xmlns:g=\"http://base.google.com/ns/1.0\" version=\"2.0\">"
Footer = "</channel></rss>"

#臨時
tmp_des = "<title>範例 - Google 商店</title><link>https://store.google.com</link><description>此為含有單一項目的基本 RSS 2.0 文件範例</description>"

def Load():

    arr = os.listdir('./posts/')
    return_File = str("")
    try:
        for arr2 in arr:
            print(arr2)
            try:
                f = open(f"./posts/" + arr1, "r", encoding="utf-8").read()
                y = json.loads(f.split("---")[0])
                title1 = y["title"]
                des = y["description"]
                print(title1 + des)
            except:
                title1 = "This Post dont have a title"
                des = "This Post dont have a description"
            Link = "./posts/" + arr2.split(".")[0]
            return_File += "<item><title>" + title1 + "</title><link>" + Link + " </link><description>" + des + "</description></item>"
        #render_template('posts.html', title=title1, description=des, href=)
        return Header + tmp_des + return_File + Footer
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
        return_Content = header_File + nf_File + footer_File
        return return_Content, 500



