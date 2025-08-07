# Qwen Image Toolkit for ComfyUI

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A collection of essential nodes designed to seamlessly integrate Alibaba's Qwen-Image model and its specific LoRA format into the ComfyUI workflow.

---

## Node Previews

### 1. Qwen-Image LoRA 加载器
A specialized LoRA loader that correctly handles the key conversion for Qwen-Image LoRAs. It features an auto-detect mechanism for the `alpha` value.
![LoRA Loader Node](example/loader.png)

### 2. Qwen-Image 提示词
A prompt styler node that quickly appends professional-grade keywords to your prompt, allowing you to easily switch between various artistic styles like cinematic, photorealistic, anime, etc.
![Prompt Styler Node](example/prompt.png)

### 3. Qwen-Image 图像比例
Provides a set of recommended aspect ratios for Qwen-Image, along with a "Custom" option for manual input. Ensures output dimensions are valid.
![Aspect Ratio Node](example/latent.png)

## Example Workflow

![Example Workflow](example/workflow.png)

---

## 安装 (Installation)

### 方法 1: 使用 ComfyUI Manager (推荐)
1.  启动 ComfyUI。
2.  打开 **ComfyUI Manager** 菜单。
3.  点击 **"Install Custom Nodes"**。
4.  搜索 `Qwen Image Toolkit`。
5.  点击 **"Install"** 按钮，安装完成后重启 ComfyUI。

### 方法 2: 手动安装 (Git Clone)
1.  进入 ComfyUI 的自定义节点目录：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆本仓库：
    ```bash
    git clone https://github.com/Cx330v/Qwen-Image-Toolkit.git
    ```
3.  重启 ComfyUI。

---

## 使用说明 (Usage)

* **Qwen-Image LoRA 加载器**:
    * 将 `lora_alpha` 设为 `0` (默认值) 来自动从 `adapter_config.json` 文件中读取 alpha 值。
    * 如果需要手动覆盖，可以直接输入一个大于0的 alpha 值。
* **Qwen-Image 提示词**:
    * 在 `text` 框中输入您的基础提示词。
    * 从 `style` 下拉菜单中选择一个风格，对应的风格化关键词会自动附加到您的提示词末尾。
* **Qwen-Image 图像比例**:
    * 从 `aspect_ratio` 下拉菜单中选择一个预设的比例。
    * 或者，选择 `Custom 自定义` 并手动设置 `custom_width` 和 `custom_height`。

## 许可证 (License)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
