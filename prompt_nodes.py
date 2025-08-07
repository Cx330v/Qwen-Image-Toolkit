class QwenImagePromptStyler:
    STYLE_KEYWORDS = {
        "电影感 (默认)": "Ultra HD, 4K, cinematic composition, professional color grading, high detail",
        "照片级真实感": "photorealistic, hyperrealistic, 8K, sharp focus, detailed skin texture, professional photography",
        "动漫 / 动画": "anime style, key visual, vibrant colors, detailed illustration, by studio ghibli",
        "数字艺术 / 插画": "digital illustration, concept art, intricate details, trending on artstation, sharp focus",
        "摄影 (人像)": "dslr photo, sharp focus, 85mm lens, f/1.8, soft lighting, detailed face",
        "漫画书 / 图画小说": "comic book style, graphic novel art, bold lines, vibrant colors, halftone patterns",
    }
    STYLES = ["无"] + list(STYLE_KEYWORDS.keys())

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "A cat"}),
                "style": (s.STYLES, {"default": "电影感 (默认)"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "apply_style"
    CATEGORY = "text/Qwen_Image_Toolkit"

    def apply_style(self, text, style):
        if style == "无" or style not in self.STYLE_KEYWORDS:
            return (text,)
            
        style_text = self.STYLE_KEYWORDS[style]
        
        if text.strip() and not text.strip().endswith(","):
            text += ", "
            
        full_prompt = text + style_text
        return (full_prompt,)