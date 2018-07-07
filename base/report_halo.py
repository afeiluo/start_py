#!/usr/bin/env python
# encoding:utf-8

import requests
import json

# TODO 增加未处理工单的监控
# TODO 增加创建工单的监控

adding_checks = [
   {
       "name": "zys5",
       "target": "zyszys",
       "target_type": "graphite",
       "type": "default",
       "interval": 180,
       "warning": 1,
       "critical": 4,
       "symptom": "test test",
       "appid": "558bb97118f4e05891dc5f46"
   },
   {
       "name": "zys6",
       "target": "zyszyszys",
       "target_type": "graphite",
       "type": "mysos",
       "interval": 180,
       "warning": 1,
       "critical": 4,
       "symptom": "test test",
       "appid": "558bb97118f4e05891dc5f46"
   }
]
def add_check_ticket_count(source, _type, rule, adding_checks):
    """
    增加检查剩余未处理的工单的报警
    """
    pass




def add_test():
   url = "http://localhost:9000/api/checks"
   headers = {"X-alert-token": "your_token"}
   res = requests.post(url, headers=headers, data=json.dumps(adding_checks))
   print res


def update_test():
   checker_id = "5ad7013c24aed01ae5934e75"
   url = "http://localhost:9000/api/checks/%s" % checker_id
   headers = {"X-alert-token": "your_token"}
   data = {"critical": 4}
   res = requests.delete(url, headers=headers, data=json.dumps(data))
   print res


def delete_test():
   checker_id = "5ad705e424aed01ae5ed090f"
   url = "http://localhost:9000/api/checks/%s" % checker_id
   headers = {"X-alert-token": "your_token"}
   data = {"critical": 4}
   res = requests.delete(url, headers=headers)
   print res


def main():

   add_test()
   #update_test()
   #delete_test()`