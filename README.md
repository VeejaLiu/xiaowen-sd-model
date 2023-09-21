# xiaowen-generate-server

## 快速开始

建立pyenv环境(可选)

```shell
pyenv virtualenv 3.10.6 xiaowen-generate-server
```

安装依赖：

```shell
pip install -r requirements.txt
```

启动服务：

```shell
uvicorn main:app --reload --host 127.0.0.1 --port 10102
```

如果增加了新的依赖，生成requirements.txt：

```shell
pip freeze > requirements.txt
```
