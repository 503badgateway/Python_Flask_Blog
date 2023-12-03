from markupsafe import escape
from flask import Flask, jsonify, render_template
import json
import markdown, json
import os
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
                title1 = y["title"]
                des = y["description"]
                print(title1 + des)
            except:
                title1 = "This Post dont have a title"
                des = "This Post dont have a description"
            Link = "./posts/" + arr1.split(".")[0]
            return_File += render_template('posts.html', title=title1, description=des, href=Link)
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
