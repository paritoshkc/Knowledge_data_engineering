from flask import Flask, render_template, request
import requests
import ast
import json

app = Flask(__name__)
params = {
    'api_key': '{API_KEY}',
}


def querying_func(requestPayload):
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = requests.post("http://localhost:3030/final/query", requestPayload, headers=header)
    return r


@app.route('/')
def hello_world():
    return render_template("MainPage.html")


if __name__ == '__main__':
    app.run()

######################################################### 1st query #################################3

@app.route('/query1',methods=['POST'])
def query1():
    requestPayload ="query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0A%0Aselect+%3Fname+where%7B%0A++%3Fparkobj+schema%3Aname+%3Fname.%0A++filter+regex(str(%3Fparkobj)%2C%22playground%22)%0A%7D+orderby(%3Fname)%0A%0A%0A"

    r = querying_func(requestPayload)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        pgname = []
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['name']['value'])
            print(dict_b['name']['value'])
        print(pgname)
        return render_template("Query1.html", summary=pgname)
    else:
        return str(r.status_code)

@app.route('/q1', methods=['POST'])
def q1():
    params = {
        'api_key': '{API_KEY}',
    }
    name = request.form["query1"]
    print(name, "this is the name---<")

    Body_query1 = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0A%0ASELECT+DISTINCT+%3Fname%0AWHERE%7B%0A%3FPARK_obj+schema%3Aaddress+%3Fpg_location+.%0A%3FPARK_obj+schema%3Aname+%3Fname+.%0AFILTER+regex(str(%3FPARK_obj)+%2C+'park')%0A%7B%0ASELECT+%3Fpg_location+%3Fpg_obj+where+%7B%0A%3Fpg_obj+schema%3Aname+%22^^%22+.%0A%3Fpg_obj+schema%3Aaddress+%3Fpg_location+.%0A%7D%7D%7D%0A%0A"
    requestPayload = Body_query1.replace("^^", name.replace(" ", "+"))
    pgname = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = querying_func(requestPayload)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['name']['value'])
            print(dict_b['name']['value'])
            msg="The parks near selected playground are"

        if len(dict_a)==0:
            msg="no parks available on the database "

        print(pgname)
        return render_template("query_Result.html", summary=pgname,msg=msg)

    else:
        return str(r.status_code)

######################################################### 1st query  ENDS HERE ###################################

@app.route('/query2',methods=['POST'])
def query2():
    requestPayload = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0A%0Aselect+%3Fname+where%7B%0A++%3Fparkobj+schema%3Aname+%3Fname.%0A++filter+regex(str(%3Fparkobj)%2C%22playground%22)%0A%7D+orderby(%3Fname)%0A%0A%0A"

    r = querying_func(requestPayload)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        pgname = []
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(30):
            dict_b = dict_a[i]
            pgname.append(dict_b['name']['value'])
            print(dict_b['name']['value'])
        print(pgname)
        return render_template("Query2.html", summary=pgname)
    else:
        return str(r.status_code)

@app.route('/q2', methods=['POST'])
def q2():
    name = request.form["query2"]
    print(name, "this is the name---<")

    Body_query2 = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0A%0ASELECT+%3Ffacilities+WHERE%7B%0A%3FPARK+schema%3Aaddress+%3Fy+.%0A%3FPARK+%3Afacilities+%3Ffacilities%0A%7B%0ASELECT+%3Fy+where+%7B%3FX+schema%3Aname+%22^^%22+.%0A%3FX+schema%3Aaddress+%3Fy+.%0A%7D%0A%7D%0A%7D%0A%0A"
    requestPayload = Body_query2.replace("^^", name.replace(" ", "+"))
    pgname = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = querying_func(requestPayload)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        dict_a = dict_a['results']['bindings']
        msg="Listed Facilities are"
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['facilities']['value'])
            print(dict_b['facilities']['value'])

        if len(pgname) > 0:
            summary = pgname[0].split(',')
            print(pgname[0].split(','))
        else:
            summary = pgname
            msg = "No Facilities listed"
        return render_template("query_Result.html", summary=summary,msg=msg)
    else:
        return str(r.status_code)
