# memory_chat_app_v1

这是一个基于 Streamlit 和 DeepSeek API 的 AI 聊天伴侣小项目。

当前功能：

- 可以在网页里和 AI 对话。
- 支持流式输出，AI 回复会一点点显示。
- 支持多轮对话。
- 支持新建会话。
- 支持保存会话。
- 支持加载历史会话。
- 支持删除历史会话。
- 聊天记录会保存到 `sessions/` 文件夹里的 JSON 文件。

## 运行前准备

需要先配置环境变量：

```text
DEEPSEEK_API_KEY=你的 DeepSeek API Key
```

`.env.example` 是环境变量模板，只写变量名，不放真实密钥。

### `config.py` 和 `.env.example` 的区别

`config.py` 是项目真正会读取的配置文件，里面放的是：

```text
API_KEY_ENV_NAME = "DEEPSEEK_API_KEY"
BASE_URL = "https://api.deepseek.com"
MODEL_NAME = "deepseek-v4-pro"
```

意思是：

- 程序要读取的环境变量名字叫 `DEEPSEEK_API_KEY`。
- 模型接口地址是 `https://api.deepseek.com`。
- 当前使用的模型名是 `deepseek-v4-pro`。

`.env.example` 是给人看的模板，不是程序真正读取的密钥文件。

意思是告诉使用者：

```text
你需要准备一个 DEEPSEEK_API_KEY
```

所以它们不一样：

```text
config.py      程序配置
.env.example   密钥模板
```

### Windows PowerShell 临时配置方式

如果只想临时运行一次，可以在 PowerShell 里执行：

```powershell
$env:DEEPSEEK_API_KEY="你的真实 DeepSeek API Key"
```

然后再运行：

```powershell
streamlit run app.py
```

注意：这个配置只在当前 PowerShell 窗口有效。关掉窗口后，下次需要重新设置。

## 运行方式

在当前项目目录先安装依赖：

```powershell
pip install -r requirements.txt
```

再运行项目：

```powershell
streamlit run app.py
```

运行后，浏览器会打开一个本地页面。用户在页面底部输入内容，就可以和 AI 对话。

聊天记录会保存到：

```text
sessions/
```

项目目录示例：

```text
F:\python的学习\2026\2026.6.8(memory_chat_app_v1)
```

## 文件说明

```text
app.py          主程序，负责页面、聊天流程和会话保存
config.py       保存模型名、接口地址、环境变量名
llm_client.py   负责调用 DeepSeek 大模型
.env.example   环境变量模板，说明需要配置 DEEPSEEK_API_KEY
requirements.txt  记录项目需要安装的 Python 库
sessions/      保存聊天记录 JSON 文件
README.md      项目说明
```
