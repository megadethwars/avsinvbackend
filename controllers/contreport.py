from flask import Response,abort,request,jsonify
import json
from run import app
from data.Service import ServiceSQL
from data.dataReport import ReportDB
from status.status import Httpstatus



@app.route('/reports')
def GetReports():

    try:
        
        data = ReportDB.getReport()

        if data == 2:
            return Httpstatus.int_server('server error')
        elif data == 1:
            return Httpstatus.not_found('not found')

        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')



@app.route('/reportcode/<name>')
def GetReport(name):
    try:
        data = ReportDB.getReportsbycode(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error')
    

@app.route('/reportname')
def GetReportbyname():
    try:

        name = request.args.get('producto')
        data = ReportDB.getReportsbyname(name)

        if data == 1:
            return Httpstatus.not_found('not found')


        if data == 2:
            return Httpstatus.int_server('server error')

          
        return data,200, {'ContentType':'application/json'}

    except:
        print("error")
        return Httpstatus.int_server('server error') 


@app.route('/postreport', methods = ['POST'])
def PostReport():

    try:
        print(request.is_json)
        if request.is_json:
            content = request.get_json()
            
            
            status = ReportDB.postReport(content)

            if status == 0:
                return Httpstatus.ok_server_post()
            else:
                return Httpstatus.int_server('server error')
        
        else:
            return Httpstatus.bad_request('bad request')

    except:        
        return Httpstatus.int_server('server error')