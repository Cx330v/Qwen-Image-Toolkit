# ComfyUI/custom_nodes/Qwen_Image_Toolkit/loader_nodes.py

import torch
import comfy.utils
import comfy.sd
import folder_paths
import os
import json

class QwenImageLoraLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",), 
                "clip": ("CLIP",), 
                "lora_name": (folder_paths.get_filename_list("loras"),),
                "strength_model": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                "strength_clip": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                "lora_alpha": ("FLOAT", {
                    "default": 0.0, 
                    "min": 0.0, 
                    "max": 128.0, 
                    "step": 0.1, 
                    "tooltips": "Set to 0 to auto-detect from the LoRA's config file, otherwise specify the value manually."
                }),
            }
        }
        
    RETURN_TYPES = ("MODEL", "CLIP")
    FUNCTION = "load_qwen_lora"
    CATEGORY = "loaders/Qwen_Image_Toolkit"

    def _get_lora_alpha(self, lora_path, manual_alpha):
        if manual_alpha > 0.0:
            return manual_alpha
            
        config_path = os.path.join(os.path.dirname(lora_path), 'adapter_config.json')
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f: config = json.load(f)
                alpha = config.get('lora_alpha')
                if alpha is not None:
                    return float(alpha)
            except Exception:
                pass # Fail silently
        return 16.0

    def _convert_keys(self, state_dict, lora_alpha):
        new_sd = {}
        for key, value in state_dict.items():
            if 'lora_' not in key: continue
            
            new_key = key.replace(".default.weight", "")
            
            if new_key.endswith(".lora_A"):
                new_key = new_key.replace(".lora_A", ".lora.down.weight")
            elif new_key.endswith(".lora_B"):
                new_key = new_key.replace(".lora_B", ".lora.up.weight")
            else:
                continue
                
            final_key = "diffusion_model." + new_key
            new_sd[final_key] = value
            
            if final_key.endswith(".lora.down.weight"):
                alpha_key = final_key.replace(".lora.down.weight", ".alpha")
                new_sd[alpha_key] = torch.tensor(float(lora_alpha))
        return new_sd

    def load_qwen_lora(self, model, clip, lora_name, strength_model, strength_clip, lora_alpha):
        if strength_model == 0 and strength_clip == 0:
            return (model, clip)
            
        lora_path = folder_paths.get_full_path("loras", lora_name)
        alpha = self._get_lora_alpha(lora_path, lora_alpha)
        lora_state_dict = comfy.utils.load_torch_file(lora_path, safe_load=True)
        converted_lora_state_dict = self._convert_keys(lora_state_dict, alpha)
        
        model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, converted_lora_state_dict, strength_model, strength_clip)
        
        return (model_lora, clip_lora)