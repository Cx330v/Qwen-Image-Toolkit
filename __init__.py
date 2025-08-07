import traceback
try:
    from .loader_nodes import QwenImageLoraLoader
    from .prompt_nodes import QwenImagePromptStyler
    from .latent_nodes import QwenImageLatentAspectRatio
    NODE_CLASS_MAPPINGS = {
        "QwenImageLoraLoader": QwenImageLoraLoader,
        "QwenImagePromptStyler": QwenImagePromptStyler,
        "QwenImageLatentAspectRatio": QwenImageLatentAspectRatio,
    }
    NODE_DISPLAY_NAME_MAPPINGS = {
        "QwenImageLoraLoader": "Qwen-Image LoRA 加载器",
        "QwenImagePromptStyler": "Qwen-Image 提示词",
        "QwenImageLatentAspectRatio": "Qwen-Image 图像比例",
    }    
    print("--- Qwen Image Toolkit: All nodes loaded successfully. ---")

except Exception as e:
    print(f"!!! Qwen Image Toolkit: Failed to load nodes. Error: {e}")
    print(f"Traceback: {traceback.format_exc()}")