# memory_chat_app_v1 学习记录

这是我把黑马 107-119 的 AI 会话项目整理出来的小项目。

现在的重点不是“马上自己完整写出整个项目”，而是按小步骤把代码吃透：

> 看懂一小块 -> 遮住一小块，自己补 -> 改一个小功能 -> 做一个极简版聊天页面 -> 再做一个类似项目。

## 当前状态

正在进行：第一步，看懂一小块。

已经完成：

- 跟着视频敲完黑马 107-119。
- 项目功能可以跑起来。
- 已经把代码整理成几个文件：`app.py`、`llm_client.py`、`config.py`、`.env.example`、`requirements.txt`、`sessions/`。

现在要做的不是重听整套课，也不是硬背代码，而是每天拆一小块：

- 今天只看懂一个变量或一个判断。
- 明天只遮住几行代码自己补。
- 后面再慢慢改功能。

## 我们现在采用的五个小步骤

### 第一步：看懂一小块

目标：先理解项目里最小的一段代码。

比如：

```python
prompt = st.chat_input("请输入一句话")

if prompt:
    st.write(prompt)
```

这段代码先理解成：

- `prompt`：用户这一次输入的内容。
- `if prompt:`：如果用户真的输入了内容，才继续执行。
- `st.write(prompt)`：把用户输入的内容显示到页面上。

当前状态：进行中。

### 第二步：遮住一小块，自己补

目标：不是从零写完整项目，而是只遮住一小块，自己补回来。

例子：

```python
prompt = st.chat_input("请输入一句话")

if ______:
    st.write(______)
```

能补出这一小块，就算进步。

当前状态：未开始。

### 第三步：改一个小功能

目标：在已有代码基础上改一个很小的功能。

例子：

- 把标题改掉。
- 把输入框提示语改掉。
- 用户输入后，不只显示原文，而是显示：`你刚刚说：xxx`。
- 给空输入加提示。

当前状态：未开始。

### 第四步：做一个极简版聊天页面

目标：不看原项目，自己做一个很小的聊天页面。

这个极简版不要求调用大模型，先做到：

- 页面有标题。
- 页面底部有聊天输入框。
- 用户输入后，能显示用户消息。
- 能用 `st.session_state` 保存多轮消息。

当前状态：未开始。

### 第五步：再做一个类似项目

目标：用同样的思路，做一个和原项目相似但不完全一样的小项目。

例子：

- 学习陪伴聊天页面。
- 背单词问答助手。
- Python 错题记录助手。
- 读书笔记问答助手。

做到这一步，才说明我不是只会跟着敲，而是开始能迁移。

当前状态：未开始。

## 文件说明

```text
app.py              主程序，负责页面、聊天流程、会话保存和加载
llm_client.py       专门负责调用 DeepSeek 大模型
config.py           保存模型名、接口地址、环境变量名等配置
.env.example        环境变量模板，提醒使用者需要准备 DEEPSEEK_API_KEY
requirements.txt    记录项目需要安装的 Python 库
sessions/           保存聊天记录 JSON 文件
chat_models.py      放消息格式相关的小函数
README.md           项目说明和学习记录
```

## `chat_models.py` 是什么

`chat_models.py` 不是新知识点，也不是必须很复杂。

它现在只是把“消息长什么样”单独放出来：

```python
USER_ROLE = "user"
ASSISTANT_ROLE = "assistant"

def create_user_message(content):
    return {"role": USER_ROLE, "content": content}

def create_assistant_message(content):
    return {"role": ASSISTANT_ROLE, "content": content}
```

也就是说，以后原来写：

```python
{"role": "user", "content": prompt}
```

可以慢慢改成：

```python
create_user_message(prompt)
```

它的作用是让消息格式更统一。现在不用急着完全掌握，先知道它是“专门创建聊天消息的小工具”就行。

## `config.py` 和 `.env.example` 的区别

`config.py` 是程序真正会用到的配置文件。

比如：

```text
API_KEY_ENV_NAME = "DEEPSEEK_API_KEY"
BASE_URL = "https://api.deepseek.com"
MODEL_NAME = "deepseek-chat"
```

`.env.example` 是给人看的模板，用来提醒：

```text
你需要准备 DEEPSEEK_API_KEY
```

它们不是一个东西：

```text
config.py       程序配置
.env.example    密钥模板
```

## `requirements.txt` 是什么

`requirements.txt` 用来记录这个项目需要安装哪些库。

当前项目需要：

```text
streamlit
openai
```

别人拿到这个项目后，可以在当前目录运行：

```powershell
pip install -r requirements.txt
```

这样就不用一个一个手动安装库。

## 运行方式

先进入当前项目目录：

```powershell
cd "F:\python的学习\2026\2026.6.8(memory_chat_app_v1)"
```

安装依赖：

```powershell
pip install -r requirements.txt
```

临时配置 DeepSeek API Key：

```powershell
$env:DEEPSEEK_API_KEY="你的真实 DeepSeek API Key"
```

运行项目：

```powershell
streamlit run app.py
```

运行后，浏览器会打开一个本地页面。用户在页面底部输入内容，就可以和 AI 对话。

## 下一步要做什么

下一步继续第一步：看懂一小块。

要看的小块是：

```python
prompt = st.chat_input(...)

if prompt:
    ...
```

验收标准：

- 能说出 `prompt` 是“用户这一次输入的内容”。
- 能说出 `if prompt:` 是“有输入才执行里面的代码”。
- 能运行一个只有输入框和显示文本的最小页面。

完成后再进入第二步：遮住一小块，自己补。

