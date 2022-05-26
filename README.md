# Html2Js
## Convert Html to equivalente javascript ( document.createElement , document.createTextNode , document.setAttribute , document.appendChild ) 


# Usage :  
## Example
		from  Html2Js import  htmljson
  		html  = """<div style="margin-top:-20px; letter-spacing:3px;font-size:45px" class="sfbg">ISSAM</div>"""
	  	print(html2js(html,root = "document.body"))
    
___
    	var itm_139927509068160 = document.createElement("div");
    	itm_139927509068160.setAttribute("style","margin-top:-20px; letter-spacing:3px;font-size:45px");
    	itm_139927509068160.classList.add("sfbg");
    	var itm_139927509052800 = document.createTextNode("ISSAM");
    	itm_139927509068160.appendChild(itm_139927509052800);
		document.body.appendChild(itm_139927509068160);
