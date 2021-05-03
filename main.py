from flask import *
import requests
import json
app=Flask('__name__')
aa=""
@app.route('/',methods=['GET'])
def funci():
    aa=request.args.get('c')
    print(aa)
    if(aa!=""):
        c='http://channelget.herokuapp.com/?c='+aa
        s=requests.get(c).text
        print(s)
        dictt={}
        dictt['live']=s
        print(dictt)
        return render_template("abc.html",ss=s,dic=dictt)
    else:
        c='http://channelget.herokuapp.com/?c='
        s=requests.get(c).text
        print(s)
        return(s)
app.run(port=5000)



