# Please install OpenAI SDK first: `pip3 install openai`
# 打开终端安装
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的API_KEY的值)
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 与AI大模型进行交互(参数)
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "我喜欢你"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 输出大模型返回的结果
print(response.choices[0].message.content)