###################################### query2 Ends Here ########################

@app.route('/query3', methods=['POST'])
def query4():
    return render_template("Query3.html")

@app.route('/q3', methods=['POST'])
def q3():
    name = request.form["query3"]
    print(name, "this is the name---<")
    body_cityCentre = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0A%0A%23SELECT+DISTINCT+%3Fname+WHERE%7B%0A%23%3FPG+schema%3Aaddress+%3Fy+.%0A%23%3FPG+schema%3Aname+%3Fname%0A%23FILTER+regex(str(%3FPG)+%2C+'playground')%0A%23%7B%0ASELECT+%3Fname+where+%7B%0A++%3FX+%3AareaOfCity+%22City+Centre%22+.%0A%3FX+schema%3Aaddress+%3Fname+.%0A++%7D%0A%23select+%3Fx+%3Fy+where+%7B%3Fx+%3AareaOfCity+%22City-West%22%7D%0A%0A"
    body_cityEast = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0A%0A%23SELECT+DISTINCT+%3Fname+WHERE%7B%0A%23%3FPG+schema%3Aaddress+%3Fy+.%0A%23%3FPG+schema%3Aname+%3Fname%0A%23FILTER+regex(str(%3FPG)+%2C+'playground')%0A%23%7B%0ASELECT+Distinct+%3Fname+where+%7B%0A++%7B%3FX+%3AareaOfCity+%22City-East%22+.%0A%3FX+schema%3Aaddress+%3Fname+.%0A++%7D+UNION+%7BSELECT+%3Fname+where+%7B%0A++%7B%3FX+%3AareaOfCity+%22City+-East%22+.%0A%3FX+schema%3Aaddress+%3Fname+.%0A++++++%7D%0A++++%7D%0A++%7D%0A%7D%0A%23select+%3Fx+%3Fy+where+%7B%3Fx+%3AareaOfCity+%22City-West%22%7D%0A%0A"
    body_cityWest = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0A%0A%23SELECT+DISTINCT+%3Fname+WHERE%7B%0A%23%3FPG+schema%3Aaddress+%3Fy+.%0A%23%3FPG+schema%3Aname+%3Fname%0A%23FILTER+regex(str(%3FPG)+%2C+'playground')%0A%23%7B%0ASELECT+Distinct+%3Fname+where+%7B%0A++%7B%3FX+%3AareaOfCity+%22City-West%22+.%0A%3FX+schema%3Aaddress+%3Fname+.%0A++%7D+UNION+%7BSELECT+%3Fname+where+%7B%0A++%7B%3FX+%3AareaOfCity+%22City+-West%22+.%0A%3FX+schema%3Aaddress+%3Fname+.%0A++++++%7D%0A++++%7D%0A++%7D%0A%7D%0A%23select+%3Fx+%3Fy+where+%7B%3Fx+%3AareaOfCity+%22City-West%22%7D%0A%0A"
    if name == "City Centre":
        requestPayload = body_cityCentre
    elif name=="City East":
        requestPayload = body_cityEast
    else:
        requestPayload=body_cityWest

    pgname = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = querying_func(requestPayload)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        dict_a = dict_a['results']['bindings']
        print("length", len(dict_a))
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['name']['value'])
            print(dict_b['name']['value'])
        summary = pgname
        if len(pgname)==0:
            msg="No parks available in around City West, Please try another location"
        else:
            msg="Parks around the area are "
        return render_template("query_Result.html", summary=summary,msg=msg)
    else:
        return str(r.status_code)


