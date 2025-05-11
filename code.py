import requests


user_info = {
    "name": "Aman Sinotiya",
    "regNo": "0827IT221013",
    "email": "amansinotiya220678@acropolis.in"
}

print("Sending request to generate webhook...")
response = requests.post(
    "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
    json=user_info
)


if response.status_code != 200:
    print("Failed to generate webhook. Status Code:", response.status_code)
    print(response.text)
    exit()


data = response.json()
webhook_url = data["webhook"]
access_token = data["accessToken"]

print("Webhook URL:", webhook_url)
print("Access Token:", access_token)


reg_no_last_digit = int(user_info["regNo"][-1])
if reg_no_last_digit % 2 == 1:
    print("You should solve SQL Question 1 (Odd RegNo)")
    print("Download: https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxoskJWY/view?usp=sharing")
else:
    print("You should solve SQL Question 2 (Even RegNo)")
    print("Download: https://drive.google.com/file/d/1PO1ZvmDqAZJv77XRYsVben11Wp2HVb/view?usp=sharing")


final_sql_query = """SELECT 
    p.AMOUNT AS SALARY,
    e.FIRST_NAME || ' ' || e.LAST_NAME AS NAME,
    (strftime('%Y', 'now') - strftime('%Y', e.DOB) - 
    (strftime('%m-%d', 'now') < strftime('%m-%d', e.DOB)) AS AGE,
    d.DEPARTMENT_NAME
FROM 
    PAYMENTS p
JOIN 
    EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN 
    DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE 
    strftime('%d', p.PAYMENT_TIME) != '01'
ORDER BY 
    p.AMOUNT DESC
LIMIT 1;"""


print("Submitting your SQL solution...")
submission_data = {
    "finalQuery": final_sql_query
}

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submit_response = requests.post(
    webhook_url,
    headers=headers,
    json=submission_data
)

if submit_response.status_code == 200:
    print("Submission successful!")
else:
    print("Submission failed. Status Code:", submit_response.status_code)
    print(submit_response.text)
