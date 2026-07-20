# 西电高代与矩阵实验室 · Streamlit 版

本项目把原始单文件 `matrix_lab.html` 嵌入 Streamlit，保留其前端交互、图像上传、音频处理、Canvas 和 Web Worker 计算逻辑。

## 项目文件

- `app.py`：Streamlit 入口与自适应 iframe 外壳。
- `matrix_lab.html`：原始实验室网页，保持为独立 UTF-8 文件。
- `requirements.txt`：Streamlit Cloud 的 Python 依赖。
- `runtime.txt`：建议使用 Python 3.11。
- `.streamlit/config.toml`：页面主题和无头服务器配置。

## 本地运行

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## 部署到 Streamlit Community Cloud

1. 将本目录中的全部文件提交到 GitHub 仓库。
2. 在 Streamlit Community Cloud 选择 **Create app**。
3. Repository 选择目标仓库，Branch 选择 `main`。
4. Main file path 填写 `app.py`。
5. 在 Advanced settings 中选择 Python 3.11。
6. 点击 Deploy。

## 登录提示

原 HTML 使用浏览器端固定密码 `xdugaodai`。该密码会随网页代码发送到访问者浏览器，只适合演示入口，不能作为真正的访问控制。如果需要保护公开部署，应改用 Streamlit Secrets 配合服务器端身份验证。
