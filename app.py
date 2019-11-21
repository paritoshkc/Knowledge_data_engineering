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
    r = requests.post("http://localhost:3030/KND/query", requestPayload, headers=header)
    return r


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/q')
def homepage():
    requestPayload = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0A%0A%0A%23SELECT+%3Fx+%3Fy+%3Flat+%3Flong+%3Fdist+WHERE+%7B+%3Fx+co%3AparkName+%22Cappagh+Park%22.%0A%23%3Fx+so_geo%3A+%3Fy.%0A%23++%3Fy+lat%3A+%3Flat.%0A%23++%3Fy+long%3A+%3Flong+.%0A%23++BIND((%3Flat)-(%3Fact_lat)+AS+%3Fdist)%0A%23++%7B%0A%23++++SELECT+%3Fact_x+%3Fact_y+%3Fact_lat+%3Fact_long+WHERE+%7B%0A%23+%3Fact_x+so_geo%3A+%3Fact_y.%0A%23++%3Fact_x+lat%3A+%3Fact_lat.%0A%23+%3Fact_x+long%3A+%3Fact_long+.%0A%23++FILTER+regex(str(%3Fact_x)+%2C+'activitiy').%0A%23%7D%0A%23++%7D%0A%23++%0A%23++%7D%0A%23+++++SELECT+%3Fact_x+%3Fact_y+%3Fact_lat+%3Fact_long+WHERE+%7B%0A%23+%3Fact_x+so_geo%3A+%3Fact_y.%0A%23++%3Fact_x+lat%3A+%3Fact_lat.%0A%23+%3Fact_x+long%3A+%3Fact_long+.%0A%23++FILTER+regex(str(%3Fact_x)+%2C+'activitiy').%0A%23%7D%0A%23++BIND((%3Flocation1-+%3Flocation2)+as+%3Fdist)%0A%23SELECT+%3Fx+%3Fy+%3Fact_lat+%3Fact_long+WHERE+%7B%0A%23+%3Fx+so_geo%3A+%3Fy.%0A%23++%3Fy+lat%3A+%3Fact_lat.%0A%23+%3Fy+long%3A+%3Fact_long+.%0A%23++FILTER+regex(str(%3Fx)+%2C+'activitiy').%0A%23%7D%0A%0A%23%0A%23+%0A%23SELECT+%3Fpitch_obj+%3Fpitch_loc+%3Fact_long+%3Fact_lat+%7B+%3Fpitch_obj+so_geo%3A+%3Fpitch_loc.%0A%23+%3Fpitch_loc+lat%3A+%3Fact_lat+.%0A%23%3Fpitch_loc+long%3A+%3Fact_long+.%0A%23++FILTER+regex(str(%3Fpitch_obj)+%2C+'activitiy').%0A%23%7D%0A%23%0A%23SELECT+%3FPITCH_OBJ+%3Fpitch_lat+%3Fpitch_long+%3Fact_obj+%3Fact_loc+%3Fact_long+%3Fact_lat+%3Fdist+WHERE+%7B+%3FPITCH_OBJ+co%3AparkName+%22Cappagh+Park%22.%0A%23++%3FPITCH_OBJ+so_geo%3A+%3Fpitch_loc+.%0A%23++%3Fpitch_loc+lat%3A+%3Fpitch_lat+.%0A%23++%3Fpitch_loc+long%3A+%3Fpitch_long+.%0A%23%23++BIND((%3Fpitch_long-+%3Fact_long)+as+%3Fdist)%0A%23++%7B%0A%23+SELECT+%3Fact_obj+%3Fact_loc+%3Fact_long+%3Fact_lat+%7B+%3Fact_obj+so_geo%3A+%3Fpitch_loc.%0A%23+%3Fact_loc+lat%3A+%3Fact_lat+.%0A%23%3Fact_loc+long%3A+%3Fact_long+.%0A%23++FILTER+regex(str(%3Fact_obj)+%2C+'activitiy').%0A%23%7D%0A%23++%7D%0A%23%7D%0A%0A%23+SELECT+%3Fact_obj+%3Fact_loc+%3Fact_long+%3Fact_lat+%7B+%3Fact_obj+so_geo%3A+%3Fpitch_loc.%0A%23+%3Fact_loc+lat%3A+%3Fact_lat+.%0A%23%3Fact_loc+long%3A+%3Fact_long+.%0A%23++FILTER+regex(str(%3Fact_obj)+%2C+'activitiy').%0A%23%7DLIMIT+1%0A%0A%23SELECT+%3Fname+%3FPARK_obj%0A%23%23FROM+http%3A%2F%2Fschema.org%2FPark%0A%23WHERE%7B%0A%23%3FPARK_obj+address%3A+%3Fpg_location+.%0A%23%3FPARK_obj+name%3A+%3Fname+.%0A%23FILTER+regex(str(%3FPARK_obj)+%2C+'park')%0A%23%0A%23%7B%0A%23SELECT+%3Fpg_location+%3Fpg_obj+where+%7B%0A%23%3Fpg_obj+name%3A%22South+Park+Playground%22+.%0A%23%3Fpg_obj+address%3A+%3Fpg_location+.%0A%23%0A%23%7D%0A%23%7D%0A%23%0A%23%7D%0A%0A%0ASELECT+%3Fname+%3FPARK_obj+WHERE%7B%0A%3FPARK_obj+address%3A+%3Fpg_location+.%0A%3FPARK_obj+name%3A+%3Fname+.%0AFILTER+regex(str(%3FPARK_obj)+%2C+'playground')%0A%7Dorder+by+asc(UCASE(str(%3Fname)))%0A%0A%0A"

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
        return render_template("1st query.html", summary=pgname)
    else:
        return str(r.status_code)


