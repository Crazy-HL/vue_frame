from zhipuai import ZhipuAI
client = ZhipuAI(api_key="1386125343a2090a113a41476c059c35.rYhIyn9tkmYL7sdl")  # Please fill in your own APIKey


html_content = ''
with open('test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


response = client.chat.completions.create(
    model="glm-4-long",  # Please fill in the model name you want to call
    messages=[
        {"role": "system", "content": "你是一个HTML文件解析专家、数据提取能手。"},
        {"role": "user", "content": f"从中提取表格内的数据"},
    ],
)
print(response.choices[0].message)