
##http 接口上报 任务信息
## POST http://luban.jifeng.online:8000/runninghub/create_task
## body:
##   {
#    "netWssUrl": null,
#    "taskId": "1910246754753896450",
#    "clientId": "e825290b08ca2015b8f62f0bbdb5f5f6",
#    "taskStatus": "QUEUED",
#    "promptTips": "{\"result\": true, \"error\": null, \"outputs_to_execute\": [\"9\"], \"node_errors\": {}}"
#   "taskResult": null,}
import  json
import http.client
import ssl


def ReportTask(api_key, task_id, client_id, task_status, prompt_tips, task_result):
    """上报任务信息"""
    conn = http.client.HTTPConnection("luban.jifeng.online", port=8000)
    payload = json.dumps({
        "netWssUrl": None,
        "taskId": task_id,
        "clientId": client_id,
        "taskStatus": task_status,
        "promptTips": prompt_tips,
        "taskResult": task_result
    })
    headers = {
        'Host': 'luban.jifeng.online',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/runninghub/create_task", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def CreateTask(api_key, workflow_id, node_info_list):

    """创建任务"""
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    conn = http.client.HTTPSConnection("www.runninghub.cn", context=context)

    payload = json.dumps({
        "apiKey": api_key,
        "workflowId": workflow_id,
        "nodeInfoList": node_info_list,
        "webhookUrl": "http://luban.jifeng.online:8000/runninghub/task_end"
    })

    headers = {
        'Host': 'www.runninghub.cn',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/task/openapi/create", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    result = json.loads(data.decode("utf-8"))
    ##{"code":0,"msg":"success","data":{"netWssUrl":"wss://www.runninghub.ai/ws/c_instance?c_host=10.129.240.19&c_port=80&clientId=053462379290dcde1a00d1164197c2f4&workflowId=1921433877150121985&
    # Rh-Comfy-Auth=eyJ1c2VySWQiOiJlMDY4NTc4MWI1ZTgyNDJmYWM0Zjg3OTc3ZDM2YzE1ZCIsInNpZ25FeHBpcmUiOjE3NDc1NTAwMTYxOTIsInRzIjoxNzQ2OTQ1MjE2MTkyLCJzaWduIjoiZDYyMDA2ZjdiMDQ5NGFmNWQwNGQ0YzUzN2I2ZjU1OGYifQ%3D%3D&
    # target=https://hbxy.runninghub.cn:11143","taskId":"1921453618497511425","clientId":"053462379290dcde1a00d1164197c2f4",
    # "taskStatus":"RUNNING","promptTips":"{\"result\": true, \"error\": null, \"outputs_to_execute\": [\"57\", \"54\", \"51\"], \"node_errors\": {}}"}}
    if result["code"] == 0:
        task_id = result["data"]["taskId"]
        client_id = result["data"]["clientId"]
        task_status = result["data"]["taskStatus"]
        prompt_tips = result["data"]["promptTips"]
        task_result = ""
        ReportTask(api_key, task_id, client_id, task_status, prompt_tips, task_result)


def CreateTaskToLuban(api_key, workflow_id, node_info_list, task_name):

    """创建任务"""
    conn = http.client.HTTPConnection("luban.jifeng.online:8000")

    payload = json.dumps({
        "info" : {
            "host": 'www.runninghub.cn',
            "task_name" : task_name
        },
        "apiKey": api_key,
        "workflowId": workflow_id,
        "nodeInfoList": node_info_list
    })

    headers = {
        'Host': 'luban.jifeng.online',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/runninghub/create_task", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    result = json.loads(data.decode("utf-8"))
    if result["code"] != 0:
        print("创建任务失败")
        return


def QueryTask(api_key, taks_id):
    """查询任务状态"""
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    conn = http.client.HTTPSConnection("www.runninghub.cn", context=context)

    payload = json.dumps({
        "apiKey": api_key,
        "taskId": taks_id
    })

    headers = {
        'Host': 'www.runninghub.cn',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/task/openapi/status", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