@app.route('/q1', methods=['POST'])
def q1():
    params = {
        'api_key': '{API_KEY}',
    }
    name = request.form["query1"]
    print(name, "this is the name---<")

    Body_query1 = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0A%0A%0ASELECT+%3Fname+%3FPARK_obj%0AWHERE%7B%0A%3FPARK_obj+address%3A+%3Fpg_location+.%0A%3FPARK_obj+name%3A+%3Fname+.%0AFILTER+regex(str(%3FPARK_obj)+%2C+'park')%0A%0A%7B%0ASELECT+%3Fpg_location+%3Fpg_obj+where+%7B%0A%3Fpg_obj+name%3A%22^^%22+.%0A%3Fpg_obj+address%3A+%3Fpg_location+.%0A%0A%7D%0A%7D%0A%0A%7D"
    requestPayload = Body_query1.replace("^^", name.replace(" ", "+"))
    pgname = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = requests.post("http://localhost:3030/KND/query", requestPayload, headers=header)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['name']['value'])
            print(dict_b['name']['value'])

        print(pgname)
        return render_template("result.html", summary=pgname)

    else:
        return str(r.status_code)


@app.route('/q2', methods=['POST'])
def q2():
    name = request.form["query2"]
    print(name, "this is the name---<")

    Body_query2 = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0A%0ASELECT+%3Ffacilities+WHERE%7B%0A%3FPARK+address%3A+%3Fpg_loc+.%0A%3FPARK+co%3Afacilities+%3Ffacilities%0A%7B%0ASELECT+%3Fpg_loc+where+%7B%3Fpg_obj+name%3A+%22^^%22+.%0A%3Fpg_obj+address%3A+%3Fpg_loc+.%0A%7D%0A%7D%0A%7D"
    requestPayload = Body_query2.replace("^^", name.replace(" ", "+"))
    pgname = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = requests.post("http://localhost:3030/KND/query", requestPayload, headers=header)
    if (r.status_code == 200):

        a = r.text
        dict_a = ast.literal_eval(a)
        print(dict_a['results'])
        dict_a = dict_a['results']['bindings']
        for i in range(len(dict_a)):
            dict_b = dict_a[i]
            pgname.append(dict_b['facilities']['value'])
            print(dict_b['facilities']['value'])

        if len(pgname) > 0:
            summary = pgname[0].split(',')
            print(pgname[0].split(','))
        else:
            summary = pgname
        return render_template("result.html", summary=summary)

    else:
        return str(r.status_code)


