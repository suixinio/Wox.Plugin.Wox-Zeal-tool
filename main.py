# -*- coding: utf-8 -*-

from wox import Wox
import os,re
from urllib.parse import quote

class ZealQuery(Wox):

    def query(self,key):
        results = []
        params = re.findall(r'(.*):',key)
        if (len(params) > 0):
            fun_params = key.replace(params[0]+":","")
            results.append({
                "Title": key,
                "IcoPath":"Images/app_zeal.png",
                "JsonRPCAction":{"method": "open_zeal", "parameters": [params[0],fun_params]}
            })
        else:
            results.append({
                "Title": key,
                "IcoPath":"Images/app_zeal.png",
                "JsonRPCAction":{"method": "open_zeal", "parameters": [key,""]}
            })
        return results

    def open_zeal(self,keys,query):
        """
            open zeal
        """
        os.startfile("dash-plugin://keys={}&query={}".format(keys,quote(query)))

if __name__ == "__main__":
    ZealQuery()