@app.route('/q4', methods=['POST'])
def q4():
    body = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0A%0A%23SELECT+DISTINCT+%3Fname+WHERE%7B%0A%23%3FPG+schema%3Aaddress+%3Fy+.%0A%23%3FPG+schema%3Aname+%3Fname%0A%23FILTER+regex(str(%3FPG)+%2C+'playground')%0A%23%7B%0ASELECT+Distinct+%3FLocation+%3Fname+%3Fparkname+WHERE%7B%0A%3FPG+schema%3Aaddress+%3FLocation+.%0A%3FPG+schema%3Aname+%3Fname+.%0A%3FPARK_obj+schema%3Aname+%3Fparkname+.%0AFILTER+regex(str(%3FPG)+%2C+'layground')%0A%0A%7BSELECT+Distinct+%3FPARK_obj+%3FLocation+where+%7B%3FPARK_obj+schema%3Aaddress+%3FLocation.%0AFILTER+regex(str(%3FPARK_obj)+%2C+'park')%0A%0A%7D%0A%7D%0A%7D%0A%23select+%3Fx+%3Fy+where+%7B%3Fx+%3AareaOfCity+%22City-West%22%7D%0A%0A"
    requestPayload = body
    pgname = []
    parkname = []
    location = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = querying_func(requestPayload)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        dict_a = dict_a['results']['bindings']
        print("length", len(dict_a))
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['name']['value'])
            print(dict_b['name']['value'])
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            location.append(dict_b['Location']['value'])
            print(dict_b['Location']['value'])
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            parkname.append(dict_b['parkname']['value'])
            print(dict_b['parkname']['value'])
        summary = pgname
        return render_template("result_park_pg_loc.html", test=zip(summary, parkname, location), msg="Locations which contain Parks and Playground")

    else:
        return str(r.status_code)


@app.route('/q5', methods=['POST'])
def q5():
    body = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0A%0ASelect+distinct+%3FPark_name+%3FPark_location+where+%7B%3FPark_object+address%3A+%3FPg_location.%0A%3FPark_object+schema%3Aname+%3FPark_name.%0A%3FPark_object+schema%3Aaddress+%3FPark_location.%0AFILTER+regex(str(%3FPark_object)+%2C+'park').%0A%0A%7BSelect+%3FX+%3FPg_location+%3FPg_name+where+%7B%3FX+schema%3AcontainsPlace+%3Chttp%3A%2F%2Fwww.example.org%2Fparking%2FWithin%2520estate%3E+.%0A%3FX+schema%3Aaddress+%3FPg_location+.%7D%0A%7D%7D"
    requestPayload = body
    parkname = []
    Park_location = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = querying_func(requestPayload)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        dict_a = dict_a['results']['bindings']
        print("length", len(dict_a))
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            Park_location.append(dict_b['Park_location']['value'])
            print(dict_b['Park_location']['value'])
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            parkname.append(dict_b['Park_name']['value'])
            print(dict_b['Park_name']['value'])

        return render_template("result_2_column.html", test=zip(parkname, Park_location), heading1="Park Name", heading2="Park Location")

    else:
        return str(r.status_code)


@app.route('/q6', methods=['POST'])
def q6():

    body = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0A%0Aselect+distinct+%3Floc+where+%7B%0A++%3Fobj+schema%3Aaddress+%3Floc.%0A++Filter+regex(str(%3Fobj)%2C'park')%0A%7Dorderby(%3Floc)"

    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        pgname = []
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['loc']['value'])
            print(dict_b['loc']['value'])
        print(pgname)
        return render_template("Query6.html", summary=pgname)


