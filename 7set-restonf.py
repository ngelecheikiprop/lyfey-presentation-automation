import requests


base_url = "http://192.168.100.2:3000"

auth = (
    "lab",
    "lab123"
)


payload = """
<lock-configuration/>

<load-configuration action="set" format="text">
    <configuration-set>
        set interfaces ge-0/0/6 description CONFIGURED_USING_REST_API
        set interfaces ge-0/0/6 unit 0 family inet address 10.10.17.1/30
    </configuration-set>
</load-configuration>

<commit/>

<unlock-configuration/>
"""

#set interfaces ge-0/0/6 unit 0 family inet address 10.10.17.1/30

response = requests.post(
    f"{base_url}/rpc?stop-on-error=1",
    auth=auth,
    headers={
        "Content-Type": "application/xml"
    },
    data=payload
)


print("REST API configuration response:")
print(response.status_code)
print(response.text)


response = requests.get(
    f"{base_url}/rpc/get-interface-information",
    auth=auth,
    params={
        "interface-name": "ge-0/0/6"
    }
)


print("Interface output:")
print(response.text)