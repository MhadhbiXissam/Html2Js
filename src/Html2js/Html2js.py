from bs4 import *
import json


def htmljson(s,parent = "root") : 
	js = {"type" : s.__class__.__name__ , "childs" : [] , "parent" : parent }
	js["id"] = id(js)
	if s.__class__.__name__ == "NavigableString" : 
		js["text"] = s.__str__()
	elif s.__class__.__name__ == "Tag" : 
		js["tagName"] = s.name
		js["attrs"] = dict(s.attrs)
		if len(list(s.children )) > 0  : 
			js["childs"] = list()
			for i in s.children : 
				js["childs"].append(htmljson(i,parent = js["id"]) )
	return js 

def to_js(json_html) : 
	code = ""
	if json_html["type"] == "NavigableString" :
		json_html["text"] = json.dumps(json_html["text"].replace('\n','').replace('\t',''))
		code += "var itm_{id} = document.createTextNode({text});itm_{parent}.appendChild(itm_{id});\n".format(**json_html)

	if json_html["type"] == "Tag" : 
		code += "var itm_{id} = document.createElement(\"{tagName}\");".format(**json_html)
		if len(json_html["attrs"]) > 0  : 
			for attrkey in json_html["attrs"] : 
				if attrkey == "class" : 
					code += "itm_{0}.classList.add({1});".format(json_html["id"] , json.dumps([clsname.strip() for clsname in json_html['attrs']['class'] ]).strip()[1:-1])
				else : 
					code += "itm_{0}.setAttribute(\"{1}\",{2});".format(json_html["id"] ,attrkey , json.dumps(json_html["attrs"][attrkey])  )
		if len(json_html["childs"]) > 0 : 
			for child in json_html["childs"] :
				code += to_js(child)
		if json_html["parent"] != "root" : 
			code += "itm_{parent}.appendChild(itm_{id});\n".format(**json_html)

	return code 


def html2js(html_string,root = "root") : 
	jsonhtml = htmljson(BeautifulSoup("""<root>{0}</root>""".format(html_string), features="lxml").find('root'))
	rootid = jsonhtml["id"]
	code = to_js(jsonhtml)
	code = code.replace(f'var itm_{rootid} = document.createElement("root");',"")
	code = code.replace(f"itm_{rootid}",root)
	return code 


if __name__ == '__main__':
	html  = """<div style="margin-top:-20px; letter-spacing:3px;font-size:45px" class="sfbg">ISSAM</div>"""
	print(html2js(html,root = "document.body"))


