""" license-usage.py
    Copyright (C) 2023  Olivia Mativi

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import requests

url = '<SITE WS URL>'
auth = {
    "arguments":{
        "apiKey":"<API KEY>",
        "logoutCurrentWebConnection":"false"
    },
    "methodName":"connectWithApiKey",
    "serviceName":"ConnectionService"
}
connectionID = (requests.post(url, json = auth).json())['result']

reqJSON = {
"arguments":{
    "count":99999,
    "startIndex":"1",
    "connectionID":connectionID,
    "includeRoleMembership":"True"
},
"methodName":"getAllUsers",
"serviceName":"UserService"}
allUserJSON = requests.get(url, json = reqJSON).json()

fullLicenseNum = 0
basicLicenseNum = 0
numUsers = len(allUserJSON['result']['users'])
print("Total number of users: " + str(numUsers))

for i in allUserJSON['result']['users']:
    for j in i['roles']:
        if j['name'].endswith('F'):
            fullLicenseNum += 1
            break
        elif j['name'].endswith('B'):
            basicLicenseNum += 1
            break

print("Full Licenses: " + str(fullLicenseNum) + 
      "\nBasic Licenses: " + str(basicLicenseNum))