@app.route('/query6', methods=['POST'])
def query6():

    body ="query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0A%0Aselect+distinct+%3FPark_name+%3Fc+%3FPitch_type+%7B%0A%0A%3FPitch_obj+%3AparkName+%3FPark_name.%0A%3FPitch_obj+%3ApitchType+%3FPitch_type.%0A%7B%0Aselect+%3FPark_name%0Awhere%7B%0A%3FPark_obj+schema%3Aaddress+'^^'.%0A%3FPark_obj+schema%3Aname+%3FPark_name.%0A%0A%7D%0A++++%0A++%7D%0A%7D"
    name = request.form["query6"]
    print(name)
    name=name.replace(",","%2C").replace(" ", "+")
    print(name)
    body = body.replace("^^", name)
    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        park_name = []
        pitch_type=[]
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            park_name.append(dict_b['Park_name']['value'])
            pitch_type.append(dict_b['Pitch_type']['value'])
            print(dict_b['Park_name']['value'])
        print(park_name)
        if len(dict_a)==0:
            msg="Sorry! there is no pitch as per the records "
            heading1 = ""
            heading2 = ""

        else:
            msg="Checkout the pitches!!"
            heading1 = "Pitch Name"
            heading2 = "Park Name"

        return render_template("result_2_column.html", test=zip(pitch_type, park_name), heading1=heading1, heading2=heading2,msg=msg)

########################################################## Query 6 Ends Here##########################################
@app.route('/q7', methods=['POST'])
def q7():

    body = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0A%0Aselect+distinct+%3Fpark_name+where%7B+%3Fx+schema%3Aname+%3Fpark_name.%0Afilter+regex(str(%3Fx)%2C%22park%2F%22)%0A%7D+orderby(%3Fpark_name)"

    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        pgname = []
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['park_name']['value'])
            print(dict_b['park_name']['value'])
        print(pgname)
        return render_template("Query7.html", summary=pgname)

@app.route('/query7', methods=['POST'])
def query7():

    body="query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0A%0ASelect+%3Fparking+%3Fparkname+where+%7B%0A%3Fplayground_obj+schema%3Aaddress+%3Flocation.%0A%3Fplayground_obj+schema%3AcontainsPlace+%3Fparking.%0A%7B%0ASELECT+%3Flocation+%3Fparkname+where%7B%3Fpark_obj+schema%3Aaddress+%3Flocation.%0A%3Fpark_obj+schema%3Aname+%3Fparkname.%0AFILTER+contains(%3Flocation%2C%22^^%22)%0AFILTER+regex(str(%3Fpark_obj)%2C+'park')%0A%7D%0A%7D%0A%7D"
    name = request.form["query7"]
    print(name)
    nm_sep=name.split(" ")
    print(nm_sep[0])
    body = body.replace("^^", nm_sep[0])
    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        park_name = []
        pitch_type=[]
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            park_name.append(dict_b['parking']['value'])
            park_name[i]=park_name[i].replace("http://www.example.org/parking/","").replace("%20"," ")
            print(dict_b['parking']['value'])
        print()
        if len(dict_a)==0:
            msg="No parking information available  "
        else:
            msg="Parking type available "

        return render_template("query_Result.html",summary=park_name,msg=msg)
################################################### query 7 ends here #####################################################


@app.route('/q8',methods=['POST'])
def q8():
    body = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0A%0Aselect+distinct+%3Fparkname+where+%7B+%3Fobj+schema%3Aname+%3Fparkname+.%0A++filter+regex(str(%3Fobj)%2C%22park%2F%22)%0A%7Dorderby+(%3Fparkname)"

    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        pgname = []
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['parkname']['value'])
            print(dict_b['parkname']['value'])
        print(pgname)
        return render_template("Query8.html", summary=pgname)

