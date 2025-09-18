import os
import dashscope

audio_file = "file://" + os.path.abspath('需求.mp3')

messages = [
    {
        "role": "system",
        "content": [
            # 此处用于配置定制化识别的Context
            {"text": ""},
        ]
    },
    {
        "role": "user",
        "content": [
            {"audio": audio_file},
        ]
    }
]
response = dashscope.MultiModalConversation.call(
    api_key="sk-61494595dd154d63bba6620946afb848",
    model="qwen3-asr-flash",
    messages=messages,
    result_format="message",
    asr_options={
        "language": "zh",
        "format": "mp3",
        "enable_lid":True,
        "enable_itn":False
    }
)
print(response)
