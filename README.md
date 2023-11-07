# xiaowen-generate-server

## 快速开始

1. 建立pyenv环境(可选)

```shell
pyenv virtualenv 3.10.6 xiaowen-generate-server
```

2. 安装依赖：

```shell
pip install -r requirements.txt
```

3. 放置模型文件，将模型文件放置在`src/service/models/`下面，如果没有该目录，需要创建：

```shell
mkdir -p src/service/models
```

> 生成的结果放在: `src/service/result/` 下面

4. 启动服务：

```shell
uvicorn main:app --reload --host 127.0.0.1 --port 10102
```

5. 如果增加了新的依赖，生成requirements.txt：

```shell
pip freeze > requirements.txt
```

## 依赖版本控制
xformers 和 torch 的版本需要一致，否则会报错，目前使用的版本是：

```shell
pip install xformers==0.0.21

pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118

```

## minio docker 搭建：
in-one-line:
```shell
docker run -p 9000:9000 -p 9001:9001 -v G:\docker-data\minio\data:/data minio/minio server /data --console-address ":9001"
```