@app.route('/query8', methods=['POST'])
def query8():

    body="query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0A%0ASELECT+%3Fname+%3Ftoilet_availability%0AWHERE%7B%0A%3FPARK_obj+schema%3Aaddress+%3Fpg_location+.%0A%3FPARK_obj+schema%3Aname+%3Fname+.%0A%3FPARK_obj+%3Atoilet+%3Ftoilet_availability.%0A%7B%0ASELECT+%3Fpg_location+%3Fpg_obj+where+%7B%0A%3Fpg_obj+schema%3Aname+%3Fname+.%0A%3Fpg_obj+schema%3Aaddress+%3Fpg_location+.%0AFILTER+contains(%3Fname%2C%22^^%22)%0A%0A%7D%7D%7D"

    name = request.form["query8"]
    print(name)
    nm_sep=name.split(" ")
    print(nm_sep[0])
    body = body.replace("^^", nm_sep[0])
    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        park_name = []
        toilet=[]
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            park_name.append(dict_b['name']['value'])
            toilet.append(dict_b['toilet_availability']['value'])
            print(dict_b['name']['value'])
        print()
        if len(dict_a)==0:
            msg="No information available  "
            heading1=""
            heading2 = ""
        else:
            msg="As per our records"
            heading1 = "Location"
            heading2 = "Availability of toilet"

        return render_template("result_2_column.html",test=zip(park_name, toilet), heading1=heading1, heading2=heading2,msg=msg)


@app.route('/query9', methods=['POST'])
def query9():

    body="query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0APREFIX+co%3A+%3Chttp%3A%2F%2Fpurl.org%2Fontology%2Fco%2Fcore%23%3E%0A%0A%0ASelect+distinct+%3Fpg_name++where+%7B%0A++%3Fpark_object+schema%3Aaddress+%3Flocation.%0A++%3Fpark_object+schema%3Aname+%3Fpark_name.%0A++%3Fpark_object+%3Adescription+%3Flocal_neighbourhood_park%0A++FILTER+regex(str(%3Fpark_object)+%2C+'park')+%0A++FILTER+contains(str(%3Flocal_neighbourhood_park)+%2C'Local')%0A%7B+%0ASelect+distinct+%3Fpg_name+%3Flocation+where+%7B%3Fobject+schema%3Aaddress+%3Flocation.%0A++++++%3Fobject+schema%3Aname+%3Fpg_name+.%0A++++FILTER+regex(str(%3Fobject)+%2C+'playground')%0A++++%7D%0A++%7D%0A%7Dorderby(%3Fpg_name)"

    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        park_name = []
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            park_name.append(dict_b['pg_name']['value'])
            print(dict_b['pg_name']['value'])
        print()
        if len(dict_a)==0:
            msg="No information available  "
        else:
            msg="As per our records. Playground names are :"

        return render_template("query_Result.html", summary=park_name,msg=msg)


@app.route('/q10', methods=['POST'])
def q10():
    body = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0A%0Aselect+distinct+%3Fparkname+where+%7B+%3Fobj+schema%3Aname+%3Fparkname+.%0A++filter+regex(str(%3Fobj)%2C%22park%2F%22)%0A%7Dorderby+(%3Fparkname)"

    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        pgname = []
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['parkname']['value'])
            print(dict_b['parkname']['value'])
        print(pgname)
        return render_template("Query10.html", summary=pgname)


@app.route('/query10', methods=['POST'])
def query10():

    body ="query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0APREFIX+co%3A+%3Chttp%3A%2F%2Fpurl.org%2Fontology%2Fco%2Fcore%23%3E%0A%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinate%3E%0APREFIX+prefix%3A+%3Chttp%3A%2F%2Fprefix.cc%2F%3E%0APREFIX+geo_cord%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0A%0ASELECT+%3Fname+%3Fsurface%0AWHERE%7B%0A%3FPARK_obj+address%3A+%3Fpg_location+.%0A%3FPARK_obj+name%3A+%3Fname+.%0A%3FPARK_obj+%3Asurface+%3Fsurface.%0A%7B%0ASELECT+%3Fpg_location+%3Fpg_obj+where+%7B%0A%3Fpg_obj+name%3A+%3Fname+.%0A%3Fpg_obj+address%3A+%3Fpg_location+.%0AFILTER+contains(%3Fname%2C%22^^%22)%0A%0A%7D%7D%7D"
    name = request.form["query8"]
    print(name)
    nm_sep = name.split(" ")
    print(nm_sep[0])
    body = body.replace("^^", nm_sep[0])
    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        park_name = []
        surface = []
        a = r.text
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            park_name.append(dict_b['name']['value'])
            surface.append(dict_b['surface']['value'])
            print(dict_b['name']['value'])
        print()
        if len(dict_a) == 0:
            msg = "No information available  "
            heading1 = ""
            heading2 = ""
        else:
            msg = "As per our records"
            heading1 = "Location"
            heading2 = "Type of surface"

        return render_template("result_2_column.html", test=zip(park_name, surface), heading1=heading1,
                               heading2=heading2, msg=msg)

