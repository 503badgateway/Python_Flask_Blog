from markupsafe import escape
from flask import Flask, jsonify, render_template
import json
import markdown, json
import os
from Feed import Load

directory = './posts'
files = os.listdir(directory)
app = Flask(__name__)

# PreLoad HTML
try:
    header_File = open(f"./templates/header.html", "r", encoding="utf-8").read()
except:
    print("Warning: header file not exists")
    header_File = str(" ")
try:
    footer_File = open(f"./templates/footer.html", "r", encoding="utf-8").read()
except:
    print("Warning: footer file not exists")
    footer_File = str(" ")
try:
    nf_File = open(f"./templates/404.html", "r", encoding="utf-8").read()
except:
    print("Warning: 404 file not exists")
    nf_File = str(" ")

#Loading config.json (not working for now)
try:
    f2 = open(f"./config/config.json", "r", encoding="utf-8").read()
    y2 = json.loads(f2)
    Url = f2["Url"]
    Title = f2["Title"]
    Description = f2["Description"]

except:
    print("Warning: config flie not exists")
    Url = Title = Description = ""



@app.route("/")
def Home_Page():
    arr = os.listdir('./posts/')
    return_File = str("")
    try:
        for arr1 in arr:
            print(arr1)
            try:
                f = open(f"./posts/" + arr1, "r", encoding="utf-8").read()
                y = json.loads(f.split("---")[0])
                try:
                    title1 = y["title"]
                except:
                    title1 = "This Post dont have a title"
                try:
                    des = y["description"]
                except:
                    des = "This Post dont have a description"
                try:
                    tag = ""
                    for tags in y["tags"]:
                        tag += "," + tags
                except:
                    tag = str("None")
                print(title1 + des + tag)
            except:
                title1 = "This Post dont have a title"
                des = "This Post dont have a description"
                tag = str("None")
            Link = "./posts/" + arr1.split(".")[0]
            return_File += render_template('posts.html', tag=tag, title=title1, description=des, href=Link)
        try:
            return header_File + return_File + footer_File
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            return_Content = header_File + nf_File + footer_File
            return return_Content, 500
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
        return_Content = header_File + nf_File + footer_File
        return return_Content, 500


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    try:
        f = open(f"./posts/{post_id}.md", "r", encoding="utf-8").read()
        markdown_content = '\n'.join(f.split("---")[1:]) 
        print(markdown.markdown(markdown_content))
        final_content = header_File + markdown.markdown(markdown_content) + footer_File
        return final_content
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
        return_Content = header_File + nf_File + footer_File
        return return_Content, 500

@app.route("/feed")
def Feed():
    return Load()

@app.route("/links")
def links():
    return_File = ""
    try:
        f1 = open(f"./config/links.json", "r", encoding="utf-8").read()
        y1 = json.loads(f1)
        try:
            for y1 in y1:
                Link_title = y1["Link_title"]
                Link_des = y1["Link_des"]
                Link_url = y1["Link_url"]
                return_File += render_template('links.html', Link_title=Link_title, Link_des=Link_des, Link_url=Link_url)
        except:
            pass
        return header_File + return_File + footer_File
    except Exception as e:
        print(f"An exception occurred: {str(e)}")
        return_Content = header_File + nf_File + footer_File
        return return_Content, 500