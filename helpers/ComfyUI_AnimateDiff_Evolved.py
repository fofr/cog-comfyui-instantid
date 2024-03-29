MODELS = [
    "mm_sd_v14.ckpt",
    "mm_sd_v15.ckpt",
    "mm_sd_v15_v2.ckpt",
    "mm_sdxl_v10_beta.ckpt",
    "v3_sd15_adapter.ckpt",
    "v3_sd15_mm.ckpt",
    "v3_sd15_sparsectrl_rgb.ckpt",
    "v3_sd15_sparsectrl_scribble.ckpt",
    "temporaldiff-v1-animatediff.ckpt",
]

LORAS = [
    "v2_lora_PanLeft.ckpt",
    "v2_lora_PanRight.ckpt",
    "v2_lora_RollingAnticlockwise.ckpt",
    "v2_lora_RollingClockwise.ckpt",
    "v2_lora_TiltDown.ckpt",
    "v2_lora_TiltUp.ckpt",
    "v2_lora_ZoomIn.ckpt",
    "v2_lora_ZoomOut.ckpt",
]

class ComfyUI_AnimateDiff_Evolved:
    @staticmethod
    def loras():
        return LORAS

    @staticmethod
    def models():
        return MODELS

    @staticmethod
    def weights_map(base_url):
        return {
            model: {
                "url": f"{base_url}/custom_nodes/ComfyUI-AnimateDiff-Evolved/{model}.tar",
                "dest": "ComfyUI/custom_nodes/ComfyUI-AnimateDiff-Evolved/models",
            }
            for model in MODELS
        } | {
            lora: {
                "url": f"{base_url}/custom_nodes/ComfyUI-AnimateDiff-Evolved/{lora}.tar",
                "dest": "ComfyUI/custom_nodes/ComfyUI-AnimateDiff-Evolved/motion_lora",
            }
            for lora in LORAS
        }