@app.route('/q11', methods=['POST'])
def q11():
    body ="query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.ttl%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0APREFIX+schema%3A+%3Chttp%3A%2F%2Fschema.org%2F%3E%0APREFIX+sc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fscience%2Fowl%2Fsciencecommons%2F%3E%0APREFIX+http%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2011%2Fhttp%23%3E%0APREFIX+co%3A+%3Chttp%3A%2F%2Fpurl.org%2Fontology%2Fco%2Fcore%23%3E%0A%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinate%3E%0APREFIX+prefix%3A+%3Chttp%3A%2F%2Fprefix.cc%2F%3E%0APREFIX+geo_cord%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0A%0A%23got+the+lower+and+upper+limits%0Aselect+%3Fname+%3Fphone+%3Fdist+where%7B%3Fgeo+schema%3Alatitude+%3Ff_lat+.+%3Fgeo+schema%3Alongitude+%3Ff_long+.%3Fobj+schema%3Ageo+%3Fgeo.+%3Fobj+schema%3Aname+%3Fname+.+%0A++%3Fobj+schema%3Atelephone+%3Fphone+%7Bselect+%3Floc+%3Flat_higher++%3Flong_lower+%3Flong_higher+%3Flat_lower+where+%7B%3Fsub+schema%3Ageo+%3Floc.+%3Floc+schema%3Alatitude+%3Flat.+%3Floc+schema%3Alongitude+%3Flong%7Bselect+%3Fsub+where+%7B%7B%3Fsub+%3ApitchType+%22All+Weather+Pitch%22.%7D+union+%7B+select+%3Fsub+where%7B%3Fsub+%3ApitchType+%22All+weather+pitch%22.%7D%7D%7D%7DBIND((%3Flat-0.001)+AS+%3Flat_lower)BIND((%3Flat%2B0.001)+AS+%3Flat_higher)BIND((%3Flong-0.2)+AS+%3Flong_lower)BIND((%3Flong%2B0.2)+AS+%3Flong_higher)%7D%7D++FILTER(%3Ff_long+%3C%3D+%3Flong_higher+%26%26+%3Ff_long+%3E+%3Flong_lower)++FILTER(%3Ff_lat+%3C%3D+%3Flat_higher+%26%26+%3Ff_lat+%3E+%3Flat_lower)FILTER+contains(str(%3Fobj)%2C'bar')%0A++bind(%3Flat_lower-%3Ff_lat+as+%3Fdist)%7Dorderby(%3Fdist)%0A%0A"

    r = querying_func(body)
    if (r.status_code == 200):

        a = r.text

        pub_name = []
        phone_num=[]
        dict_a = ast.literal_eval(a)
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pub_name.append(dict_b['name']['value'])
            phone_num.append(dict_b['phone']['value'])
            print(dict_b['name']['value'])
            print(phone_num)
        print(pub_name)
        if len(pub_name)==0:
            msg =" Sorry, No pubs and bars near you ! "
            heading1=''
            heading2=''
        else:
            msg="Pub and Bars nearest to you are"
            heading1='Pub/Bar Name'
            heading2='Phone number'
        return render_template("result_2_column.html",test=zip(pub_name, phone_num), heading1=heading1, heading2=heading2,msg=msg)



