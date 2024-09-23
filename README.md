# xiaowen-generate-server

## 项目介绍
本项目为《小纹AI》的一部分。主要功能是提供 Stable diffusion 相关模型，以及训练集。 

## minio docker 搭建：
in-one-line:
```shell
docker run -p 9000:9000 -p 9001:9001 -v G:\docker-data\minio\data:/data minio/minio server /data --console-address ":9001"
```