@app.route('/q3', methods=['POST'])
def q3():
    name = request.form["query3"]
    print(name, "this is the name---<")
    body_cityCentre = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0A%0ASELECT+DISTINCT+%3Fname+WHERE%7B%0A%3FPG+address%3A+%3Fy+.%0A%3FPG+name%3A+%3Fname%0AFILTER+regex(str(%3FPG)+%2C+'playground')%0A%7B%0ASELECT+%3Fy+where+%7B%3FX+co%3AareaOfCity+%22City+Centre%22+.%0A%3FX+address%3A+%3Fy+.%0A%7D%0A%7D%0A%7D"
    body_cityEast = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0A%0ASELECT+DISTINCT+%3Fname+WHERE%7B%0A%3FPG+address%3A+%3Fy+.%0A%3FPG+name%3A+%3Fname%0AFILTER+regex(str(%3FPG)+%2C+'playground')%0A%7B%0ASELECT+distinct+%3FX+%3Fy+where+%7B%7B%3FX+co%3AareaOfCity+%22City+-East%22%7D+UNION%7B+SELECT+distinct+%3FX+where+%7B%3FX+co%3AareaOfCity+%22City-East%22%7D%7D%0A%3FX+address%3A+%3Fy+.%0A%7D%0A%7D%0A%7D%0A%0A"

    if name == "City-Centre":
        requestPayload = body_cityCentre
    else:
        requestPayload = body_cityEast
    pgname = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = requests.post("http://localhost:3030/KND/query", requestPayload, headers=header)
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
        return render_template("result.html", summary=summary)

    else:
        return str(r.status_code)


@app.route('/q4', methods=['POST'])
def q4():
    body = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0ASELECT+Distinct+%3FLocation+%3Fname+%3Fparkname+WHERE%7B%0A%3FPG+address%3A+%3FLocation+.%0A%3FPG+name%3A+%3Fname+.%0A%3FPARK_obj+name%3A+%3Fparkname+.%0AFILTER+regex(str(%3FPG)+%2C+'layground')%0A%0A%7BSELECT+Distinct+%3FPARK_obj+%3FLocation+where+%7B%3FPARK_obj+address%3A+%3FLocation.%0AFILTER+regex(str(%3FPARK_obj)+%2C+'park')%0A%0A%7D%0A%7D%0A%7D"
    requestPayload = body
    pgname = []
    parkname = []
    location = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = requests.post("http://localhost:3030/KND/query", requestPayload, headers=header)
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
        return render_template("result_park_pg_loc.html.html", test=zip(summary, parkname, location))

    else:
        return str(r.status_code)


@app.route('/q5', methods=['POST'])
def q5():
    body = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0APREFIX+co%3A+%3Chttps%3A%2F%2Fraw.githubusercontent.com%2Ftannineo%2Fcs7is1-knd-project%2Fmaster%2Fchao_ontology.xml%23%3E%0APREFIX+so%3A+%3Chttp%3A%2F%2Fschema.org%2Fversion%2Flatest%2Fschema.rdf%3E%0APREFIX+name%3A+%3Chttp%3A%2F%2Fschema.org%2Fname%3E%0APREFIX+address%3A+%3Chttp%3A%2F%2Fschema.org%2Faddress%3E%0APREFIX+park%3A+%3Chttp%3A%2F%2Fschema.org%2FPark%3E%0APREFIX+oh%3A+%3Chttp%3A%2F%2Fschema.org%2FopeningHours%3E%0APREFIX+contains%3A+%3Chttp%3A%2F%2Fschema.org%2FcontainsPlace%3E%0APREFIX+lat%3A+%3Chttp%3A%2F%2Fschema.org%2Flatitude%3E%0APREFIX+long%3A+%3Chttp%3A%2F%2Fschema.org%2Flongitude%3E%0APREFIX+geo%3A+%3Chttps%3A%2F%2Fschema.org%2FGeoCoordinates%3E%0APREFIX+so_geo%3A+%3Chttp%3A%2F%2Fschema.org%2Fgeo%3E%0APREFIX+fl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23float%3E%0A%0A%0ASelect+distinct+%3FPark_name+%3FPark_location+where+%7B%3FPark_object+address%3A+%3FPg_location.%0A%3FPark_object+name%3A+%3FPark_name.%0A%3FPark_object+address%3A+%3FPark_location.%0AFILTER+regex(str(%3FPark_object)+%2C+'park').%0A%0A%7BSelect+%3FX+%3FPg_location+%3FPg_name+where+%7B%0A++++++%3FX+contains%3A+%3Chttp%3A%2F%2Fwww.example.org%2FparkingFacility%2FWithin%2520estate%3E.%0A%3FX+address%3A+%3FPg_location+.%7D%0A%7D%7D"
    requestPayload = body
    parkname = []
    Park_location = []
    header = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    r = requests.post("http://localhost:3030/KND/query", requestPayload, headers=header)
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

        return render_template("result_park_pg.html", test=zip( parkname, Park_location))

    else:
        print("ERRRRRRRRRRRRRRRRRRROOORR")
        return str(r.status_code)

